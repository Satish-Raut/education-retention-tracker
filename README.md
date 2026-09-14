# Education & EdTech - Student Retention & Welfare Efficacy Tracker

## Project Overview

The **Student Retention & Welfare Efficacy Tracker** is a data analytics project focused on understanding student attendance, academic performance, mid-day meal utilization, and school infrastructure.

The project combines data from multiple education-related datasets and aims to identify patterns and factors that can help understand student welfare and retention at the school and district levels.

The project will use **Python for data cleaning and analysis** and **Power BI for interactive visualization and dashboard development**.

---

## Work Completed So Far

The following work has been completed:

### Project Setup
- Created the project repository and folder structure.
- Organized the original datasets inside the `data/raw/` directory.
- Created a Jupyter notebook for data exploration and cleaning.
- Added the required Python dependencies in `requirements.txt`.

### Initial Data Audit
- Loaded all available datasets using Python.
- Inspected dataset dimensions, columns, data types, and missing values.
- Identified data-quality issues that need to be handled during preprocessing.

### School Master Data
- Standardized column names.
- Standardized `school_id` values across the dataset.
- Removed exact duplicate records.
- Standardized text fields such as district, school type, and medium.
- **618 records → 600 records after duplicate removal.**
- **18 duplicate records removed.**

### Student Attendance Data
- Standardized column names and `school_id`.
- Handled multiple date formats and converted them into a consistent datetime format.
- Converted `total_students` and `present_students` into numeric values.
- Identified logically impossible attendance records.
- Created an `attendance_valid` flag for attendance validation.
- Calculated `attendance_rate` for valid records.
- Standardized `teacher_present` values into Boolean values.

### Attendance Validation Results

| Metric | Result |
|---|---:|
| Total attendance records | 20,800 |
| Valid attendance records | 19,965 |
| Invalid records flagged | 835 |
| Average attendance rate | 80.51% |

The invalid attendance records have been **flagged rather than deleted** so that the data-quality issues can be investigated during further analysis.

---

## Project Structure

```text
education-retention-tracker/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   └── 01_eda_and_cleaning.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt