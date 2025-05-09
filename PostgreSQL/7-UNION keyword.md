The `UNION` keyword in PostgreSQL is used to **combine the results of two or more `SELECT` statements** into a single result set, **eliminating duplicate rows by default**.

---

## ✅ **Syntax**

```sql
SELECT column1, column2 FROM table1
UNION
SELECT column1, column2 FROM table2;
```

---

## 🔸 **Key Rules**

- All `SELECT` statements must have the **same number of columns**
- Columns must have **compatible data types**
- Results are sorted by default in some cases unless overridden

---

## 🔄 **UNION vs UNION ALL**

| Keyword     | Removes Duplicates | Keeps Duplicates | Faster |
| ----------- | ------------------ | ---------------- | ------ |
| `UNION`     | ✅ Yes             | ❌ No            | ❌     |
| `UNION ALL` | ❌ No              | ✅ Yes           | ✅     |

---

## 🔸 **Examples**

### 1. Basic `UNION`

```sql
SELECT name FROM customers
UNION
SELECT name FROM vendors;
```

✅ Combines customer and vendor names, removing duplicates

---

### 2. `UNION ALL`

```sql
SELECT product_id FROM warehouse_1
UNION ALL
SELECT product_id FROM warehouse_2;
```

✅ Includes duplicate product IDs (if any)

---

### 3. With `ORDER BY`

If you want to sort the final result:

```sql
SELECT name FROM customers
UNION
SELECT name FROM vendors
ORDER BY name;
```

---
