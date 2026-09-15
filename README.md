# Education Retention & Welfare Efficacy Tracker

## Project Overview

This project focuses on analyzing education and student welfare data to understand
student attendance, retention-related patterns, learning outcomes, mid-day meal
utilization, and school infrastructure.

The goal is to build a data-driven dashboard that helps identify areas where
schools may require attention and support.

## Current Progress

### Data Cleaning

- School Master dataset cleaned and validated.
- Student Attendance dataset cleaned and validated.
- Attendance duplicate records removed.
- School IDs, dates, and grade values standardized.
- Teacher presence and record-marking values standardized.
- Invalid attendance records flagged instead of being removed.
- Proxy attendance anomalies identified using Sunday and 100% attendance checks.
- Missing attendance record IDs retained and flagged.
- Cleaned datasets are stored separately from the raw datasets.

### Completed Datasets

| Dataset | Status |
|---|---|
| School Master | Completed |
| Student Attendance | Completed |
| Mid-Day Meal Procurement | Completed |
| Test Scores | Pending |
| School Infrastructure | Pending |

### Attendance Cleaning Summary

| Metric | Result |
|---|---:|
| Raw records | 20,800 |
| Cleaned records | 20,000 |
| Duplicate records removed | 800 |
| Impossible attendance records flagged | 806 |
| Proxy attendance records flagged | 979 |
| Missing record IDs | 405 |

## Project Structure

```text
education-retention-tracker/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── docs/
│
├── notebooks/
│   └── 01_eda_and_cleaning.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt