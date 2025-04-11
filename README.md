# Political Insights: Interactive Data Visualization for Students

An interactive data visualization platform designed to make political data more accessible and interpretable for students. This project transforms complex political datasets into easy-to-understand visualizations, with a focus on USA, UK, and global political data.

## Project Overview

This platform is to address a common challenge: political data is often stored in formats that are difficult to interpret, such as regression tables or complex Excel files. This tool makes finding and analyzing data for essays and research much more efficient.

### Key Features:
- Interactive correlation graphs with real-time data
- Easy-to-interpret visualizations
- Customizable data analysis tools
- Beginner-friendly descriptions for students without quantitative backgrounds
- Multi-regional coverage (USA, UK, and global data)

## Getting Started

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebooks in order to generate necessary datasets
4. Launch the web interface:
   ```bash
   streamlit run webstream.py
   ```

## Project Structure

```
.
├── docs/
│   └── Notebooks/          # Analysis notebooks
├── Data/                   # Generated datasets
├── requirements.txt        # Project dependencies
└── webstream.py           # Streamlit web application
```

## Data Processing

The project uses a series of Jupyter notebooks to process and prepare data:
1. Run notebooks in sequential order
2. Each notebook generates CSV files in the Data folder
3. Final notebook creates the database for the website
4. Launch the Streamlit interface to interact with the processed data

## Data Sources

This project aggregates data from various reliable sources including:
- US State and Territory Statistics
- Poverty and Income Statistics (HHS)
- UK Electoral Data
- Global Population Projections
- Inflation Data
- Historical Protest Data
- Electoral Calculations and Predictions

## Usage

The platform is designed to help students:
- Find relevant political data quickly
- Create custom visualizations for essays and research
- Understand complex political trends through interactive graphs
- Compare variables across different political datasets
- Generate insights without requiring advanced quantitative skills

## Sources

- [US States and Territories Area Data](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area)
- [HHS Poverty Statistics](https://aspe.hhs.gov/information-poverty-income-statistics-tables)
- [UK General Election Turnout Data](https://www.theguardian.com/news/datablog/2010/may/06/general-election-2010-turnout-since-1945)
- [UK Protests Database](https://en.wikipedia.org/wiki/List_of_protests_in_the_United_Kingdom)
- [Electoral Predictions](https://www.electoralcalculus.co.uk/prediction_main.html)
- [World Population Projections](https://www.ined.fr/en/everything_about_population/data/world-projections/projections-by-countries/)
- [US Inflation Data](https://www.usinflationcalculator.com/inflation/current-inflation-ra)
