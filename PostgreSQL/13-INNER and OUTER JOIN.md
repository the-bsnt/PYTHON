# Understanding Inner Joins and Outer Joins in PostgreSQL

## Inner Joins

An **inner join** returns only the rows that have matching values in both tables being joined.

### Key Characteristics:

- Only includes records where the join condition is satisfied in both tables
- Non-matching rows from both tables are excluded
- Most commonly used type of join

```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.id;
```

This query would return only employees who are assigned to a department that exists in the departments table.

## Outer Joins

Outer joins return all rows from one table and the matched rows from the other table. There are three types:

### 1. LEFT OUTER JOIN (or LEFT JOIN)

- Returns all records from the left table (first table mentioned)
- Returns matched records from the right table
- For unmatched rows from the left, NULL values are returned for right table columns

```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.id;
```

This would return all employees, even those not assigned to any department (with NULL for department_name).

### 2. RIGHT OUTER JOIN (or RIGHT JOIN)

- Returns all records from the right table
- Returns matched records from the left table
- For unmatched rows from the right, NULL values are returned for left table columns

```sql
SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.dept_id = departments.id;
```

This would return all departments, even those with no employees (with NULL for employee names).

### 3. FULL OUTER JOIN (or FULL JOIN)

- Returns all records when there's a match in either left or right table
- Combines results of both LEFT and RIGHT joins
- For unmatched rows on either side, NULL values are returned for the other table's columns

```sql
SELECT employees.name, departments.department_name
FROM employees
FULL JOIN departments ON employees.dept_id = departments.id;
```

This would return all employees and all departments, with NULLs where there are no matches.

## Visual Representation

```
Table A        Table B
-------        -------
1 | John       1 | Sales
2 | Mary       3 | HR
3 | Sam
4 | Lisa

-- INNER JOIN (A ∩ B)
John | Sales
Sam  | HR

-- LEFT JOIN (All A + matching B)
John | Sales
Mary | NULL
Sam  | HR
Lisa | NULL

-- RIGHT JOIN (All B + matching A)
John | Sales
NULL | HR
Sam  | HR

-- FULL JOIN (All A + All B)
John | Sales
Mary | NULL
Sam  | HR
Lisa | NULL
NULL | HR
```

Choose the join type based on whether you want to preserve unmatched rows from one or both tables in your results.

---

### Are those same?

```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.id;
or
SELECT employees.name, departments.department_name
FROM department
RIGHT JOIN employees ON employees.dept_id = departments.id;
```

Yes, the two queries you provided are **functionally equivalent** - they will produce exactly the same result set.

## LEFT JOIN vs RIGHT JOIN Comparison

### Query 1 (LEFT JOIN):

```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.id;
```

### Query 2 (RIGHT JOIN):

```sql
SELECT employees.name, departments.department_name
FROM departments
RIGHT JOIN employees ON employees.dept_id = departments.id;
```

## Why They're Equivalent:

1. **Table Order Reversal**:

   - In LEFT JOIN, `employees` is the left/preserved table
   - In RIGHT JOIN, `employees` becomes the right/preserved table

2. **Same Logical Operation**:

   - Both queries return all employees regardless of whether they have a department
   - Both will show NULL for `department_name` if an employee has no department

3. **Same Join Condition**:
   - The ON clause is identical in both queries

## Key Differences:

1. **Readability**:

   - LEFT JOIN is generally preferred as it's more intuitive (read left-to-right)
   - RIGHT JOIN can be confusing when tables are listed in reverse order

2. **Performance**:

   - In PostgreSQL, the query planner will typically optimize both to the same execution plan
   - No performance difference in practice

3. **Common Usage**:
   - LEFT JOIN is used much more frequently (about 90%+ of cases in my experience)
   - RIGHT JOIN is relatively rare in production code

## Recommendation:

Use the LEFT JOIN version (Query 1) because:

- It follows the more common pattern
- Is easier to read and understand
- Matches how most developers think about joins (left table = primary table)

The RIGHT JOIN version works perfectly fine but might cause a double-take for other developers reading your code.
