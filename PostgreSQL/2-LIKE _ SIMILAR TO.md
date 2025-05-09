The `LIKE` keyword in PostgreSQL is used to search for a **pattern** in a column, typically with `WHERE`.

---

### 🔹 **Syntax:**

```sql
SELECT column1, column2
FROM table_name
WHERE column1 LIKE 'pattern';
```

---

### 🔹 **Pattern Matching Symbols:**

- `%` – Matches **zero or more** characters
- `_` – Matches **exactly one** character

---

### 🔹 **Examples:**

#### 1. Match values starting with 'A':

```sql
SELECT * FROM users
WHERE name LIKE 'A%';
```

#### 2. Match values ending with 'son':

```sql
SELECT * FROM users
WHERE name LIKE '%son';
```

#### 3. Match values containing 'li':

```sql
SELECT * FROM users
WHERE name LIKE '%li%';
```

#### 4. Match names like 'A_ice' (e.g., 'Alice', 'Anice'):

```sql
SELECT * FROM users
WHERE name LIKE 'A_ice';
```

---

To search for **multiple patterns** in a column using the `LIKE` keyword in PostgreSQL, you can combine conditions using the `OR` operator, or use `SIMILAR TO` or `~` (regex).

---

### ✅ **Option 1: Multiple `LIKE` with `OR`**

```sql
SELECT * FROM users
WHERE name LIKE '%john%' OR name LIKE '%doe%';
```

---

### ✅ **Option 2: `SIMILAR TO` (SQL regex-like)**

```sql
SELECT * FROM users
WHERE name SIMILAR TO '%(john|doe)%';
```

---

### ✅ **Option 3: Regex with `~` (PostgreSQL-specific)**

```sql
SELECT * FROM users
WHERE name ~ '(john|doe)';
```

- Use `~*` for **case-insensitive** match:

```sql
SELECT * FROM users
WHERE name ~* '(john|doe)';
```
