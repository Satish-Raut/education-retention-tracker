# Education & EdTech — Student Retention & Welfare Efficacy Tracker

## Project Overview

This project is being developed for the **TransOrg AgentIQ Datathon – Track 4: Education & EdTech**.

The goal is to build a data-driven system that analyzes **student attendance, academic performance, mid-day meal utilization, and school infrastructure** to identify factors affecting student retention and welfare.

The project focuses on cleaning and integrating multiple datasets and presenting the resulting insights through an interactive dashboard.

## Work Completed So Far

### Dataset 1 — School Master
- Standardized school IDs across datasets.
- Removed duplicate records.
- Standardized categorical fields such as district, school type, and medium.
- Handled missing district and block values using `Unknown`.
- Validated duplicate school IDs and missing values.
- Saved the cleaned dataset as:
  `data/cleaned/school_master_cleaned.csv`

### Dataset 2 — Student Attendance
- Standardized school IDs.
- Standardized and validated date values.
- Converted attendance-related numeric fields to appropriate numeric types.
- Identified invalid attendance records where present students exceeded total students.
- Calculated attendance rate for valid records.
- Standardized teacher presence values.
- Standardized attendance records marked by different roles.
- Removed exact duplicate records.
- Flagged missing record IDs.
- Saved the cleaned dataset as:
  `data/cleaned/student_attendance_cleaned.csv`

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