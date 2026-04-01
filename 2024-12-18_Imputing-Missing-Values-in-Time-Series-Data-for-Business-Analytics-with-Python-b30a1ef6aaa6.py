# Description: Short example for Imputing Missing Values in Time Series Data for Business Analytics with Python.



# Example Time Series with Missing Values

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = [10, 12, np.nan, np.nan, 15, np.nan, 18, 20, np.nan, 22]
df = pd.Series(data, index=date_range)

# Forward Fill
df_ffill = df.ffill()

# Plot Original and Forward-Filled Data
plt.figure(figsize=(12, 6))
plt.plot(df.index, df.values, label='Original', marker='o')
plt.plot(df_ffill.index, df_ffill.values, label='Forward Fill', marker='x')
plt.legend()
plt.title("Forward Fill for Missing Values")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('forward_fill_missing_values.png')
plt.show()

# Backward Fill
df_bfill = df.bfill()

# Plot Original and Forward-Filled Data
plt.figure(figsize=(12, 6))
plt.plot(df.index, df.values, label='Original', marker='o')
plt.plot(df_bfill.index, df_bfill.values, label='Back Fill', marker='x')
plt.legend()
plt.title("Forward Fill for Missing Values")
plt.xlabel("Date")
plt.ylabel("Value")

plt.tight_layout()
plt.savefig('back_fill_missing_values.png')
plt.show()

# Forward Fill
df_mfill = df.fillna(df.mean())

# Plot Original and Forward-Filled Data
plt.figure(figsize=(12, 6))
plt.plot(df.index, df.values, label='Original', marker='o')
plt.plot(df_mfill.index, df_mfill.values, label='Mean Fill', marker='x')
plt.legend()
plt.title("Mean Fill for Missing Values")
plt.xlabel("Date")
plt.ylabel("Value")

plt.tight_layout()
plt.savefig('mean_fill_missing_values.png')
plt.show()

# Example Time Series with Missing Values
data_with_gaps = pd.DataFrame({'Value': data})
data_with_gaps['Index'] = np.arange(len(data_with_gaps))
train_data = data_with_gaps.dropna()
# Regression Model to Predict Missing Values
model = LinearRegression()
model.fit(train_data[['Index']], train_data['Value'])
# Predict Missing Values
missing_indices = data_with_gaps[data_with_gaps['Value'].isnull()]['Index']
predicted_values = model.predict(missing_indices.values.reshape(-1, 1))
# Fill Missing Values
data_with_gaps.loc[data_with_gaps['Value'].isnull(), 'Value'] = predicted_values
# Plot Results
plt.figure(figsize=(10, 5))
plt.plot(date_range, data, label='Original', marker='o')
plt.plot(date_range, data_with_gaps['Value'], label='Regression Imputed', marker='x')
plt.legend()
plt.title("Regression Fill for Missing Values")
plt.xlabel("Date")
plt.ylabel("Value")

plt.tight_layout()
plt.savefig('regression_fill_missing_values.png')
plt.show()
