### **set operation keywords** in PostgreSQL: `INTERSECT`, `EXCEPT`, and how they relate to `UNION`.

---

## 🔷 1. `INTERSECT`

Returns only the rows that **exist in both** result sets (like a logical AND).

### ✅ Syntax:

```sql
SELECT column FROM table1
INTERSECT
SELECT column FROM table2;
```

### 🧪 Example:

```sql
SELECT user_id FROM newsletter_subscribers
INTERSECT
SELECT user_id FROM paying_customers;
```

✅ Returns users who are **both** subscribers and paying customers

---

## 🔷 2. `EXCEPT`

Returns rows from the **first SELECT** that do **not** exist in the second (like a logical difference).

### ✅ Syntax:

```sql
SELECT column FROM table1
EXCEPT
SELECT column FROM table2;
```

### 🧪 Example:

```sql
SELECT user_id FROM all_users
EXCEPT
SELECT user_id FROM banned_users;
```

✅ Returns all users **excluding** those who are banned

---

## 🔄 `INTERSECT ALL` and `EXCEPT ALL`

These keep duplicates, similar to `UNION ALL`. For example:

```sql
SELECT value FROM table1
INTERSECT ALL
SELECT value FROM table2;
```

---

### ⚠️ Notes:

- Columns must match in **number and type**
- PostgreSQL removes duplicates by default (except with `ALL`)
- Use `ORDER BY` after the **final** `SELECT` to sort combined results

---

Let me know if you'd like to dive into `WITH`, `CASE`, or aggregation functions (`GROUP BY`, `HAVING`) next.
