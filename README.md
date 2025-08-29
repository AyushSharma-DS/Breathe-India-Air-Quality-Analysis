<<<<<<< HEAD
# Breathe India: A Data-Driven Exploration of Air Quality Across Indian Cities

## Project Motivation
Air pollution is a critical issue in India, impacting millions of lives. This project aims to analyze real air quality data from Indian cities to uncover trends, identify pollution hotspots, and demonstrate data science skills in data cleaning, EDA, visualization, and reporting.

## Skills Demonstrated
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Outlier detection
- Correlation analysis
- Data visualization (matplotlib, seaborn, plotly)
- Exporting results
- Modular, well-documented code

## Dataset
- `india_air_quality_2025.csv`: Contains air quality measurements for various Indian cities, stations, and pollutants.

## Workflow
1. **Data Loading & Cleaning:**
   - Handles missing values and converts columns to correct types.
2. **Exploratory Data Analysis:**
   - Summary statistics, missing data overview, pollutant distributions.
   - City-wise average pollutant levels and top polluted cities.
   - Correlation heatmap for pollutant min/max/avg.
   - Outlier detection using IQR method.
   - Interactive time series plots for pollutant trends.
3. **Exporting Results:**
   - Top polluted cities and summary statistics exported to CSV.
   - Interactive plots saved as HTML.

## Usage
Install dependencies:
```
pip install -r requirements.txt
```

Run the main script:
```
python main.py
```

## Outputs
- Console: DataFrame info, missing data, top cities, outliers
- Plots: PM2.5 distribution, top cities bar chart, correlation heatmap, interactive time series
- Files: `top_cities_pm2.5.csv`, `city_pollutant_summary.csv`, `PM2.5_timeseries.html`

## Next Steps
- Build predictive models for air quality
- Deploy as a web dashboard
- Integrate real-time data sources

## License
MIT
=======
# Breathe-India-Air-Quality-Analysis
A data-driven exploration of air quality across Indian cities using Python, pandas, and visualization tools. Includes analysis, visualizations, and summary exports for PM2.5 and other pollutants.
>>>>>>> 5e1e929ad2cbce81d86eb3db284aca670282b40b
