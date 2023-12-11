# Instagram Influencer Analysis

## Project Overview

This project focuses on analyzing Instagram influencer data to predict the 'total_likes' an influencer may receive based on various features. The end goal is to provide actionable insights that can aid in making informed decisions in the context of social media marketing.

### Objectives

- Clean and format the influencer dataset for analysis.
- Conduct exploratory data analysis (EDA) to understand the data's characteristics.
- Perform statistical tests to assess the data's distribution and compare different subsets.
- Develop predictive models to estimate an influencer's 'total_likes'.
- Interpret model results to gain business insights.

## Data Preprocessing

The data was cleaned to convert strings with suffixes 'k', 'm', and 'b' into numeric values. Missing values, particularly in the 'country' column, were handled appropriately.

## Exploratory Data Analysis (EDA)

The EDA involved:

- Summarizing data statistics.
- Visualizing distributions with histograms and box plots.
- Creating correlation matrices and pair plots to uncover relationships.

## Statistical Testing

Statistical tests conducted:

- Normality tests to check Gaussian distribution.
- T-tests to compare mean 'total_likes' between influencers from different countries.

## Predictive Modeling

Three regression models were developed and evaluated:

1. Decision Tree Regressor
2. Random Forest Regressor
3. XGBoost Regressor

The XGBoost model showed the lowest MAE, indicating the highest predictive accuracy among the three.

## Model Interpretation

Feature importance was extracted, revealing 'new_post_avg_like' as the most influential predictor for 'total_likes'.

## Business Impact

Insights from the project suggest that enhancing engagement with new posts could significantly affect an influencer's total likes. The predictive model can inform content strategy and influencer selection in marketing campaigns.

## Future Directions

Further steps to enhance the project include hyperparameter tuning, cross-validation, model explainability, and feature engineering.

## Authors

- [Satvick Malhotra]


