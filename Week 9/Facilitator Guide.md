# Week 9 · Option Greeks & Risk Sensitivities

**60 minutes · 35 minutes of finance, 20 minutes of Python, 5 minutes of discussion**

**How can a call lose value when its stock goes up, and what would a delta hedge have changed?**

Bring the Week 8 example forward. The European call has spot \$100, strike \$95, three months to expiry, a 10% annual rate, 50% annual volatility, and zero dividends. Its Black–Scholes value is \$13.6953 per share. Keep that example on the board throughout. Open the [Week 9 notebook](Week_9_Option_Greeks_and_Risk_Sensitivities.ipynb) before class. Prices and P&L below are per share unless a contract multiplier is stated. [Week 8 class notebook](https://github.com/novaquantclub/quant-roadmap/blob/main/Week%208/Week_8_Options_Final_Executed.ipynb) · [Week 9 roadmap](https://github.com/novaquantclub/quant-roadmap#week-9-option-greeks--risk-sensitivities-2311-to-2911)

By the end, members should be able to read a Greek with its units, size a stock hedge, and explain the main drivers of an option's P&L under a scenario.

## Run of show

| Minutes | Teach or do | Question for the room |
|---|---|---|
| 0–5 | Return to the one-step binomial replication from Week 8. If the stock ends at \$120 or \$80, the \$95 call pays \$25 or \$0. Subtract the two replication equations to get the hedge ratio, $25 / 40 = 0.625$. In Black–Scholes, delta is the local slope of the value curve. | Why does the bond holding drop out when we subtract? |
| 5–14 | Sketch the call value against spot and draw its tangent at \$100. Compare a long call's positive delta with a long put's negative delta. Introduce gamma as the change in delta per \$1 move. Use the \$1 bump to estimate the new call delta, then size the stock hedge. Discuss why a near-expiry option near the strike can require frequent rebalancing. | If the stock rises after we hedge a long call, should we buy or sell shares to restore neutrality? |
| 14–24 | Teach vega, theta and rho by changing one input at a time. Emphasize implied volatility, percentage points, and calendar-day decay. Cover rate and dividend direction for European calls and puts using the discounted strike and the stock's expected dividend yield. | If IV falls from 50% to 45%, what number multiplies a vega quoted per volatility point? |
| 24–35 | Give pairs the scenario below. Have them predict the sign, attribute the move on paper, then add the P&L from the initial stock hedge. Use the last few minutes to discuss gamma, vega, and time decay that remain after hedging delta. | Which exposure dominates when the stock goes up \$1 and the call loses value? |
| 35–41 | Open the notebook and run the setup. Build the central-difference delta on screen by pricing at spot \$100.10 and \$99.90, then dividing the price difference by \$0.20. Compare the analytical and finite-difference columns. | What stays fixed when we bump spot? |
| 41–47 | Use the top row of the Greek plots. Compare one week with three months and look for the sharp change near the strike. Try spot shocks of \$1 and \$15 and compare delta-only, delta–gamma, and full repricing. | Where will a fixed delta go stale fastest? |
| 47–55 | Run the same scenario the pairs worked on. Reconcile the estimated P&L with full repricing and check how the initial hedge changes the result. Show the new option delta and ask for the next hedge trade. | What does the residual tell you about using today's Greeks for tomorrow's book? |
| 55–60 | Exit ticket and introduce Lab 9. | How can a delta-neutral position lose money tomorrow? Name a remaining risk and give its direction for this call. |

## Board reference

| Greek | Read it aloud | Week 8 call |
|---|---|---:|
| Delta | Estimated premium change for a \$1 rise in spot. Also stock-equivalent shares per option share. | +0.6665 |
| Gamma | Estimated change in delta for a \$1 rise in spot. | +0.01455 |
| Vega | Estimated premium change for a one-percentage-point rise in implied volatility. | +\$0.1818 |
| Theta | Estimated premium change for one calendar day passing, with other inputs fixed. | −\$0.0643 |
| Rho | Estimated premium change for a one-percentage-point rise in the annual rate. | +\$0.1324 |

For long European vanilla options in this model, calls have positive delta and rho and puts have negative delta and rho. Both have positive gamma and vega. Theta is commonly negative and can be positive, for example for some deep in-the-money European puts. A higher continuous dividend yield lowers the call price and raises the put price, holding the other inputs fixed. A short position flips the signs of its exposures. [Options Industry Council guide to the Greeks](https://prd-web.optionseducation.org/advancedconcepts/understanding-options-greeks)

If your long call represents 100 shares, its position delta is about +66.65 shares. Short about 66.65 shares in the frictionless example. With a spot-only rise of \$1, the call's delta rises to about 0.681 per share, so short roughly 1.45 more shares per contract to rebalance, using gamma as an estimate. A stock position supplies delta, so the gamma, vega, theta, and rho of the option are still present.

## Pair exercise and answer key

**Prompt.** Tomorrow the stock is \$101, IV is 45%, and the rate and dividend assumptions are unchanged. Estimate the long call's P&L. Then add the one-day P&L of the stock position from the initial delta hedge. Ask pairs to write the units beside each input before using the numbers.

| Driver | Calculation | P&L per share |
|---|---|---:|
| Delta | $0.666465 \times 1$ | +0.6665 |
| Gamma | $\tfrac12 \times 0.014547 \times 1^2$ | +0.0073 |
| Vega | $0.181843 \times (-5)$ | −0.9092 |
| Theta | $-0.064327 \times 1$ | −0.0643 |
| Rho | $0.132378 \times 0$ | 0.0000 |
| **Estimated option P&L** | Sum of the terms | **−0.2998** |
| **Full Black–Scholes repricing** | $V_{\text{new}}-V_{\text{old}}$ | **−0.2825** |

The short stock position loses another \$0.6665 per option share. The combined option and stock P&L is **−\$0.9490** before cash interest and trading costs. The drop in implied volatility more than offsets the gain from higher spot. The option's new delta is about 0.6901. For a 100-share contract, short roughly 2.36 more shares after this combined shock. The \$0.0173 difference between full repricing and the Greek estimate includes changes in sensitivities and interactions among the shocks. [CME Group worked example of Greek attribution](https://www.cmegroup.com/education/courses/option-greeks/options-the-greeks-options-premium-and-the-greeks)

**Exit ticket answer.** A drop in implied volatility hurts a long call through positive vega. A quiet day can also produce a loss through theta. Gamma means the stock exposure changes as spot moves, so delta neutrality is measured at the hedge time.

## Lab 9

The notebook continues with a single-call and long-straddle risk report, full repricing under isolated and combined shocks, and a seeded simulation of a self-financing delta hedge. Ask members to submit one concise risk report with:

1. A position Greek table and the sensitivity charts. Compare analytical and bump-and-reprice values and state the reporting units.
2. One combined scenario with Greek contributions, full-repricing P&L, and the unexplained residual. Use the isolated volatility and one-day aging shocks to explain vega and theta.
3. Terminal hedging-error mean and RMSE for three rebalancing schedules. Explain what changes when the stock's simulated volatility differs from the volatility the hedger uses and what the frictionless setup assumes.
