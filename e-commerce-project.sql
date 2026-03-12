SHOW DATABASES;
CREATE DATABASE ecommerce;

-- Creación de Query´s para gráficos 

-- Distribución de riesgo de churn --
SELECT 
    risk_segment,
    COUNT(*) AS customers
FROM analytics_customer_360
GROUP BY risk_segment;

-- Promedio de engagement --
SELECT 
    AVG(engagement_score) AS avg_engagement
FROM analytics_customer_360;

-- Clientes en riesgo de churn --
SELECT 
    predicted_churn_rule_based,
    COUNT(*) AS total
FROM analytics_customer_360
GROUP BY predicted_churn_rule_based;

-- Inactividad Promedio --
SELECT 
    AVG(inactivity_score) AS avg_inactivity
FROM analytics_customer_360;

-- Top Clientes con mayor riesgo --
SELECT 
    customer_id,
    risk_score
FROM analytics_customer_360
ORDER BY risk_score DESC
LIMIT 10;

-- Segmentación de riesgo --
CREATE OR REPLACE VIEW dashboard_risk_segments AS
SELECT
    risk_segment,
    COUNT(*) AS total_customers,
    AVG(lifetime_value) AS avg_ltv,
    AVG(total_purchases) AS avg_purchases
FROM analytics_customer_360
GROUP BY risk_segment;

-- Churn prediction --
CREATE OR REPLACE VIEW dashboard_churn_prediction AS
SELECT
    predicted_churn_rule_based,
    COUNT(*) AS customers
FROM analytics_customer_360
GROUP BY predicted_churn_rule_based;

-- Valor por país --
CREATE OR REPLACE VIEW dashboard_country_value AS
SELECT
    country,
    COUNT(*) AS customers,
    AVG(lifetime_value) AS avg_ltv
FROM analytics_customer_360
GROUP BY country
ORDER BY avg_ltv DESC;

-- Engagement vs compras --
CREATE OR REPLACE VIEW dashboard_engagement_sales AS
SELECT
    engagement_score,
    total_purchases,
    lifetime_value
FROM analytics_customer_360;

USE ecommerce_db;
SHOW FULL TABLES;
DROP VIEW IF EXISTS dashboard_churn_prediction;
DROP TABLE IF EXISTS dashboard_churn_prediction;

SELECT * 
FROM dashboard_churn_prediction;

SHOW TABLES;

SELECT user, host FROM mysql.user;

USE customer_db;
SHOW TABLES;

DESCRIBE analytics_customer_360;
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_name = 'analytics_customer_360';

SELECT COUNT(*) FROM ecommerce.analytics_customer_360;

SHOW TABLES;