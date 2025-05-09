### How to use `SUBSTRING()`, `LEFT()`, and `RIGHT()` in PostgreSQL — all useful for extracting parts of a string.

---

## 🔹 1. `SUBSTRING()` — Extract a portion of a string by position or regex

### ✅ Syntax (positional):

```sql
SUBSTRING(string FROM start_position FOR length)
```

### 🧪 Example:

```sql
SELECT SUBSTRING('PostgreSQL' FROM 1 FOR 4);  -- Output: 'Post'
```

---

### ✅ Syntax (regex-based):

```sql
SUBSTRING(string FROM 'regex_pattern')
```

### 🧪 Example:

```sql
SELECT SUBSTRING('abc123xyz' FROM '[0-9]+');  -- Output: '123'
```

---

## 🔹 2. `LEFT()` — Get the leftmost N characters

### ✅ Syntax:

```sql
LEFT(string, number_of_characters)
```

### 🧪 Example:

```sql
SELECT LEFT('PostgreSQL', 4);  -- Output: 'Post'
```

---

## 🔹 3. `RIGHT()` — Get the rightmost N characters

### ✅ Syntax:

```sql
RIGHT(string, number_of_characters)
```

### 🧪 Example:

```sql
SELECT RIGHT('PostgreSQL', 4);  -- Output: 'SQL'
```

---

## 🧠 Bonus Tip: Combine with other functions

```sql
SELECT UPPER(LEFT(name, 1)) || LOWER(SUBSTRING(name FROM 2))
FROM users;
```

✅ Capitalizes only the first letter of a name.

---

---

## To get the **last 3 characters** of a string using `SUBSTRING()` in PostgreSQL, you can use this pattern:

---

### ✅ Using `SUBSTRING()` + `LENGTH()`:

```sql
SELECT SUBSTRING('PostgreSQL' FROM LENGTH('PostgreSQL') - 2 FOR 3);
```

### 🔍 Explanation:

- `LENGTH('PostgreSQL')` returns 10
- `10 - 2 = 8`, so it starts at position 8
- Extracts 3 characters → `'SQL'`

---

### 🔁 Generic Version (for any column):

```sql
SELECT SUBSTRING(column_name FROM LENGTH(column_name) - 2 FOR 3)
FROM your_table;
```

✅ This works for any string, no matter its length.

---

### 🔄 Simpler Alternative with `RIGHT()`:

```sql
SELECT RIGHT('PostgreSQL', 3);  -- Also returns 'SQL'
```

Use `RIGHT()` if you're **always taking from the end** — it's cleaner.
