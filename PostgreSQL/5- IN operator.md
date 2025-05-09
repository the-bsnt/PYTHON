The `IN` operator in PostgreSQL is used to **match a value against a list of values**. It’s a cleaner alternative to multiple `OR` conditions.

---

## ✅ **Syntax**

```sql
SELECT column1, column2
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

---

## 🔸 **Example: Match Specific Values**

```sql
SELECT * FROM users
WHERE country IN ('Nepal', 'India', 'Bhutan');
```

Same as:

```sql
WHERE country = 'Nepal' OR country = 'India' OR country = 'Bhutan';
```

---

## 🔸 **NOT IN**

```sql
SELECT * FROM users
WHERE status NOT IN ('inactive', 'banned');
```

---

## 🔸 **With Subquery**

```sql
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE country = 'Nepal');
```

---

## 🔒 Caution: `NULL` and `NOT IN`

If the list contains a `NULL`, `NOT IN` may return no rows (because NULL means "unknown").

### 🔸 Example of a common bug:

```sql
-- Suppose one status is NULL
SELECT * FROM users
WHERE status NOT IN ('active', 'banned');  -- Might return nothing!
```

---
