import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def forward_fill() -> None:
    date_range = pd.date_range(start="2023-01-01", periods=10, freq="D")
    data = [10, 12, np.nan, np.nan, 15, np.nan, 18, 20, np.nan, 22]
    df = pd.Series(data, index=date_range)
    df_ffill = df.ffill()
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df.values, label="Original", marker="o")
    plt.plot(df_ffill.index, df_ffill.values, label="Forward Fill", marker="x")
    plt.legend()
    plt.title("Forward Fill for Missing Values")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("forward_fill_missing_values.png")
    plt.show()
    df.bfill()


def plot_original_and_forward_filled_data() -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df.values, label="Original", marker="o")
    plt.plot(df_bfill.index, df_bfill.values, label="Back Fill", marker="x")
    plt.legend()
    plt.title("Forward Fill for Missing Values")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("back_fill_missing_values.png")
    plt.show()
    df.fillna(df.mean())


def plot_original_and_forward_filled_data_2() -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df.values, label="Original", marker="o")
    plt.plot(df_mfill.index, df_mfill.values, label="Mean Fill", marker="x")
    plt.legend()
    plt.title("Mean Fill for Missing Values")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("mean_fill_missing_values.png")
    plt.show()


def example_time_series_with_missing_values() -> None:
    data_with_gaps = pd.DataFrame({"Value": data})
    data_with_gaps["Index"] = np.arange(len(data_with_gaps))
    train_data = data_with_gaps.dropna()
    model = LinearRegression()
    model.fit(train_data[["Index"]], train_data["Value"])
    missing_indices = data_with_gaps[data_with_gaps["Value"].isnull()]["Index"]
    predicted_values = model.predict(missing_indices.values.reshape(-1, 1))
    data_with_gaps.loc[data_with_gaps["Value"].isnull(), "Value"] = predicted_values


def plot_results() -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(date_range, data, label="Original", marker="o")
    plt.plot(date_range, data_with_gaps["Value"], label="Regression Imputed", marker="x")
    plt.legend()
    plt.title("Regression Fill for Missing Values")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("regression_fill_missing_values.png")
    plt.show()


def main() -> None:
    forward_fill()
    plot_original_and_forward_filled_data()
    plot_original_and_forward_filled_data_2()
    example_time_series_with_missing_values()
    plot_results()


if __name__ == "__main__":
    main()
