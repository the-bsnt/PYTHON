# HAVING Clause in PostgreSQL

The `HAVING` clause in PostgreSQL is used to filter groups after the `GROUP BY` clause has been applied. It's similar to the `WHERE` clause, but while `WHERE` filters individual rows before grouping, `HAVING` filters groups after aggregation.

## Basic Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

## Key Differences: HAVING vs WHERE

| Feature    | WHERE                          | HAVING                             |
| ---------- | ------------------------------ | ---------------------------------- |
| Timing     | Filters rows before grouping   | Filters groups after grouping      |
| Usage      | Can be used without GROUP BY   | Requires GROUP BY (or aggregation) |
| Aggregates | Cannot use aggregate functions | Can use aggregate functions        |

## Examples

1. **Basic HAVING with COUNT**:

   ```sql
   SELECT department, COUNT(*) as emp_count
   FROM employees
   GROUP BY department
   HAVING COUNT(*) > 5;
   ```

2. **HAVING with multiple conditions**:

   ```sql
   SELECT department, AVG(salary) as avg_salary
   FROM employees
   GROUP BY department
   HAVING AVG(salary) > 50000 AND COUNT(*) > 3;
   ```

3. **HAVING with different aggregate functions**:

   ```sql
   SELECT product_id, SUM(quantity) as total_quantity, AVG(price) as avg_price
   FROM sales
   GROUP BY product_id
   HAVING SUM(quantity) > 100 AND AVG(price) < 50;
   ```

4. **HAVING with string functions**:

   ```sql
   SELECT SUBSTRING(email FROM '@(.*)$') as domain, COUNT(*)
   FROM users
   GROUP BY domain
   HAVING SUBSTRING(email FROM '@(.*)$') LIKE '%.com';
   ```

5. **Combining WHERE and HAVING**:
   ```sql
   SELECT department, AVG(salary) as avg_salary
   FROM employees
   WHERE hire_date > '2020-01-01'
   GROUP BY department
   HAVING AVG(salary) > 60000;
   ```

## Advanced Usage

1. **HAVING with GROUPING SETS/CUBE/ROLLUP**:

   ```sql
   SELECT department, job_title, COUNT(*)
   FROM employees
   GROUP BY CUBE(department, job_title)
   HAVING COUNT(*) > 10;
   ```

2. **HAVING with window functions** (requires subquery):
   ```sql
   SELECT * FROM (
     SELECT department,
            AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
     FROM employees
   ) subquery
   WHERE dept_avg_salary > 70000;
   ```

## Performance Tips

- Apply the most restrictive filters in the WHERE clause when possible
- Use HAVING only for conditions that must be evaluated after aggregation
- Consider creating indexes on columns used in HAVING conditions when appropriate

Remember that HAVING can reference:

- Any column in the GROUP BY clause
- Any aggregate function
- Aliases defined in the SELECT list
- But not regular columns that aren't in the GROUP BY or aggregated
