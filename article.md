# Imputing Missing Values in Time Series Data for Business Analytics with Python Real world data is messy. Unlike the pristine data we use from Kaggle or
classroom examples, real time series data has missing values...

### Imputing Missing Values in Time Series Data for Business Analytics with Python
Real world data is messy. Unlike the pristine data we use from Kaggle or
classroom examples, real time series data has missing values caused by
sensor malfunctions, data transmission errors, or inconsistent reporting
intervals.


<figcaption>Photo by <a
class="markup--anchor markup--figure-anchor"
rel="photo-creator noopener" target="_blank">Damien TUPINIER</a> on <a
class="markup--anchor markup--figure-anchor"


Time series models assume the data is complete --- so you can end up
with wrong results if you proceed with using a model but the data is
incomplete.

This article explores four techniques for imputing (creating) missing
values--- forward fill, backward fill, mean fill, and regression-based
imputation --- and discusses the risks of using imputed data in
modeling.

#### Why Missing Values Matter in Time Series
Missing values disrupt the continuity and temporal structure of time
series data, which can lead to biased analysis because the model assumes
that the "step" from one observation to the next is constant. Having
missing values will mess up the calculations for trends, seasonality, or
autocorrelations.

In regular analytics, we often drop incomplete observations (rows with
missing values). When you have a lot of independent, identically
distributed (iid) data then dropping some rows does not fundamentally
alter the analysis. But in time series, dropping some rows means we have
changed the "step" between data points.

Common time series models (e.g., ARIMA, LSTM) don't have methods to team
with missing values during training so passing in a dataset with "NaN"
(not a number) values will cause errors in training.

The goal of imputation is to fill in missing values in a way that
preserves the underlying patterns of the time series. But we have to be
careful when using imputed data because the method we use for imputation
necessarily introduces assumptions (read uncertainty) into the model.

#### Common Imputation Techniques
**Forward Fill** replaces missing values with the most recent available
value. It assumes that the last observed value is a good approximation
for the missing point.

Python Example: Forward Fill



Forward fill is simple and quick to implement. It preserves trends and
does not introduce sudden changes. However, it can also propagate
(meaning continue) outdated values if missing intervals are large.
Forward will is not a good method for a time series with rapid changes
between values.

**Backward Fill** replaces missing values with the next observed value.
It assumes future observations approximate the missing point.

Python Example: Backward Fill



Backfill is also simple to use and effective when the series quickly
stabilizes. It can introduce "future leakage" if used improperly in
predictive models and it assumes that the next observations is a
reliable approximation for the previous value (basically the opposite of
what we are trying to do with time series forecasting).

**Mean Fill** replaces missing values with the mean of the available
data.

Python Example: Mean Fill



This is a hybrid between forward fill and back fill. It is also simple
and fast to compute and works well for stationary series without strong
trends. Because it uses the mean, it smooths out variations which makes
it harder to identify temporal patterns. It also assumes data is
stationary and the mean is stable.

**Regression-Based Imputation** predicts missing values based on
relationships with other variables or past observations. It is a more
sophisticated method that can account for trends and patterns.

Python Example: Regression Imputation



This method is often the most accurate because it uses temporal
relationships to provide more accurate predictive values (imputations).
Regression accounts for trends and correlations with other variables
which is especially useful when you have multivariabte data available.
Linear regression assumption the misisng values have a linear
relationship with the other varibakes you are using, which may not
always be the case. This method is computationally more complex than the
other techniques discussed here and can be harder to "undo" if you end
up getting updated info about the values.

#### Dangers of Imputed Data in Modeling
While imputation solves the problem of missing data, it introduces
assumptions that can impact model performance. Imputation methods like
mean fill reduce variability and smooth out anomalies, which can bias
results. Complex imputation methods, such as regression, can introduce
noise or model assumptions that lead to overfitting. We need to remember
that imputed values aren't observed so treating them as "real" values
brings in additional uncertainty. Using methods like backward fill can
leak future information into training data, basically doing part of the
work that we expect from our predictive models.

Example of Modeling Caution:

- **Forward/Backward Fill** works well for short-term gaps but can fail
  for larger missing intervals.
- **Mean Fill** ignores temporal structure, which may mislead models
  dependent on trends or seasonality.
- **Regression Imputation** assumes that relationships remain stable
  over time, which may not always hold true.

There are best practices to mitigate the problems with imputating time
series values. Always mark imputed values in a separate column to track
where imputation occurred. Test models with and without imputed data to
evaluate the impact of imputation. Consider models that handle missing
values naturally, such as neural network models.

#### Next Steps
Imputing missing values is often necessary for time series analysis, but
it comes with risks. Forward fill, backward fill, mean fill, and
regression-based imputation have strengths and weaknesses depending on
the context and structure of the data.

Part of your value as an analyst is picking the best technique to ensure
that imputations do not introduce bias, distort patterns, or leak future
information into models.

#### Related Posts
This article is part of a series of posts on time series forecasting.
Here is the list of articles in the order they were designed to be read.

1.  [[Time Series for Business Analytics with
    Python](https://medium.com/@kylejones_47003/time-series-for-business-analytics-with-python-a92b30eecf62?source=your_stories_page-------------------------------------)]
2.  [[Time Series Visualization for Business Analysis with
    Python](https://medium.com/@kylejones_47003/time-series-visualization-for-business-analysis-with-python-5df695543d4a?source=your_stories_page-------------------------------------)]
3.  [[Patterns in Time Series for
    Forecasting](https://medium.com/@kylejones_47003/patterns-in-time-series-for-forecasting-8a0d3ad3b7f5?source=your_stories_page-------------------------------------)]
4.  [[Imputing Missing Values in Time Series Data for Business Analytics
    with
    Python](https://medium.com/@kylejones_47003/imputing-missing-values-in-time-series-data-for-business-analytics-with-python-b30a1ef6aaa6?source=your_stories_page-------------------------------------)]
5.  [[Measuring Error in Time Series Forecasting with
    Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
6.  [[Univariate and Multivariate Time Series Analysis with
    Python](https://medium.com/@kylejones_47003/univariate-and-multivariate-time-series-analysis-with-python-b22c6ec8f133?source=your_stories_page-------------------------------------)]
7.  [[Feature Engineering for Time Series Forecasting in
    Python](https://medium.com/@kylejones_47003/feature-engineering-for-time-series-forecasting-in-python-7c469f69e260?source=your_stories_page-------------------------------------)]
8.  [[Anomaly Detection in Time Series Data with
    Python](https://medium.com/@kylejones_47003/anomaly-detection-in-time-series-data-with-python-5a15089636db?source=your_stories_page-------------------------------------)]
9.  [[Dickey-Fuller Test for Stationarity in Time Series with
    Python](https://medium.com/@kylejones_47003/dickey-fuller-test-for-stationarity-in-time-series-with-python-4e4bf1953eed?source=your_stories_page-------------------------------------)]
10. [[Using Classification Model for Time Series Forecasting with
    Python](https://medium.com/@kylejones_47003/using-classification-model-for-time-series-forecasting-with-python-d74a1021a5c4?source=your_stories_page-------------------------------------)]
11. [[Measuring Error in Time Series Forecasting with
    Python](https://medium.com/@kylejones_47003/measuring-error-in-time-series-forecasting-with-python-18d743a535fd?source=your_stories_page-------------------------------------)]
12. [[Physics-informed anomaly detection in a wind turbine using Python
    with an autoencoder
    transformer](https://medium.com/@kylejones_47003/physics-informed-anomaly-detection-in-a-wind-turbine-using-python-with-an-autoencoder-transformer-06eb68aeb0e8?source=your_stories_page-------------------------------------)]
