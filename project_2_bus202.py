"""
Authors: Luis Coronel
Description: This code will analyze the stock price over time of 3 components (AMZN, TSLA, GOOGL), 
exploring how election years affect stock prices using statistical tests and visualization.
"""
    # --- Libraries ---
import pandas as pd
import numpy as np
from plotnine import *
import pingouin as pg
from statsmodels.formula.api import ols

def main():
    # --- Load the data (adjust path as needed) ---
    df = pd.read_csv("mag7.csv")

    # --- Add a new variable 'electionYear' to identify election years ---
    df["Year"] = pd.to_datetime(df["Date"]).dt.year
    df['electionYear'] = df['Year'].isin([2016, 2020, 2024]).astype(int)

    # --- Data overview ---
    print(df)
    print(df.describe())
    print(df.dtypes)
    print(df['electionYear'].value_counts())  # Bar chart reference
    print(df['AMZN'].describe())  # Histogram reference
    print(df['TSLA'].describe())
    print(df['GOOGL'].describe())


    # --- Graphs for variables ---

    # Bar chart for electionYear
    print(
        ggplot(df, aes(x="electionYear")) +
        geom_bar(stat="count", width=0.2, fill="skyblue")
    )

    # Histograms for stock prices
    for stock in ['AMZN', 'GOOGL', 'TSLA']:
        print(
            ggplot(df, aes(x=stock)) +
            geom_histogram(bins=60, fill="skyblue", color="white")
        )


    # --- Visualization of mean stock prices between election and non-election years ---

    # Function to create comparison bar chart for each stock
    def comparison_chart(stock_name):
        mean_election = df[df['electionYear'] == 1][stock_name].mean()
        mean_non_election = df[df['electionYear'] == 0][stock_name].mean()
        comparison_df = pd.DataFrame({
            'Election Year': ['Non-Election Year', 'Election Year'],
            f'Mean {stock_name}': [mean_non_election, mean_election]
        })
        return (
            ggplot(comparison_df, aes(x='Election Year', y=f'Mean {stock_name}', fill='Election Year')) +
            geom_bar(stat='identity', width=0.6, color='black') +
            labs(x='Election Year', y=f'Mean {stock_name}')
        )


    # Run for AMZN, GOOGL, TSLA (only one needed for report)
    print(comparison_chart('TSLA'))
    print(comparison_chart('GOOGL'))
    print(comparison_chart('AMZN'))


    # --- Scatterplot and regression line between GOOGL and TSLA, colored by electionYear ---
    print(
        ggplot(df, aes(x='GOOGL', y='TSLA', color='factor(electionYear)')) +
        geom_point(size=0.7, alpha=0.8) +
        geom_smooth(method="lm", se=False)
    )


    # --- Two Sample T-Tests ---

    """
    For the Two Sample T-Test:
    Null Hypothesis: There is no difference in the mean stock price between election and non-election years.
    Alternative Hypothesis: There is a significant difference in the mean stock price between election and non-election years.
    """

    # Function to perform and print T-test result
    def perform_ttest(stock_name):
        election = df[df['electionYear'] == 1][stock_name]
        non_election = df[df['electionYear'] == 0][stock_name]
        result = pg.ttest(election, non_election, paired=False, correction=True)
        print(f"{stock_name} Election vs. Non-Election Year")
        print(result)
        print('\n\n')


    # T-tests for each stock (do only one for final report)
    perform_ttest('TSLA')
    perform_ttest('AMZN')
    perform_ttest('GOOGL')


    # --- Multiple Linear Regression ---

    """
    For the Multiple Regression:
    Null Hypothesis: There is no significant relationship between GOOGL and electionYear on TSLA stock prices.
    Alternative Hypothesis: At least one of GOOGL or electionYear significantly affects TSLA prices.
    """

    # Multiple Linear Regression: TSLA ~ GOOGL + electionYear
    model = ols("TSLA ~ GOOGL + electionYear", data=df)
    result = model.fit()
    print(result.summary())

    # Regression equation:
    """
    Equation:

    TSLA = -66.6584 + 2.3300 * GOOGL - 36.6971 * electionYear

    Predictions:

    1) GOOGL = 200, electionYear = 0 (Non-election year)
    TSLA = -66.6584 + 2.3300(200) - 36.6971(0) = 399.34

    2) GOOGL = 1500, electionYear = 1 (Election year)
    TSLA = -66.6584 + 2.3300(1500) - 36.6971(1) = 3391.65
    """

    # --- Confidence Intervals for Predictions ---

    print('Prediction 1')
    X1 = pd.DataFrame({'GOOGL': [200], 'electionYear': [0]})
    pred1 = result.get_prediction(X1)
    print(pred1.summary_frame(alpha=0.05))

    print('\n\n\nPrediction 2')
    X2 = pd.DataFrame({'GOOGL': [1500], 'electionYear': [1]})
    pred2 = result.get_prediction(X2)
    print(pred2.summary_frame(alpha=0.05))


    # --- Checking Conditions for Multiple Regression ---

    # Residuals and predictions
    df['residual'] = result.resid
    df['pred'] = result.predict(df[['GOOGL', 'electionYear']])

    # Plot residuals vs predictions
    print(
        ggplot(df, aes(x="pred", y="residual")) +
        geom_point(color="tomato", size=0.5)
    )

    # Histogram of residuals
    print(
        ggplot(df, aes(x="residual")) +
        geom_histogram(fill="skyblue", color="black", bins=10)
    )

    # Notes:
    # 1. Strong slope (check)
    # 2. Random samples (check)
    # 3. Normally distributed residuals (check)

if __name__ == "__main__":
    main()

