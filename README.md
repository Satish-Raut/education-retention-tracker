# Education Retention & Welfare Efficacy Tracker

## Project Overview

This project focuses on analyzing education and student welfare data to understand
student attendance, retention-related patterns, learning outcomes, mid-day meal
utilization, and school infrastructure.

The goal is to build a data-driven dashboard that helps identify areas where
schools may require attention and support.

## Work Completed So Far

### Dataset 1 — School Master
- Standardized school IDs
- Removed duplicate records
- Standardized categorical fields
- Handled missing district and block values
- Validated the cleaned dataset
- Saved cleaned dataset

### Dataset 2 — Student Attendance
- Standardized school IDs
- Standardized attendance dates
- Validated student attendance values
- Identified invalid attendance records
- Calculated attendance rate
- Standardized teacher presence values
- Standardized attendance marked-by values
- Removed exact duplicate records
- Identified missing record IDs
- Flagged Sunday 100% attendance as proxy attendance anomalies
- Saved cleaned dataset

### Current Progress

- School Master: Complete
- Student Attendance: Complete
- Mid-Day Meal Procurement: In progress
- Test Scores: Pending
- School Infrastructure: Pending
- Dashboard: Pending

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