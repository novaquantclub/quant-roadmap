# 10-Week Quantitative Finance Roadmap

## Program Overview
This curriculum bridges traditional economic and finance theory with quantitative implementation, machine learning, time-series econometrics, and algorithmic backtesting in Python. 

* **Prerequisites:** Introductory Micro/Macroeconomics, basic statistics, Linear Algebra, and Multivariable Calculus. No prior programming or Git experience is required.
* **Core Tooling:** `numpy`, `pandas`, `scipy`, `statsmodels`, `scikit-learn`, `matplotlib`/`seaborn`, `yfinance`.

## Semester Research Project
Each team works on one quantitative-finance research question throughout the semester. The project is an independent track that can draw on relevant course material from the learning sessions as needed; the team is not expected to use every weekly topic. The project must produce a fully specified trading strategy for inclusion in the club's paper-trading portfolio, supported by a short research paper, reproducible code, and a final presentation.

### Project Milestones
* **Weeks 1–2:** Select a topic, formulate a research question, identify the required data, and submit a brief proposal describing the hypothesis, assets, methods, and evaluation criteria.
* **Weeks 3–5:** Complete the literature and data review and present preliminary descriptive results. Apply AI-assisted research, backtesting, or factor methods only where they support the research question.
* **Week 6:** Implement the core empirical method and document choices about estimation, validation, and avoidance of look-ahead bias. Use statistical-arbitrage methods where appropriate.
* **Week 7:** Apply a directional or cross-sectional ranking model only if it is appropriate to the research question, and evaluate its robustness, economic value, and risk of overfitting.
* **Weeks 9–10:** Finalize the paper, reproducible code, and presentation. Deliver the selected trading strategy with its signal logic, universe, position-sizing rules, execution assumptions, risk limits, monitoring plan, and relevant backtest and risk analysis for review before inclusion in the club's paper-trading portfolio.

### Suggested Research Topics
* **Volatility-managed momentum:** Does scaling momentum exposure by realized volatility improve out-of-sample risk-adjusted returns and reduce drawdowns after transaction costs?
* **Momentum versus mean reversion across market regimes:** Can volatility and trend conditions identify when a momentum or mean-reversion strategy should be given greater portfolio weight?
* **Cointegration-based sector pairs trading:** Can dynamically selected cointegrated pairs produce market-neutral returns after accounting for hedge-ratio instability, slippage, and liquidity constraints?
* **Factor timing:** Can market and macroeconomic signals improve the timing of exposure to value, size, profitability, investment, and momentum factors?
* **Machine-learning cross-sectional ranking:** Can lagged returns, volatility, liquidity, and technical features improve stock selection relative to a simple momentum or equal-weight baseline?
* **Machine-learning trade selection for pairs trading:** Can a model identify which statistically valid pairs are most likely to converge profitably?
* **Trend following with tail-risk controls:** Can volatility scaling, drawdown limits, or defensive hedges reduce crash losses without eliminating the return benefit of trend following?
* **Options-based tail-risk protection:** Can a systematic protective-put or put-spread overlay improve portfolio resilience at an acceptable long-run cost?
* **Delta-hedged volatility strategies:** Does trading the difference between implied and realized volatility generate robust returns after hedging costs and option-market frictions?
* **Multi-signal portfolio construction:** Does combining momentum, value, mean reversion, and defensive signals with portfolio-level risk limits improve stability and reduce factor concentration?

---

## Week 0: Computing & Collaboration for Total Beginners (Optional)

Week 0 is a hands-on orientation for members who have never programmed or used developer tools. The goal is not to master every tool, but to become comfortable opening a notebook, running small experiments, reading simple errors, and keeping work reproducible.

* **Python basics:** Variables, strings, numbers, lists, dictionaries, `for` loops, conditionals, functions, imports, and reading error messages. Practice by writing small calculations and a function that summarizes a list of prices.
* **Jupyter basics:** Create and run a notebook, understand the difference between Markdown and code cells, restart the kernel, run cells in order, and save a notebook with outputs. Learn why a notebook should be rerun from a clean kernel before it is shared.
* **pandas basics:** Load a small CSV, inspect a `DataFrame` with `head`, `shape`, `info`, and `describe`, select columns and rows, handle missing values, and make one simple plot.
* **Git basics:** Install or verify Git, configure a username, initialize or clone a repository, check status, add files, commit changes, inspect history, and understand the difference between a local commit and a remote repository.
* **GitHub basics:** Create or join the club repository, clone it, create a branch, push a commit, open a pull request, review a change, and pull updates from the shared repository. Never commit passwords, API keys, or private data.
* **Working habits:** Use clear filenames, keep one idea per notebook, write short Markdown explanations next to code, and record the data source and assumptions for every analysis.

---

## Phase 1: Foundations (Weeks 1–2)

### Week 1: Python for Financial Data & Market Microstructure (28/9 to 4/10)
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

### Week 2: Momentum & Mean-Reversion Algorithmic Strategies (5/10 to 11/10)
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

## Phase 2: AI-Assisted Strategy Research & Quantitative Portfolio Management (Weeks 3–5)

### Week 3: Proper Backtesting & Strategy Validation (12/10 to 18/10)
* **Core Topics:**
  * Backtest design: defining the investment universe, signal timing, execution timing, portfolio rules, and rebalancing frequency.
  * Avoiding look-ahead bias, survivorship bias, data leakage, and unrealistic fills.
  * In-sample versus out-of-sample testing, walk-forward validation, benchmark selection, and sensitivity analysis.
* **Technical Skills:**
  * Building event-driven or vectorized backtests with point-in-time data and explicit signal-to-trade delays.
  * Modeling commissions, bid-ask spreads, slippage, turnover, liquidity limits, and position constraints.
  * Evaluating returns, volatility, Sharpe and Sortino ratios, maximum drawdown, turnover, capacity, and statistical uncertainty.
* **Deliverable / Lab:**
  * **Lab 3:** Build a reproducible backtest for a rules-based strategy, with separate development and out-of-sample periods, realistic execution costs, explicit position limits, and a benchmark comparison. Report performance, drawdowns, turnover, exposure, and robustness across parameter and cost assumptions.

---

### Week 4: AI-Assisted Quantitative Research & Strategy Development (19/10 to 25/10)
* **Core Topics:**
  * Using AI to turn a market hypothesis into a precise, testable strategy specification.
  * AI-assisted data exploration, feature ideas, research-code scaffolding, and interpretation of backtest results.
  * Verification, reproducibility, and responsible use: checking generated code, avoiding fabricated data or citations, protecting sensitive information, and preventing data leakage.
* **Technical Skills:**
  * Writing effective prompts and structured instructions for quantitative research and coding tasks.
  * Using AI to generate tests, identify backtesting flaws, explain diagnostics, and document assumptions without outsourcing judgment.
  * Comparing AI-assisted implementations with a simple independently verified baseline.
* **Deliverable / Lab:**
  * **Lab 4:** Use AI to develop a candidate trading strategy from a stated hypothesis, produce a reproducible backtest specification and implementation, and critique the result for look-ahead bias, unrealistic execution, overfitting, and unsupported claims. Compare the AI-assisted strategy with a transparent baseline before considering it for the paper-trading portfolio.

---

### Week 5: Multi-Factor Models & Asset Pricing (26/10 to 1/11)
* **Core Topics:**
  * Capital Asset Pricing Model (CAPM) and idiosyncratic risk.
  * Fama-French 3-Factor (Market, SMB, HML) and 5-Factor models (RMW, CMA).
  * Statistical factor modeling: Principal Component Analysis (PCA) on cross-sectional equities.
* **Technical Skills:**
  * Multivariate Ordinary Least Squares (OLS) regressions using `statsmodels`.
  * Rolling factor beta attribution and alpha estimation ($t$-statistics and $p$-values).
  * Dimensionality reduction using `scikit-learn.decomposition.PCA`.
* **Deliverable / Lab:**
  * **Lab 5:** Download historical Fama-French factor returns. Deconstruct the performance of an actively managed fund (e.g., Berkshire Hathaway or ARKK) to isolate true manager alpha from systemic factor exposures.

---

## Phase 3: Statistical Arbitrage (Week 6)

### Week 6: Cointegration & Pairs Trading (Statistical Arbitrage) (2/11 to 8/11)
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

## Phase 4: Machine Learning, Risk Analytics & Options (Weeks 7–10)

### Week 7: Machine Learning for Return Direction & Cross-Sectional Ranking (9/11 to 15/11)
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

### Week 8: Introduction to Options & Option Pricing (16/11 to 22/11)
* **Core Topics:**
  * Call and put options, contract terms, payoff diagrams, moneyness, intrinsic value, and time value.
  * No-arbitrage pricing and the binomial option-pricing model.
  * Black-Scholes pricing, assumptions, sensitivities (the Greeks), and implied volatility.
  * Monte Carlo simulation for pricing and evaluating path-dependent options.
* **Technical Skills:**
  * Implementing binomial-tree, Black-Scholes, and Monte Carlo pricing models in Python.
  * Comparing model prices with market prices and interpreting sources of pricing error.
  * Using option-pricing outputs to evaluate hedging, risk, and strategy design assumptions.
* **Deliverable / Lab:**
  * **Lab 8:** Price a selected option using a binomial tree, Black-Scholes, and Monte Carlo simulation. Compare the results across assumptions and explain the implications for risk and trading decisions.

---

### Week 9: Option Greeks & Risk Sensitivities (23/11 to 29/11)
* **Core Topics:**
  * Delta, gamma, vega, theta, and rho as measures of option-price sensitivity.
  * How spot price, volatility, time to expiry, interest rates, and dividends affect option value and risk.
  * Delta hedging, gamma exposure, volatility exposure, and P&L attribution across changing market conditions.
* **Technical Skills:**
  * Calculating Greeks analytically and validating them with finite-difference approximations.
  * Building risk reports for single options and multi-leg positions.
  * Stress-testing Greek exposures across price, volatility, time, and interest-rate scenarios.
* **Deliverable / Lab:**
  * **Lab 9:** Calculate and visualize the Greeks for a selected option or multi-leg position, validate the results with finite differences, and simulate a delta-hedging strategy. Report hedging error, P&L attribution, and sensitivity to volatility and time decay.

---

### Week 10: Risk Management & Capstone Strategy Showcase (30/11 to 6/12)
* **Core Topics:**
  * Value at Risk (VaR): Parametric, Historical, and Monte Carlo approaches.
  * Coherent risk measures: Expected Shortfall (CVaR).
  * Portfolio stress testing, scenario analysis, and maximum leverage limits.
* **Technical Skills:**
  * Consolidating execution, factor exposures, and risk reporting into unified dashboards.
  * Generating tear-sheets using `quantstats`.
* **Deliverable / Capstone:**
  * **Lab 10:** Produce a quantitative risk report using VaR, Expected Shortfall, drawdown analysis, and stress-testing scenarios.
* **Final Showcase:** The team presents its research project and proposed trading strategy to the club for consideration in the paper-trading portfolio.
  * **Requirements:**
    1. Economic/market anomaly thesis.
    2. Factor exposure and risk decomposition.
    3. Out-of-sample backtest with transaction costs.
    4. Risk report (VaR, CVaR, drawdown duration).
    5. Execution/liquidity constraints.
    6. Explicit signal, position-sizing, rebalancing, and risk-limit rules suitable for paper trading.