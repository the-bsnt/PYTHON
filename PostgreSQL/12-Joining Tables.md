# Joining Tables in PostgreSQL

PostgreSQL supports several types of joins to combine data from multiple tables:

## Basic Join Types

### INNER JOIN

Returns rows when there's a match in both tables:

```sql
SELECT a.column1, b.column2
FROM table_a a
INNER JOIN table_b b ON a.id = b.a_id;
```

### LEFT (OUTER) JOIN

Returns all rows from the left table, with matching rows from the right table (or NULLs if no match):

```sql
SELECT a.column1, b.column2
FROM table_a a
LEFT JOIN table_b b ON a.id = b.a_id;
```

### RIGHT (OUTER) JOIN

Returns all rows from the right table, with matching rows from the left table (or NULLs if no match):

```sql
SELECT a.column1, b.column2
FROM table_a a
RIGHT JOIN table_b b ON a.id = b.a_id;
```

### FULL (OUTER) JOIN

Returns all rows when there's a match in either table:

```sql
SELECT a.column1, b.column2
FROM table_a a
FULL JOIN table_b b ON a.id = b.a_id;
```

## Special Join Types

### CROSS JOIN

Returns the Cartesian product of both tables (all possible combinations):

```sql
SELECT a.column1, b.column2
FROM table_a a
CROSS JOIN table_b b;
```

### NATURAL JOIN

Joins tables on columns with the same name (use with caution):

```sql
SELECT column1, column2
FROM table_a
NATURAL JOIN table_b;
```

### SELF JOIN

Joins a table to itself:

```sql
SELECT a.column1, b.column1
FROM table a
JOIN table b ON a.parent_id = b.id;
```

## Join with Multiple Tables

```sql
SELECT a.column1, b.column2, c.column3
FROM table_a a
JOIN table_b b ON a.id = b.a_id
JOIN table_c c ON b.id = c.b_id;
```

## Join with WHERE Clause

```sql
SELECT a.column1, b.column2
FROM table_a a, table_b b
WHERE a.id = b.a_id;
```

PostgreSQL also supports advanced join operations like LATERAL joins and joins with complex conditions.
