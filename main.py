import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import seaborn as sns
import numpy as np
import os

# 1. Data Loading and Cleaning
def load_data(csv_path):
    """Load CSV data into a pandas DataFrame."""
    return pd.read_csv(csv_path)

def clean_data(df):
    """Convert columns to correct types and handle missing values."""
    df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')
    df['pollutant_min'] = pd.to_numeric(df['pollutant_min'], errors='coerce')
    df['pollutant_max'] = pd.to_numeric(df['pollutant_max'], errors='coerce')
    df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')
    df['pollutant_avg'] = df['pollutant_avg'].fillna(df['pollutant_avg'].mean())
    return df

# 2. Exploratory Data Analysis (EDA)
def basic_info(df):
    print('--- DataFrame Info ---')
    print(df.info())
    print('\n--- Head ---')
    print(df.head())
    print('\n--- Describe ---')
    print(df.describe())

def missing_data_summary(df):
    print('\n--- Missing Values by Column ---')
    print(df.isnull().sum())

def plot_pollutant_distribution(df, pollutant='PM2.5'):
    data = df[df['pollutant_id'].str.upper() == pollutant.upper()]
    if not data.empty:
        plt.figure(figsize=(8,5))
        data['pollutant_avg'].hist(bins=30, color='skyblue', edgecolor='black')
        plt.title(f'{pollutant} Distribution')
        plt.xlabel(f'{pollutant} (avg)')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    else:
        print(f'No {pollutant} data found in dataset.')

def plot_top_cities(df, pollutant='PM2.5', top_n=10):
    data = df[df['pollutant_id'].str.upper() == pollutant.upper()]
    if not data.empty and 'city' in data.columns:
        city_avg = data.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(top_n)
        print(f'\n--- Top {top_n} Cities by Average {pollutant} ---')
        print(city_avg)
        plt.figure(figsize=(10,6))
        city_avg.plot(kind='bar', color='tomato', edgecolor='black')
        plt.title(f'Top {top_n} Polluted Cities by Average {pollutant}')
        plt.xlabel('City')
        plt.ylabel(f'Average {pollutant}')
        plt.tight_layout()
        plt.show()
        city_avg.to_csv(f'top_cities_{pollutant.lower()}.csv')
        print(f'Exported top cities {pollutant} averages to top_cities_{pollutant.lower()}.csv')
    else:
        print(f'No {pollutant} or city data found in dataset.')

def plot_time_series(df, pollutant='PM2.5', city=None):
    data = df[df['pollutant_id'].str.upper() == pollutant.upper()]
    if city:
        data = data[data['city'] == city]
    if not data.empty:
        fig = px.line(data, x='last_update', y='pollutant_avg', color='city', title=f'{pollutant} Time Series')
        pio.write_html(fig, file=f'{pollutant}_timeseries.html', auto_open=False)
        print(f'Interactive {pollutant} time series plot saved as {pollutant}_timeseries.html')
    else:
        print(f'No data for pollutant {pollutant} (and city {city} if specified).')

def plot_correlation_heatmap(df):
    """Plot correlation heatmap for pollutant_avg, min, max."""
    corr = df[['pollutant_min', 'pollutant_max', 'pollutant_avg']].corr()
    plt.figure(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap (Min, Max, Avg)')
    plt.tight_layout()
    plt.show()

def detect_outliers(df, pollutant='PM2.5'):
    """Detect and print outliers for a pollutant using IQR method."""
    data = df[df['pollutant_id'].str.upper() == pollutant.upper()]
    q1 = data['pollutant_avg'].quantile(0.25)
    q3 = data['pollutant_avg'].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = data[(data['pollutant_avg'] < lower) | (data['pollutant_avg'] > upper)]
    print(f'Outliers for {pollutant} (avg):')
    print(outliers[['city', 'station', 'pollutant_avg']])
    return outliers

def export_summary(df):
    summary = df.groupby(['city', 'pollutant_id'])['pollutant_avg'].mean().reset_index()
    summary.to_csv('city_pollutant_summary.csv', index=False)
    print('Exported city-pollutant summary to city_pollutant_summary.csv')

if __name__ == '__main__':
    csv_path = 'india_air_quality_2025.csv'
    df = load_data(csv_path)
    df = clean_data(df)
    basic_info(df)
    missing_data_summary(df)
    plot_pollutant_distribution(df, pollutant='PM2.5')
    plot_top_cities(df, pollutant='PM2.5', top_n=10)
    plot_time_series(df, pollutant='PM2.5')
    plot_correlation_heatmap(df)
    detect_outliers(df, pollutant='PM2.5')
    export_summary(df)
