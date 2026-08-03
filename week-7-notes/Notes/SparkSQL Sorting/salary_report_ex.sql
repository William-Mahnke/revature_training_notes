-- Databricks/Spark SQL: create an in-memory training data set.
CREATE OR REPLACE TEMP VIEW employees AS
SELECT * FROM VALUES
  (104, 'Asha', 75000),
  (102, 'Ben',  92000),
  (103, 'Chen', 75000),
  (101, 'Diya', CAST(NULL AS INT)),
  (105, 'Evan', 62000)
AS employees(employee_id, employee_name, salary);

-- Report contract:
-- 1. Highest salary first.
-- 2. Missing salary at the bottom.
-- 3. Lower employee_id first when salaries tie.
SELECT employee_id, employee_name, salary
FROM employees
ORDER BY salary DESC NULLS LAST, employee_id ASC;