# Self Join in PostgreSQL

A self join is a regular join operation where a table is joined with itself. This is useful when you need to compare rows within the same table or query hierarchical data structures.

## Basic Syntax

```sql
SELECT a.column1, a.column2, b.column1, b.column2
FROM table_name a
JOIN table_name b ON a.common_field = b.common_field
[WHERE condition];
```

## Common Use Cases

1. **Employee-Manager Relationships**:

   ```sql
   SELECT e.employee_name, m.employee_name AS manager_name
   FROM employees e
   JOIN employees m ON e.manager_id = m.employee_id;
   ```

2. **Finding Duplicate Records**:

   ```sql
   SELECT a.*
   FROM customers a
   JOIN customers b ON a.email = b.email AND a.id <> b.id;
   ```

3. **Hierarchical Data (e.g., organizational charts)**:
   ```sql
   SELECT child.name, parent.name AS parent_name
   FROM categories child
   LEFT JOIN categories parent ON child.parent_id = parent.id;
   ```

## Types of Self Joins

1. **Inner Self Join**:

   ```sql
   SELECT a.*, b.*
   FROM table_name a
   INNER JOIN table_name b ON a.id = b.related_id;
   ```

2. **Left Self Join**:

   ```sql
   SELECT a.*, b.*
   FROM table_name a
   LEFT JOIN table_name b ON a.id = b.related_id;
   ```

3. **Right Self Join**:
   ```sql
   SELECT a.*, b.*
   FROM table_name a
   RIGHT JOIN table_name b ON a.id = b.related_id;
   ```

## Practical Example

```sql
-- Find all pairs of employees who work in the same department
SELECT e1.name AS employee1, e2.name AS employee2, e1.department
FROM employees e1
JOIN employees e2
  ON e1.department = e2.department
  AND e1.id < e2.id  -- Avoids duplicate pairs and self-matches
ORDER BY e1.department;
```

## Performance Considerations

- Self joins can be resource-intensive for large tables
- Ensure proper indexes exist on the join columns
- Consider using CTEs (Common Table Expressions) for complex self joins

Self joins are a powerful tool when you need to analyze relationships within a single table.
