import duckdb
import pandas as pd
from pathlib import Path

def build_gold_warehouse(silver_dir: str | Path, gold_dir: str | Path) -> str:
    """
    Reads Silver cleaned datasets, constructs Gold Star Schema tables,
    and builds SQL Analytical Mart Views inside a DuckDB database (`education_analytics.duckdb`).
    """
    silver_dir = Path(silver_dir)
    gold_dir = Path(gold_dir)
    gold_dir.mkdir(parents=True, exist_ok=True)

    db_path = gold_dir / "education_analytics.duckdb"
    conn = duckdb.connect(str(db_path))

    print(f"[Warehouse Builder] Connecting to Gold DuckDB at {db_path}...")

    # Load Silver CSVs into DuckDB Tables & save Gold Fact/Dim CSVs
    file_table_map = {
        "clean_school_master.csv": ("dim_school", "dim_school.csv"),
        "clean_student_attendance.csv": ("fact_attendance", "fact_attendance.csv"),
        "clean_mid_day_meal.csv": ("fact_mdm_procurement", "fact_mdm_procurement.csv"),
        "clean_test_scores.csv": ("fact_test_scores", "fact_test_scores.csv"),
        "clean_school_infrastructure.csv": ("fact_infrastructure", "fact_infrastructure.csv"),
    }

    for silver_name, (table_name, gold_csv_name) in file_table_map.items():
        silver_file = silver_dir / silver_name
        if silver_file.exists():
            df = pd.read_csv(silver_file)
            
            # Save Gold CSV for Power BI / easy access
            gold_csv_file = gold_dir / gold_csv_name
            df.to_csv(gold_csv_file, index=False)
            
            # Register in DuckDB
            conn.register(f"temp_{table_name}", df)
            conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM temp_{table_name}")
            print(f" -> Created Gold Table: {table_name} ({len(df)} rows)")

    # =========================================================================
    # CREATE GOLD SQL ANALYTICAL MARTS & VIEWS FOR DASHBOARD & AI AGENT
    # =========================================================================

    # 1. District Efficacy Summary View
    conn.execute("""
    CREATE OR REPLACE VIEW vw_district_efficacy_summary AS
    SELECT 
        s.district,
        COUNT(DISTINCT s.school_id) AS total_schools,
        SUM(s.total_enrolled_students) AS total_enrolled_students,
        ROUND(AVG(a.attendance_rate_pct), 2) AS avg_attendance_rate_pct,
        SUM(CASE WHEN a.is_proxy_fraud THEN 1 ELSE 0 END) AS total_proxy_fraud_cases,
        ROUND(AVG(t.normalized_score_pct), 2) AS avg_test_score_pct,
        ROUND(AVG(i.infrastructure_deficit_pct), 2) AS avg_infrastructure_deficit_pct
    FROM dim_school s
    LEFT JOIN fact_attendance a ON s.school_id = a.school_id
    LEFT JOIN fact_test_scores t ON s.school_id = t.school_id
    LEFT JOIN fact_infrastructure i ON s.school_id = i.school_id
    GROUP BY s.district
    ORDER BY avg_attendance_rate_pct DESC;
    """)
    print(" -> Created SQL View: vw_district_efficacy_summary")

    # 2. Proxy Attendance Fraud View
    conn.execute("""
    CREATE OR REPLACE VIEW vw_proxy_attendance_fraud AS
    SELECT 
        a.record_id,
        a.date,
        a.school_id,
        s.school_name,
        s.district,
        a.grade,
        a.total_students,
        a.present_students,
        a.attendance_rate_pct,
        a.day_of_week
    FROM fact_attendance a
    JOIN dim_school s ON a.school_id = s.school_id
    WHERE a.is_proxy_fraud = TRUE OR a.is_impossible_attendance = TRUE
    ORDER BY a.date DESC;
    """)
    print(" -> Created SQL View: vw_proxy_attendance_fraud")

    # 3. Infrastructure Impact View
    conn.execute("""
    CREATE OR REPLACE VIEW vw_infrastructure_impact AS
    SELECT 
        i.has_electricity,
        i.has_drinking_water,
        i.has_functional_toilet,
        i.has_boundary_wall,
        i.has_playground,
        ROUND(AVG(a.attendance_rate_pct), 2) AS avg_attendance_pct,
        ROUND(AVG(t.normalized_score_pct), 2) AS avg_test_score_pct
    FROM fact_infrastructure i
    JOIN fact_attendance a ON i.school_id = a.school_id
    JOIN fact_test_scores t ON i.school_id = t.school_id
    GROUP BY 1, 2, 3, 4, 5;
    """)
    print(" -> Created SQL View: vw_infrastructure_impact")

    # 4. MDM Procurement Summary View
    conn.execute("""
    CREATE OR REPLACE VIEW vw_mdm_procurement_summary AS
    SELECT 
        m.vendor_name,
        m.grain_type,
        COUNT(m.procurement_id) AS total_orders,
        ROUND(SUM(m.quantity_kg), 2) AS total_quantity_kg,
        ROUND(SUM(m.total_cost_inr), 2) AS total_cost_inr,
        ROUND(SUM(m.total_cost_inr) / NULLIF(SUM(m.quantity_kg), 0), 2) AS avg_cost_per_kg
    FROM fact_mdm_procurement m
    GROUP BY m.vendor_name, m.grain_type
    ORDER BY total_cost_inr DESC;
    """)
    print(" -> Created SQL View: vw_mdm_procurement_summary")

    conn.close()
    print(f"[Warehouse Builder] Successfully built Gold DuckDB warehouse at {db_path}!")
    return str(db_path)

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parents[2]
    s_dir = base_dir / "data" / "silver"
    g_dir = base_dir / "data" / "gold"
    build_gold_warehouse(s_dir, g_dir)
