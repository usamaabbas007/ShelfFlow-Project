
-- SQL: Aggregate daily sales and shortages by store and product
SELECT
    store_id,
    product_id,
    date,
    SUM(units_sold) AS total_units_sold,
    SUM(units_short) AS total_units_short,
    SUM(units_restocked) AS total_units_restocked,
    AVG(ending_inventory) AS avg_inventory
FROM sales_inventory
GROUP BY store_id, product_id, date;
