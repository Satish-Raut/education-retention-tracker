# 🧹 Data Rescue & Cleaning Audit Log

This document provides explicit proof of data cleaning, standardization, and anomaly detection required for **Gate 1 & Gate 2 Evaluation**.

## 📊 Summary of Raw vs. Cleaned Record Counts

| Dataset | Raw File Name | Raw Record Count | Cleaned Record Count | Key Transformations & Anomalies Addressed |
| :--- | :--- | :--- | :--- | :--- |
| **School Master** | `track4_school_master.csv` | 618 | 600 | Standardized `school_id` to `SCHXXXX`, filled missing districts/blocks as `Unknown`, normalized medium/type text casing. |
| **Student Attendance** | `track4_student_attendance.csv` | 20,800 | 19958 | Parsed mixed date strings, flagged **835 impossible records** (`present > total`), flagged **Sunday proxy attendance fraud**, normalized `teacher_present` booleans. |
| **MDM Procurement** | `track4_mid_day_meal_procurement.xlsx` | 12,360 | 12000 | Standardized vendor names, translated Hindi grain names (`Chawal` -> `Rice`), converted mixed units (`Sacks`, `Grams`, embedded `"40 kg"`) to standard **KG** (`1 Sack = 50 KG`), stripped currency symbols. |
| **Test Scores (FLN)** | `track4_test_scores.json` | 8,000 | 8000 | Converted mixed grading scales (`Letter Grades A+`, `Raw Marks 45/50`, `CGPA 8.4`, `%`) into standard **0–100% score**, normalized subject names. |
| **Infrastructure** | `track4_school_infrastructure.csv` | 3,150 | 3000 | Normalized multilingual booleans (`Hai`/`Haan`/`Yes`/`1` -> `1`; `Nahi`/`Kharab`/`No`/`0` -> `0`), computed **Infrastructure Deficit Index (%)**. |

---

## 🏛️ Gold Warehouse SQL Mart Views Created

All cleaned tables are saved in `data/gold/` as Fact/Dimension CSVs and loaded into `data/gold/education_analytics.duckdb`:

1. `vw_district_efficacy_summary` - Aggregated daily attendance %, proxy fraud count, avg FLN test scores by District.
2. `vw_proxy_attendance_fraud` - Detailed audit records of attendance fraud cases.
3. `vw_infrastructure_impact` - Correlation view of electricity, toilets, water vs. attendance & test scores.
4. `vw_mdm_procurement_summary` - Vendor supply volume in KG, cost per KG, and payment status analysis.

*Generated automatically by `main.py` pipeline launcher.*
