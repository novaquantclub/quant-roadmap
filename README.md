# 8-Week Quantitative Finance Roadmap

## Program Overview
This curriculum bridges traditional economic and corporate finance theory with quantitative implementation, machine learning, time-series econometrics, and algorithmic backtesting in Python. 

* **Prerequisites:** Introductory Micro/Macroeconomics, basic statistics, Linear Algebra, Multivariable Calculus, and basic Python familiarity (`pandas`, `numpy`).
* **Core Tooling:** `numpy`, `pandas`, `scipy`, `statsmodels`, `scikit-learn`, `matplotlib`/`seaborn`, `yfinance`.

## Semester Research Project
Students work in teams of two on one quantitative-finance research question throughout the semester. The project is an independent track that can draw on relevant course material as needed; teams are not expected to use every weekly topic. Each team submits a short research report, reproducible code, and a final presentation.

### Project Milestones
* **Weeks 1–2:** Select a topic, formulate a research question, identify the required data, and submit a brief proposal describing the hypothesis, assets, methods, and evaluation criteria.
* **Weeks 3–4:** Complete the literature and data review and present preliminary descriptive results. Apply portfolio or factor methods only where they support the research question.
* **Weeks 5–6:** Implement the core empirical method and document choices about estimation, validation, and avoidance of look-ahead bias. Use time-series or statistical-arbitrage methods where appropriate.
* **Week 7:** Apply a directional or cross-sectional ranking model only if it is appropriate to the research question, and evaluate its robustness, economic value, and risk of overfitting.
* **Week 8:** Submit the final report, reproducible code, and presentation, including the relevant backtest and risk analysis for the project.

### Suggested Research Topics
* Momentum versus mean reversion in equities or ETFs, including transaction costs and out-of-sample performance.
* Portfolio construction: compare equal-weighted, minimum-variance, and factor-based portfolios.
* Factor investing: evaluate whether CAPM or Fama-French factors explain the returns of a selected fund or sector.
* Volatility forecasting: compare historical, GARCH, and option-implied volatility forecasts.
* Statistical arbitrage: investigate cointegration and pairs-trading opportunities within an industry or asset class.
* Machine-learning prediction: compare regression or tree-based models for forecasting stock returns or price direction against a simple baseline.
* Machine-learning feature analysis: study whether technical indicators, lagged returns, or market variables improve out-of-sample predictions.
* Quantitative risk management: compare VaR and Expected Shortfall under different distributional assumptions and market-stress scenarios.

---

## Phase 1: Foundations (Weeks 1–2)

### Week 1: Python for Financial Data & Market Microstructure
* **Core Topics:**
  * Order book mechanics: bids, asks, market depth, bid-ask spread, slippage.
  * Tick-level vs. OHLCV data.
  * Stylized facts of financial time series: fat tails, leptokurtosis, volatility clustering, autocorrelation of absolute returns.
* **Technical Skills:**
  * Vectorized data processing with `numpy` and `pandas`.
  * Pulling historical data using market APIs (`yfinance`, CCXT, or Alpaca).
  * Computing log returns versus arithmetic returns and understanding compounding.
* **Deliverable / Lab:**
  * **Lab 1:** Analyze five years of daily `SPY` and `TLT` data by computing returns, summarizing their descriptive statistics and distributions, and presenting the findings with visualizations of volatility and normality.

---

### Week 2: Momentum & Mean-Reversion Algorithmic Strategies
* **Core Topics:**
  * Signal generation logic: Simple Moving Averages (SMA), Exponential Moving Averages (EMA), Relative Strength Index (RSI), Bollinger Bands.
  * Common backtesting pitfalls: look-ahead bias, survivorship bias, data snooping.
  * Performance metrics: Sharpe Ratio, Sortino Ratio, Maximum Drawdown, Calmar Ratio, Win/Loss Rate.
* **Technical Skills:**
  * Vectorized strategy backtesting frameworks.
  * Modeling execution costs: transaction fees and slippage models.
* **Deliverable / Lab:**
  * **Lab 2:** Implement a vectorized dual moving-average crossover strategy for an equity index ETF. Compare performance under zero transaction costs versus realistic institutional friction levels ($0.005/share + 5 bps slippage).

---

## Phase 2: Quantitative Portfolio Management (Weeks 3–4)

### Week 3: Modern Portfolio Theory (MPT) & The Efficient Frontier
* **Core Topics:**
  * Markowitz mean-variance framework: expected return vector and covariance matrix $\Sigma$.
  * Global Minimum Variance (GMV) portfolio, Capital Allocation Line (CAL), and the Tangency Portfolio.
  * Covariance matrix estimation errors and shrinkage estimators (Ledoit-Wolf).
* **Technical Skills:**
  * Convex optimization using `scipy.optimize`.
  * Portfolio constraint handling (long-only, target return, sector-bound constraints).
* **Deliverable / Lab:**
  * **Lab 3:** Build an interactive Efficient Frontier generator for a 10-asset universe. Run an out-of-sample backtest comparing the theoretical Tangency Portfolio against an equal-weighted ($1/N$) benchmark.

---

### Week 4: Multi-Factor Models & Asset Pricing
* **Core Topics:**
  * Capital Asset Pricing Model (CAPM) and idiosyncratic risk.
  * Fama-French 3-Factor (Market, SMB, HML) and 5-Factor models (RMW, CMA).
  * Statistical factor modeling: Principal Component Analysis (PCA) on cross-sectional equities.
* **Technical Skills:**
  * Multivariate Ordinary Least Squares (OLS) regressions using `statsmodels`.
  * Rolling factor beta attribution and alpha estimation ($t$-statistics and $p$-values).
  * Dimensionality reduction using `scikit-learn.decomposition.PCA`.
* **Deliverable / Lab:**
  * **Lab 4:** Download historical Fama-French factor returns. Deconstruct the performance of an actively managed fund (e.g., Berkshire Hathaway or ARKK) to isolate true manager alpha from systemic factor exposures.

---

## Phase 3: Time Series Econometrics & Statistical Arbitrage (Weeks 5–6)

### Week 5: Time Series Econometrics & Volatility Modeling
* **Core Topics:**
  * Stationarity, unit roots, and why financial returns are preferred to prices for modeling.
  * A practical introduction to the Augmented Dickey-Fuller (ADF) test and interpreting autocorrelation.
  * Volatility clustering and the basic ARCH/GARCH framework.
* **Technical Skills:**
  * Transforming price data into returns and inspecting ACF plots.
  * Fitting and interpreting a simple GARCH model using the `arch` Python package.
* **Deliverable / Lab:**
  * **Lab 5:** Test the stationarity of S&P 500 prices and returns, visualize volatility clustering, and use a simple GARCH model to produce a short-horizon volatility forecast.

---

### Week 6: Cointegration & Pairs Trading (Statistical Arbitrage)
* **Core Topics:**
  * Correlation versus Cointegration ($I(1)$ series cointegrated to $I(0)$ spread).
  * Engle-Granger two-step method and the Johansen test.
  * Mean-reverting processes: Ornstein-Uhlenbeck (OU) equation and the half-life of mean reversion.
* **Technical Skills:**
  * Computing dynamic hedge ratios via rolling OLS and Kalman filters.
  * Z-score normalization for spread threshold execution.
* **Deliverable / Lab:**
  * **Lab 6:** Screen an equity sector (e.g., Energy or Utilities) for cointegrated pairs. Build an automated pairs trading backtester with $z$-score entry/exit bands ($z = \pm 2.0$ entry, $z = 0.0$ exit) and stop-loss criteria.

---

## Phase 4: Machine Learning & Risk Analytics (Weeks 7–8)

### Week 7: Machine Learning for Return Direction & Cross-Sectional Ranking
* **Core Topics:**
  * Classification of positive versus negative future returns.
  * Cross-sectional ranking of stocks by expected relative return.
  * Feature engineering from market data, technical indicators, and lagged returns.
  * Model validation, time-series cross-validation, overfitting, and data leakage.
* **Technical Skills:**
  * Classification and ranking models using `scikit-learn`.
  * Feature selection, hyperparameter tuning, and out-of-sample evaluation.
  * Comparing directional accuracy, ranking quality, and portfolio performance with appropriate baselines.
* **Deliverable / Lab:**
  * **Lab 7:** Build and evaluate a machine-learning model that predicts return direction or ranks stocks by expected relative return using strictly time-ordered data. Compare it with a simple baseline and discuss predictive performance, economic significance, and limitations.

---

### Week 8: Risk Management & Capstone Strategy Showcase
* **Core Topics:**
  * Value at Risk (VaR): Parametric, Historical, and Monte Carlo approaches.
  * Coherent risk measures: Expected Shortfall (CVaR).
  * Portfolio stress testing, scenario analysis, and maximum leverage limits.
* **Technical Skills:**
  * Consolidating execution, factor exposures, and risk reporting into unified dashboards.
  * Generating tear-sheets using `quantstats`.
* **Deliverable / Capstone:**
  * **Lab 8:** Produce a quantitative risk report using VaR, Expected Shortfall, drawdown analysis, and stress-testing scenarios.
  * **Final Showcase:** Student teams present their research project and its quantitative investment or trading implications to the club.
    * **Requirements:**
      1. Economic/market anomaly thesis.
      2. Factor exposure and risk decomposition.
      3. Out-of-sample backtest with transaction costs.
      4. Risk report (VaR, CVaR, drawdown duration).
      5. Execution/liquidity constraints.