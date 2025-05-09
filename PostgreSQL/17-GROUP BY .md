# GROUP BY in PostgreSQL

The `GROUP BY` clause in PostgreSQL is used to group rows that have the same values in specified columns into aggregated data. It's commonly used with aggregate functions like `COUNT()`, `SUM()`, `AVG()`, `MAX()`, and `MIN()`.

## Basic Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

## Examples

1. **Simple GROUP BY**:

   ```sql
   SELECT department, COUNT(*) as employee_count
   FROM employees
   GROUP BY department;
   ```

2. **GROUP BY with multiple columns**:

   ```sql
   SELECT department, job_title, AVG(salary) as avg_salary
   FROM employees
   GROUP BY department, job_title;
   ```

3. **GROUP BY with HAVING clause** (filtering groups):

   ```sql
   SELECT department, COUNT(*) as employee_count
   FROM employees
   GROUP BY department
   HAVING COUNT(*) > 5;
   ```

4. **GROUP BY with expressions**:
   ```sql
   SELECT EXTRACT(YEAR FROM hire_date) as hire_year, COUNT(*)
   FROM employees
   GROUP BY hire_year;
   ```

## PostgreSQL-Specific Features

1. **GROUPING SETS**:

   ```sql
   SELECT department, job_title, COUNT(*)
   FROM employees
   GROUP BY GROUPING SETS ((department), (job_title), ());
   ```

2. **CUBE** (all possible grouping sets):

   ```sql
   SELECT department, job_title, COUNT(*)
   FROM employees
   GROUP BY CUBE (department, job_title);
   ```

3. **ROLLUP** (hierarchical grouping sets):

   ```sql
   SELECT year, quarter, month, SUM(sales)
   FROM sales_data
   GROUP BY ROLLUP (year, quarter, month);
   ```

4. **DISTINCT ON with GROUP BY** (PostgreSQL extension):
   ```sql
   SELECT DISTINCT ON (department) department, employee_name, salary
   FROM employees
   ORDER BY department, salary DESC;
   ```

## Performance Considerations

- Add indexes on columns used in GROUP BY clauses
- Use FILTER clauses with aggregates for conditional aggregation
- Consider using window functions (OVER clause) for some use cases instead of GROUP BY

Remember that in PostgreSQL, you can GROUP BY column names, column aliases, or expressions, but you cannot GROUP BY column numbers (unlike some other databases).
