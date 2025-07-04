import pandas as pd
import numpy as np
import os

def load_and_clean_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, 'data', 'AirQualityUCI.xlsx')
    df = pd.read_excel(file_path)

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str),
                                     format='%Y-%m-%d %H:%M:%S')

    df.set_index('Datetime', inplace=True)

    df.drop(['Date', 'Time'], axis=1, inplace=True)

    df.replace(-200, np.nan, inplace=True)

    threshold = 0.2  # Keep columns with at least 20% non-NaN
    df = df.loc[:, df.notna().mean() >= threshold]

    df = df.fillna(df.median(numeric_only=True))  # simple imputation

    return df

if __name__ == "__main__":
    df_clean = load_and_clean_data()
    print("Cleaned dataset shape:", df_clean.shape)
    print(df_clean.head())
