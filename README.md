# SuperStore-Sales-Analysis
# Automated ETL & Executive KPI Dashboard

## Project Overview
This project demonstrates an **end-to-end data pipeline and analytics workflow** for operational sales data. It includes: 

- Ingesting raw operational data files.
- Performing **Python ETL** (Extract, Transform, Load) with data cleaning, preprocessing, and validation.
- Loading processed data into a **MySQL database**.
- Creating **KPI tables** for reporting.
- Simulating **scheduled automated refresh** logic.
- Building an **interactive, executive-level Power BI dashboard**.
- Tracking **trend analysis** and **performance metrics**.
- Generating **automated summary outputs**.
- Documenting **end-to-end data flow and automation logic**.

---

## Technologies Used

- **Python**: Pandas, NumPy, SQLAlchemy, MySQL Connector  
- **MySQL**: Relational database for storing cleaned operational data  
- **Power BI**: Interactive dashboard for KPI reporting and trend visualization  
- **ETL Concepts**: Data ingestion, transformation, validation, and loading  
- **Automation**: Python scripts scheduled for automated data refresh  

---

## Architecture / Workflow

```text
Raw Operational Data (CSV / Excel) 
           │
           ▼
   Python ETL Pipeline
   - Data Cleaning & Validation
   - Feature Engineering
           │
           ▼
   MySQL Database
   - Fact & KPI Tables
           │
           ▼
   Power BI Dashboard
   - KPI Cards
   - Trend Analysis Charts
   - Product & Region Insights
   - Ship Mode Analysis
           │
           ▼
   Automated Summary Outputs
