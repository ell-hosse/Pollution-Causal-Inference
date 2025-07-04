import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_and_clean import load_and_clean_data
import os


def save_figure(fig, filename):
    """Save figure to the outputs/figures directory."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(base_dir, 'outputs', 'figures', filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)


def plot_time_series(df, pollutants):
    """Plot time series for selected pollutants."""
    for pollutant in pollutants:
        if pollutant in df.columns and pd.api.types.is_numeric_dtype(df[pollutant]):
            if df[pollutant].dropna().shape[0] > 0:
                plt.figure(figsize=(12, 4))
                df[pollutant].plot()
                plt.title(f'Time Series of {pollutant}')
                plt.ylabel(pollutant)
                plt.xlabel('Datetime')
                plt.tight_layout()
                safe_name = pollutant.replace("(", "").replace(")", "")
                save_figure(plt.gcf(), f'{safe_name}_timeseries.png')
                plt.close()
            else:
                print(f"Skipped {pollutant} — all data missing.")
        else:
            print(f"Skipped {pollutant} — not numeric or missing.")


def plot_distributions(df, pollutants):
    """Plot distribution (histogram) for selected pollutants."""
    for pollutant in pollutants:
        if pollutant in df.columns and pd.api.types.is_numeric_dtype(df[pollutant]):
            if df[pollutant].dropna().shape[0] > 0:
                plt.figure(figsize=(6, 4))
                sns.histplot(df[pollutant], kde=True, bins=40)
                plt.title(f'Distribution of {pollutant}')
                plt.tight_layout()
                safe_name = pollutant.replace("(", "").replace(")", "")
                save_figure(plt.gcf(), f'{safe_name}_distribution.png')
                plt.close()
            else:
                print(f"Skipped {pollutant} — all data missing.")
        else:
            print(f"Skipped {pollutant} — not numeric or missing.")


def plot_correlation_matrix(df):
    """Plot a heatmap of the correlation matrix for numeric columns."""
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.shape[1] > 1:
        corr_matrix = numeric_df.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.tight_layout()
        save_figure(plt.gcf(), 'correlation_matrix.png')
        plt.close()
    else:
        print("Not enough numeric data for correlation matrix.")


def run_exploratory_analysis():
    df = load_and_clean_data()
    pollutants = ['CO(GT)', 'C6H6(GT)', 'NOx(GT)', 'NO2(GT)']

    plot_time_series(df, pollutants)
    plot_distributions(df, pollutants)
    plot_correlation_matrix(df)

    print("Exploratory analysis completed. Figures saved to outputs/figures/.")


if __name__ == "__main__":
    run_exploratory_analysis()
