In PostgreSQL, **wildcard characters** are used mainly with the `LIKE`, `ILIKE`, and `SIMILAR TO` operators for **pattern matching** in strings. Here’s a breakdown:

---

## 🔸 1. `LIKE` and `ILIKE` Wildcards

| Wildcard | Meaning                             | Example                            |
| -------- | ----------------------------------- | ---------------------------------- |
| `%`      | Matches **zero or more characters** | `'Jo%'` → `John`, `Jordan`, `Jo`   |
| `_`      | Matches **exactly one character**   | `'J_n'` → `Jan`, `Jon`, not `John` |

- `LIKE` is **case-sensitive**
- `ILIKE` is **case-insensitive**

### ✅ Examples:

```sql
-- Names that start with "Jo"
SELECT * FROM users WHERE name LIKE 'Jo%';

-- Names with 4 letters starting with "J"
SELECT * FROM users WHERE name LIKE 'J___';

-- Case-insensitive match
SELECT * FROM users WHERE name ILIKE 'jo%';
```

---

## 🔸 2. `SIMILAR TO` Wildcards (Regex-like)

| Wildcard | Meaning                 | Example                              |
| -------- | ----------------------- | ------------------------------------ | ------ | ------ |
| `%`      | Zero or more characters | `'Jo%'`                              |
| `_`      | Exactly one character   | `'J_n'`                              |
| `        | `                       | OR (alternation)                     | `'John | Jane'` |
| `[]`     | Character set           | `'[Jj]ohn'` matches `John` or `john` |
| `()`     | Grouping                | `'(abc                               | xyz)'` |

### ✅ Example:

```sql
-- Match names with "john" or "jane"
SELECT * FROM users
WHERE name SIMILAR TO '%(john|jane)%';
```

---

## 🔸 3. Regex Match (`~`, `~*`)

PostgreSQL also supports **full regular expressions**, as discussed earlier.

---

#### Great! Let's walk through how to implement the wildcard characters `[]` and `()` in **PostgreSQL**, specifically with the `SIMILAR TO` operator and regular expressions (`~` or `~*`).

---

## ✅ 1. `[]` — Character Classes

**Purpose:** Match **any one character** inside the brackets.

### ➤ Using `~` (regex):

```sql
SELECT * FROM users
WHERE name ~ '^[Jj]ohn$';
```

✅ Matches: `John`, `john`  
❌ Does NOT match: `JOHN`, `jOhn`

---

## ✅ 2. `()` and `|` — Grouping and Alternation

**Purpose:** Group patterns and allow alternation (logical OR).

### ➤ Using `SIMILAR TO`:

```sql
SELECT * FROM users
WHERE name SIMILAR TO '%(john|jane)%';
```

✅ Matches: `johnsmith`, `maryjane`, `thejohn`  
❌ Does NOT match: `bob`, `jack`

---

### ➤ Using regex (`~*` for case-insensitive):

```sql
SELECT * FROM users
WHERE name ~* '(john|jane)';
```

✅ Matches: `John`, `JANE`, `littlejohn`

---

## 🧪 Bonus Example Combining Both

```sql
SELECT * FROM users
WHERE name ~* '^[A-Z][a-z]+ (Smith|Jones)$';
```

✅ Matches: `Alice Smith`, `Bob Jones`  
❌ Does NOT match: `alice smith`, `Alice john`

---

These features give PostgreSQL powerful string filtering capability beyond simple `LIKE`.
