# -*- coding: utf-8 -*-
"""Project 2 BUS202

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17JlJmPyg_qfXuSGe7uhiYp5FRR2QqJm-
"""

"""
Authors :  Luis Coronel

"""

import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

# loading the data (Change directory for each person if needed )
df = pd.read_csv("/content/drive/My Drive/BUS202/DATA/mag7.csv")

df # add a presidential year as 1 , rest as 0 bar chart of mean of the presitial year between

#add new var called electionyear that will add an automatic 1 if the year is 2016,2020,2024 and
#everything else will have a 0 so that we can compare how the stock price is affected
#during theyears that there is eleciton and the
#ones that don't have election dates.


yearsElected = ['2016','2020','2024']
df["Year"] = pd.to_datetime(df["Date"]).dt.year
df['electionYear'] = df['Year'].isin([2016,2020,2024]).astype(int)

df

df.describe()

df.dtypes

df['electionYear'].value_counts() # bar chart

df['AMZN'].describe() # histogram

df['TSLA'].describe()

df['GOOGL'].describe()

#Graphs for varaibles
from plotnine import *
(
ggplot(df, aes(x = "electionYear")) +
  geom_bar(stat = "count", width = 0.2, fill = "skyblue")
)

(
ggplot(df, aes(x = "AMZN")) +
  geom_histogram(bins = 60, # number of bars
                 fill = "skyblue", # color
                 color = "white") # outline color
)

(
ggplot(df, aes(x = "GOOGL")) +
  geom_histogram(bins = 60, # number of bars
                 fill = "skyblue", # color
                 color = "white") # outline color
)

(
ggplot(df, aes(x = "TSLA")) +
  geom_histogram(bins = 60, # number of bars
                 fill = "skyblue", # color
                 color = "white") # outline color

)

# 4)   visualize the relationships between variables that you want to examine in your
# models (e.g., a bar chart of group means, comparison bar chart, scatterplot, etc.)

#two sample t test comparison chart for TSLA , only need 1


mean_tsla_election = df[df['electionYear'] == 1]['TSLA'].mean()
mean_tsla_non_election = df[df['electionYear'] == 0]['TSLA'].mean()

comparison_df =  pd.DataFrame({
    'Election Year': ['Non-Election Year', 'Election Year'],
    'Mean TSLA': [mean_tsla_non_election, mean_tsla_election]
})

(
    ggplot(comparison_df, aes(x='Election Year', y='Mean TSLA', fill='Election Year')) +
    geom_bar(stat='identity', width=0.6, color='black') +
    labs(
        x='Election Year',
        y='Mean TSLA'
    )
)

# 4)   visualize the relationships between variables that you want to examine in your
# models (e.g., a bar chart of group means, comparison bar chart, scatterplot, etc.)

#two sample t test comparison chart for GOOGL , only need 1


mean_GOOGL_election = df[df['electionYear'] == 1]['GOOGL'].mean()
mean_GOOGL_non_election = df[df['electionYear'] == 0]['GOOGL'].mean()

comparison_df =  pd.DataFrame({
    'Election Year': ['Non-Election Year', 'Election Year'],
    'Mean GOOGL': [mean_GOOGL_non_election, mean_GOOGL_election]
})

(
    ggplot(comparison_df, aes(x='Election Year', y='Mean GOOGL', fill='Election Year')) +
    geom_bar(stat='identity', width=0.6, color='black') +
    labs(
        x='Election Year',
        y='Mean GOOGL'
    )
)

# 4)   visualize the relationships between variables that you want to examine in your
# models (e.g., a bar chart of group means, comparison bar chart, scatterplot, etc.)

#two sample t test comparison chart for AMZN , only need 1


mean_AMZN_election = df[df['electionYear'] == 1]['AMZN'].mean()
mean_AMZN_non_election = df[df['electionYear'] == 0]['AMZN'].mean()

comparison_df =  pd.DataFrame({
    'Election Year': ['Non-Election Year', 'Election Year'],
    'Mean AMZN': [mean_AMZN_non_election, mean_AMZN_election]
})

(
    ggplot(comparison_df, aes(x='Election Year', y='Mean AMZN', fill='Election Year')) +
    geom_bar(stat='identity', width=0.6, color='black') +
    labs(
        x='Election Year',
        y='Mean AMZN'
    )
)

#multiple regression : scatterplot

#found keyword factor on plotnine documentation to plotnine https://plotnine.org/

(
ggplot(df, aes(x = 'GOOGL', y = 'TSLA', color = 'factor(electionYear)')) +
  geom_point(size = 0.7, alpha = 0.8) +
  geom_smooth(method = "lm", se = False)
)


# currently working on this gimme 2 hours ill upload this charts to the docs

!pip install pingouin

"""
For the Two Sample T-Test
Null Hypothesis: There is no difference in the mean stock price between election and non election years.
Alternative Hypothesis: There is a significant difference in the mean stock price between election and non election years.

"""

import pingouin as pg

# Split data into election years and non-election years
TSLA_election = df[df['electionYear'] == 1]['TSLA']
TSLA_non_election = df[df['electionYear'] == 0]['TSLA']

# Perform a two-sample t-test for TSLA
result = pg.ttest(TSLA_election, TSLA_non_election, paired=False, correction=True)
print("TSLA Election vs. Non-Election Year\n")
print(result)
print('\n\n')

AMZN_election = df[df['electionYear'] == 1]['AMZN']
AMZN_non_election = df[df['electionYear'] == 0]['AMZN']

# Perform a two-sample t-test for AMZN
result2 = pg.ttest(AMZN_election, AMZN_non_election, paired=False, correction=True)
print("AMZN Election vs. Non-Election Year")
print(result2)
print('\n\n')
GOOGL_election = df[df['electionYear'] == 1]['GOOGL']
GOOGL_non_election = df[df['electionYear'] == 0]['GOOGL']

# Perform a two-sample t-test for GOOGL
result3 = pg.ttest(GOOGL_election, GOOGL_non_election, paired=False, correction=True)
print("GOOGL Election vs. Non-Election Year")
print(result3)


# for this part , i did all 3 but when writing in the docs you actually just need to do 1 if im not mistaken

"""
For the Multiple regression
Null Hypothesis : There is no significant relationship between google and election year and TSLA stock prices
which means that the coefficients for Google and electionyear are 0

Alternative Hypothesis : one of the {google or electionyear} has a significant relation with TSLA prices,
meaning that the coeffieicents for google or electionyear are not 0.

"""

from statsmodels.formula.api import ols
import statsmodels.api as sm

#Multiple Linear Regresion between Google , election year to predict TSLA
model = ols("TSLA ~ GOOGL + electionYear", data=df)
result = model.fit()
print(result.summary())

#Regresion result
"""
equation:

TSLA = -66.6584 + 2.3300 * GOOGL -36.6971 * electionYear

2 predictions

1)  Google = 200 , electionyear = 0 (non election year)
    TSLA =  -66.6584 + 2.3300(200) -36.6971(0)
    TSLA = 399.34


2)
    Google = 1500, electionyear = 1 (election year)
    TSLA = -66.6584 + 2.3300(1500) -36.6971(1)
    TSLA = 3391.65

"""

#Confidence intervals for predictions for prediction 1
print('Prediction 1')
X = pd.DataFrame(zip([200],[0]), columns=['GOOGL','electionYear'])
pred = result.get_prediction(X)
print(pred.summary_frame(alpha=0.05))
#Confidence intervals for predictions for prediction 2

print('\n\n\n')
print('Prediction 2')
X = pd.DataFrame(zip([1500],[1]), columns=['GOOGL','electionYear'])
pred2 = result.get_prediction(X)
print(pred2.summary_frame(alpha=0.05))

#Checking conditions for Multiple regression :


# 1. there is a strong slope (check)
# 2. they are random samples (check)
# 3 calc residuals

df['residual'] = result.resid

## Make predictions with the data
df['pred'] = result.predict(df[['GOOGL','electionYear']])

## Plot residuals along with the predictions
(
ggplot(df, aes(x = "pred", y = "residual")) +
  geom_point(color = "tomato", size = 0.5)
)

(
ggplot(df, aes(x = "residual")) +
  geom_histogram(fill = "skyblue", color = "black", bins = 10)
)

#normally distributed (check)