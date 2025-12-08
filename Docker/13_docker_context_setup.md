### 1️⃣ `build` section

```yaml
build:
  context: ./backend
  dockerfile: ../docker/django/Dockerfile
```

- **`context: ./backend`**

  - This is the **build context**. Docker can only see files **inside `./backend`** (relative to where `docker-compose.yml` is).
  - Everything outside `./backend` is **not accessible** to `COPY` or `ADD` commands inside the Dockerfile—unless you adjust paths or move the build context.

- **`dockerfile: ../docker/django/Dockerfile`**

  - This tells Docker **where the Dockerfile is located**, relative to the location of the `docker-compose.yml`.
  - Here, `../docker/django/Dockerfile` means: go **one level up** from the current folder, then into `docker/django/` to find `Dockerfile`.

⚠️ Important: The Dockerfile can be **outside the build context**, but any `COPY` or `ADD` commands inside it can **only access files inside the context** (`./backend` in this case).

---

### 3️⃣ Visualization of paths

Assume this project structure:

```
project/
├─ backend/
│  ├─ manage.py
│  └─ requirements.txt
├─ docker/
│  └─ django/
│     └─ Dockerfile
└─ docker-compose.yml
```

- `docker-compose.yml` is in `project/`
- `context: ./backend` → points to `project/backend`
- `dockerfile: ../docker/django/Dockerfile` → points to `project/docker/django/Dockerfile`

Inside `Dockerfile`:

```dockerfile
COPY . /app
```

- This copies **everything from `backend/`**, because `backend/` is the context.
- Files outside `backend/` (like other docker folders) **cannot be accessed** here.

---

If you want, I can rewrite this setup to **make the Dockerfile inside the context**, which simplifies paths and avoids tricky `../` references. That’s usually cleaner.

### 2️⃣ Relative Paths (`./` vs `../`)

- `./docker` → points to a `docker` folder **inside the current directory**.
- `../docker` → points to a `docker` folder **one level up from the current directory**.

Example directory structure:

```
project/
├─ backend/
│  └─ requirements.txt
├─ docker/
│  └─ Dockerfile
└─ docker-compose.yml
```

- If your terminal is inside `backend/`:

  - `../docker` → goes up one level (`project/`) and then into `docker/`. Correct path to Dockerfile.
  - `./docker` → looks for `backend/docker/` (doesn’t exist in this case).

---

### 3️⃣ Dockerfile `COPY` Consideration

Inside your Dockerfile:

```dockerfile
COPY ./backend/requirements.txt /app/
```

- `./backend/requirements.txt` is **relative to the build context**, not relative to the Dockerfile.
- So if your build context is `project/`, it works fine.
- If your build context is `backend/`, then `COPY ./backend/requirements.txt` will fail because Docker only sees `backend/` folder contents, not the parent.

---

✅ **Summary:**

- Use `../docker` when your Docker folder is **outside the current folder**.
- Use `./docker` when your Docker folder is **inside the current folder**.
- Always remember: **paths in COPY/ADD are relative to the build context**, not necessarily to the Dockerfile.
