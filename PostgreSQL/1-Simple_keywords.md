Here are some **basic PostgreSQL keywords and syntax** examples that are essential for working with a database:

---

### 1. **CREATE TABLE**

Defines a new table.

```sql
CREATE TABLE table_name (
  column1 datatype CONSTRAINTS,
  column2 datatype CONSTRAINTS
);
```

**Example:**

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);
```

---

### 2. **INSERT INTO**

Adds new rows to a table.

```sql
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);
```

**Example:**

```sql
INSERT INTO users (name, email)
VALUES ('Alice', 'alice@example.com');
```

---

### 3. **SELECT**

Retrieves data.

```sql
SELECT column1, column2 FROM table_name;
```

**Example:**

```sql
SELECT name, email FROM users;
```

---

### 4. **UPDATE**

Modifies existing data.

```sql
UPDATE table_name
SET column1 = value1
WHERE condition;
```

**Example:**

```sql
UPDATE users
SET email = 'new_email@example.com'
WHERE name = 'Alice';
```

---

### 5. **DELETE**

Removes rows.

```sql
DELETE FROM table_name
WHERE condition;
```

**Example:**

```sql
DELETE FROM users
WHERE name = 'Alice';
```

---

### 6. **WHERE**

Filters rows based on a condition.

```sql
SELECT * FROM table_name
WHERE condition;
```

---

### 7. **ORDER BY**

Sorts results.

```sql
SELECT * FROM table_name
ORDER BY column_name ASC|DESC;
```

---

### 8. **JOIN**

Combines rows from two or more tables.

```sql
SELECT *
FROM table1
JOIN table2 ON table1.id = table2.foreign_id;
```
