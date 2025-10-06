# Aliyah Trends Dashboard (2015–2023)

## Overview
This project analyzes immigration (“Aliyah”) data to Israel from 2015–2023, consolidating multiple public CSV files from the Ministry of Aliyah and Absorption into a unified, queryable dataset.
The goal is to provide a clear view of long-term migration trends, including yearly dynamics, countries of origin, and demographic distributions.
## Objectives
 - Combine and clean fragmented multi-year CSVs with inconsistent field names and mixed Hebrew/English labels.
 - Translate and normalize column headers for international readability.
 - Build a structured dataset for analytical queries and visualization in Power BI.
 - Identify demographic and temporal patterns in Aliyah trends.
## Data
**Source**: Public CSVs released by the Ministry of Aliyah and Absorption (Israel).
Coverage: 2015–2023.
Volume: ~100 000 records.
Format: UTF-8 CSV, partially in Hebrew.
## Processing Pipeline
**Data Cleaning**:
 - Unified column schemas (renamed and translated fields).
 - Removed duplicates and standardized date formats.
**SQL Integration**:
 - Loaded all yearly files into one consolidated table.
 - Validated consistency of key fields (country, gender, year, count).
**Export**:
 - Produced a single master CSV ready for further BI or ML use.
## Visualization
**Power BI** Dashboard showing:
 - Yearly Aliyah totals
 - Country-wise immigration patterns
 - Age group distributions
 - Temporal peaks and long-term trends

## Key Insights
 - Strong immigration peaks observed around specific geopolitical events.
 - Stable upward trend from selected regions.
 - Balanced age and gender ratios across most years.

## Tech Stack
- **Python** - pandas
- **SQL** 
- **Power BI** 
- **Excel**
