The `BETWEEN` operator in PostgreSQL is used to **filter results within a specific range**, inclusive of the boundary values.

---

## ✅ **Syntax**

```sql
SELECT column1, column2
FROM table_name
WHERE column_name BETWEEN lower_bound AND upper_bound;
```

This is equivalent to:

```sql
WHERE column_name >= lower_bound AND column_name <= upper_bound;
```

---

## 🔸 **Examples**

### 1. Numeric Range

```sql
SELECT * FROM products
WHERE price BETWEEN 100 AND 500;
```

✅ Returns products priced from 100 to 500 **inclusive**

---

### 2. Date Range

```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

✅ Returns orders from January 1 to December 31, 2024

---

### 3. Text (Lexicographical Range)

```sql
SELECT * FROM customers
WHERE name BETWEEN 'A' AND 'M';
```

✅ Returns names that start with letters from A to M

---

## 🔁 NOT BETWEEN

```sql
SELECT * FROM employees
WHERE salary NOT BETWEEN 40000 AND 70000;
```

✅ Returns employees with salaries outside the specified range

---
