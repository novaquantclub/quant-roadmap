import base64
import io
import pickle
import zlib
import numpy as np
import pandas as pd
import yfinance as yf
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.preprocessing import StandardScaler


class QuantLSTM(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 32, num_layers: int = 2, dropout: float = 0.3):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.layer_norm = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        lstm_out, _ = self.lstm(x)
        last_step = lstm_out[:, -1, :]
        out = self.layer_norm(last_step)
        out = self.dropout(out)
        return self.fc(out)


class Trader:
    # Any valid yfinance ticker(s)
    tickers = [
        "SPY",
        "QQQ",
        "GLD",
    ]  # Mandatory: declare the tickers you want to trade here

    def __init__(self):
        self.name = "Pre-Trained 10Y QuantLSTM Strategy"
        self.author = "David Catalim"

        self.seq_len = 20
        self.hidden_dim = 32
        self.num_layers = 2
        self.rebalance_band = 0.05
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.feature_cols = [
            "Log_Ret",
            "Ret_Lag1",
            "Ret_Lag2",
            "Rolling_Vol_10",
            "Momentum_5",
            "Momentum_10",
            "Vol_ZScore",
        ]

        # Download 10 years of data, train LSTMs, and serialize into <100 KB string
        self._initial_trader_data = self._train_and_serialize_10y()

    def _compute_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Constructs the 7 stationary features from the lab pipeline."""
        feat = pd.DataFrame(index=df.index)

        close = df["Close"]
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]
        close = close.astype(float)

        log_ret = np.log(close / close.shift(1))
        feat["Log_Ret"] = log_ret
        feat["Ret_Lag1"] = log_ret.shift(1)
        feat["Ret_Lag2"] = log_ret.shift(2)
        feat["Rolling_Vol_10"] = log_ret.rolling(10).std()
        feat["Momentum_5"] = log_ret.rolling(5).sum()
        feat["Momentum_10"] = log_ret.rolling(10).sum()

        if "Volume" in df.columns:
            vol = df["Volume"]
            if isinstance(vol, pd.DataFrame):
                vol = vol.iloc[:, 0]
            vol = vol.astype(float)
            if (vol > 0).any():
                vol_std = vol.rolling(20).std().replace(0, np.nan)
                feat["Vol_ZScore"] = ((vol - vol.rolling(20).mean()) / vol_std).fillna(0.0)
            else:
                feat["Vol_ZScore"] = 0.0
        else:
            feat["Vol_ZScore"] = 0.0

        return feat[self.feature_cols]

    @staticmethod
    def _create_sequences(features: np.ndarray, targets: np.ndarray, seq_len: int = 20):
        X, y = [], []
        for i in range(seq_len, len(features)):
            X.append(features[i - seq_len : i])
            y.append(targets[i - 1])
        return (
            torch.tensor(np.array(X), dtype=torch.float32),
            torch.tensor(np.array(y), dtype=torch.float32).unsqueeze(1),
        )

    def _train_and_serialize_10y(self) -> str:
        """Downloads 10Y data, trains an LSTM per ticker, and compresses weights under 100 KB."""
        np.random.seed(42)
        torch.manual_seed(42)
        trained_bundle = {}

        for ticker in self.tickers:
            try:
                df = yf.download(ticker, period="10y", interval="1d", progress=False)
                if df is None or len(df) < 250:
                    continue

                feat_df = self._compute_features(df)
                feat_df["Target_Next_Ret"] = feat_df["Log_Ret"].shift(-1) * 100.0
                clean_df = feat_df.dropna()

                # Chronological Split (85% Train, 15% Validation for Early Stopping)
                split_idx = int(len(clean_df) * 0.85)
                train_df = clean_df.iloc[:split_idx]
                val_df = clean_df.iloc[split_idx:]

                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(train_df[self.feature_cols].values)
                X_val_scaled = scaler.transform(val_df[self.feature_cols].values)

                y_train_raw = train_df["Target_Next_Ret"].values
                y_val_raw = val_df["Target_Next_Ret"].values

                X_train, y_train = self._create_sequences(X_train_scaled, y_train_raw, self.seq_len)
                X_val, y_val = self._create_sequences(X_val_scaled, y_val_raw, self.seq_len)

                train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=False)
                val_loader = DataLoader(TensorDataset(X_val, y_val), batch_size=64, shuffle=False)

                model = QuantLSTM(
                    input_dim=len(self.feature_cols),
                    hidden_dim=self.hidden_dim,
                    num_layers=self.num_layers,
                    dropout=0.3,
                ).to(self.device)

                criterion = nn.HuberLoss(delta=1.0)
                optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)

                best_val_loss = float("inf")
                best_state = None

                for _ in range(25):
                    model.train()
                    for X_b, y_b in train_loader:
                        X_b, y_b = X_b.to(self.device), y_b.to(self.device)
                        optimizer.zero_grad()
                        loss = criterion(model(X_b), y_b)
                        loss.backward()
                        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                        optimizer.step()

                    model.eval()
                    val_losses = []
                    with torch.no_grad():
                        for X_b, y_b in val_loader:
                            X_b, y_b = X_b.to(self.device), y_b.to(self.device)
                            val_losses.append(criterion(model(X_b), y_b).item())

                    val_loss = float(np.mean(val_losses))
                    if val_loss < best_val_loss:
                        best_val_loss = val_loss
                        # Cast weights to float16 so 3 LSTM models easily fit under the 100 KB limit
                        best_state = {k: v.detach().cpu().half().numpy() for k, v in model.state_dict().items()}

                trained_bundle[ticker] = {
                    "scaler_mean": scaler.mean_.astype(np.float32),
                    "scaler_scale": scaler.scale_.astype(np.float32),
                    "state_dict": best_state,
                }
            except Exception:
                continue

        compressed = zlib.compress(pickle.dumps(trained_bundle), level=9)
        return base64.b64encode(compressed).decode("ascii")

    def run(self, state) -> dict:
        orders = {}

        # 1. Persist and load compressed LSTM weights from state.trader_data
        if not getattr(state, "trader_data", None):
            state.trader_data = self._initial_trader_data

        try:
            raw_bytes = zlib.decompress(base64.b64decode(state.trader_data.encode("ascii")))
            trained_bundle = pickle.loads(raw_bytes)
        except Exception:
            raw_bytes = zlib.decompress(base64.b64decode(self._initial_trader_data.encode("ascii")))
            trained_bundle = pickle.loads(raw_bytes)

        target_allocation_per_ticker = state.portfolio_value / len(self.tickers)

        # 2. Reconstruct LSTM and run 3D sequence inference on each ticker
        for ticker, df in state.history.items():
            # Need at least 20 bars for rolling window warmup + 20 bars for LSTM sequence lookback
            if ticker not in trained_bundle or len(df) < self.seq_len + 21:
                continue

            feat_df = self._compute_features(df).dropna()
            if len(feat_df) < self.seq_len:
                continue

            # Extract the latest 20-day window of features
            recent_window = feat_df.iloc[-self.seq_len :].values

            bundle = trained_bundle[ticker]
            scaled_window = (recent_window - bundle["scaler_mean"]) / bundle["scaler_scale"]

            # Rebuild model and load saved weights
            model = QuantLSTM(
                input_dim=len(self.feature_cols),
                hidden_dim=self.hidden_dim,
                num_layers=self.num_layers,
                dropout=0.0,
            ).to(self.device)
            state_dict = {
                k: torch.tensor(v, dtype=torch.float32, device=self.device)
                for k, v in bundle["state_dict"].items()
            }
            model.load_state_dict(state_dict)
            model.eval()

            # Shape: (1, 20, 7) -> (Batch=1, Seq_Len=20, Features=7)
            X_live = torch.tensor(scaled_window, dtype=torch.float32, device=self.device).unsqueeze(0)
            with torch.no_grad():
                pred_pct = float(model(X_live).cpu().item())

            # Conviction sizing: tanh-squashed forecast clipped to [0.0, 1.0]
            conviction = float(np.clip(np.tanh(pred_pct * 3.0), 0.0, 1.0))

            current_price = float(df["Close"].iloc[-1])
            current_pos = state.positions.get(ticker, 0.0)
            current_weight = (current_pos * current_price) / target_allocation_per_ticker

            if abs(conviction - current_weight) > self.rebalance_band:
                target_value = target_allocation_per_ticker * conviction
                target_shares = np.floor(target_value / current_price)
                orders[ticker] = target_shares - current_pos

        return orders