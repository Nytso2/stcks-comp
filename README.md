# Statistical Analysis of Big Tech Stock Prices During U.S. Presidential Elections

## 📊 Project Overview

This project analyzes the stock price fluctuations of **Amazon, Tesla, and Google** and investigates whether **U.S. presidential elections** have a significant impact on their prices. Given the influence of big tech on the market, understanding how political events affect stock valuations is essential for investors.
```bash
note that all the graphs are displayed by the python.
```
## ❓ Research Question

**Do U.S. presidential elections significantly affect the stock prices of Amazon, Tesla, and Google?**

## 📂 Data Source

Dataset from **Kaggle** containing 10 years of daily stock prices for the "Magnificent 7" tech companies.  
🔗 [Magnificent 7 Stock Prices (Kaggle)](https://www.kaggle.com/datasets/unmoved/magnificent-7-past-10-years-prices-updated-daily)

## ⚙️ Methodology

1. **Descriptive Statistics & Visualization**  
   - Summary stats (mean, std, min, max) for Amazon, Tesla, Google.  
   - Election vs. non-election year frequency.  
   - Group mean visualizations.

2. **Statistical Tests**  
   - **Two-Sample T-Tests**: Compare stock prices during election vs. non-election years.  
   - **Multiple Regression**: Predict Tesla price using Google price and election year indicator.

3. **Assumption Verification**  
   - Linearity, independence, equal variance, normality for regression.  
   - Independence and normality for T-tests.

## 📈 Key Results

### Descriptive Statistics

| Stock  | Count | Mean  | Std Dev | Min  | 25%  | Median | 75%  | Max  |
|-------|------|------|------|------|------|------|------|------|
| Amazon | 2513 | 98.99 | 53.38 | 14.35 | 47.68 | 93.76 | 152.05 | 214.10 |
| Tesla | 2513 | 111.41 | 110.56 | 9.58 | 16.97 | 24.72 | 217.61 | 409.97 |
| Google | 2513 | 80.99 | 42.77 | 24.85 | 46.84 | 62.94 | 117.68 | 191.18 |

### Two-Sample T-Test Results

| Company | p-value | Conclusion |
|------|---------|------------|
| Tesla | 0.0036 | Significant difference in stock prices. |
| Amazon | 1.51e-15 | Significant difference in stock prices. |
| Google | 0.000001 | Significant difference in stock prices. |

> ✅ **Conclusion**: Stock prices differ significantly during election years.

### Multiple Regression

TSLA = -66.6584 + 2.3300 * GOOGL - 36.6971 * ElectionYear R-squared: 0.805 (80.5% variance explained)

### Confidence Intervals for Predictions

| Scenario | Predicted TSLA | 95% CI |
|------|------|------|
| Google = 200, Non-Election Year | 399.34 | [393.41, 405.27] |
| Google = 1500, Election Year | 3391.65 | [3328.09, 3455.13] |

## ✅ Conclusions

- **Presidential elections** significantly affect stock prices of Amazon, Tesla, and Google.
- Tesla prices influenced by Google stock and election year.
- Investors should consider these factors during election cycles.

## ⚠️ Limitations

- Data limited to **last 10 years** — recent tech trends dominate.
- **Confounding factors**: COVID-19, quarterly earnings may affect outcomes.

## 📚 References

- [Yahoo! Finance](https://finance.yahoo.com/)
- [U.S. Bank](https://www.usbank.com/investing/financial-perspectives/market-news/how-presidential-elections-affect-the-stock-market.html)
- [Investopedia](https://www.investopedia.com/magnificent-seven-stocks-8402262)

## 💻 Code

Python analysis notebook:  
🔗 [Colab Notebook](https://colab.research.google.com/drive/17JlJmPyg_qfXuSGe7uhiYp5FRR2QqJm-?usp=sharing)

### ✅ Requirements if running locally:
