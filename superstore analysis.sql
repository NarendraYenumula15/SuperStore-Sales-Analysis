CREATE DATABASE analysis_db;
USE analysis_db;
SHOW TABLES;
SELECT * FROM fact_sales LIMIT 5;
CREATE TABLE monthly_kpi AS
SELECT 
    year,
    month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin_adjusted), 2) AS avg_profit_margin,
    ROUND(AVG(shipping_days), 2) AS avg_shipping_days
FROM fact_sales
GROUP BY year, month;

SELECT * FROM monthly_kpi LIMIT 10;


CREATE TABLE category_kpi AS
SELECT 
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin_adjusted), 2) AS avg_profit_margin
FROM fact_sales
GROUP BY category;

SELECT * FROM category_kpi;



SHOW COLUMNS FROM fact_sales;


CREATE TABLE subcategory_kpi AS
SELECT 
    category,
    `sub-category` AS sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin_adjusted), 2) AS avg_profit_margin
FROM fact_sales
GROUP BY category, `sub-category`;

SELECT * FROM subcategory_kpi;


CREATE TABLE region_kpi AS
SELECT 
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(AVG(profit_margin_adjusted), 2) AS avg_profit_margin
FROM fact_sales
GROUP BY region;

SELECT * FROM region_kpi;

ALTER TABLE fact_sales
ADD PRIMARY KEY (row_id);

ALTER TABLE fact_sales
MODIFY sales DOUBLE NOT NULL,
MODIFY quantity BIGINT NOT NULL,
MODIFY order_date DATETIME NOT NULL,
MODIFY ship_date DATETIME NOT NULL;

ALTER TABLE fact_sales
ADD CONSTRAINT chk_sales CHECK (sales >= 0),
ADD CONSTRAINT chk_quantity CHECK (quantity > 0),
ADD CONSTRAINT chk_discount CHECK (discount BETWEEN 0 AND 1),
ADD CONSTRAINT chk_shipping_days CHECK (shipping_days >= 0),
ADD CONSTRAINT chk_month CHECK (month BETWEEN 1 AND 12),
ADD CONSTRAINT chk_quarter CHECK (quarter BETWEEN 1 AND 4);

ALTER TABLE fact_sales
ADD CONSTRAINT chk_shipping_dates
CHECK (ship_date >= order_date);

SHOW TABLES;


