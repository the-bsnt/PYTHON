That’s a **very good question** — this is exactly how you should think before deploying to a server 👍
I’ll give you a **clear, practical checklist** for deploying **using a non-root user** (best practice).

I’ll assume a typical Linux server (Ubuntu/Debian) and a web app (Django / Node / React / etc.). Adjust as needed.

---

# ✅ Pre-deployment checklist (with a non-root user)

## 1️⃣ Create a dedicated deployment user

Never deploy as `root`.

```bash
sudo adduser deploy
```

Give sudo access (only if needed):

```bash
sudo usermod -aG sudo deploy
```

Switch to the user:

```bash
su - deploy
```

---

## 2️⃣ Secure SSH access (VERY IMPORTANT)

### 🔹 Disable password login (use SSH keys)

On your local machine:

```bash
ssh-keygen
ssh-copy-id deploy@SERVER_IP
```

On server:

```bash
sudo nano /etc/ssh/sshd_config
```

Set:

```
PermitRootLogin no
PasswordAuthentication no
```

Restart SSH:

```bash
sudo systemctl restart ssh
```

✅ This prevents brute-force attacks.

---

## 3️⃣ Set correct directory structure & ownership

Example structure:

```bash
/var/www/myapp
```

Create it:

```bash
sudo mkdir -p /var/www/myapp
sudo chown -R deploy:deploy /var/www/myapp
```

Permissions:

```bash
chmod 755 /var/www
chmod 755 /var/www/myapp
```

---

## 4️⃣ Install system dependencies (as root)

Only root should install system packages:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip nginx git ufw
```

After this → switch back to `deploy`.

---

## 5️⃣ Clone project as deploy user

```bash
cd /var/www/myapp
git clone https://github.com/yourrepo.git .
```

✅ Files now belong to `deploy`, not root.

---

## 6️⃣ Environment variables & secrets

Never hard-code secrets.

Create `.env`:

```bash
nano .env
```

Example:

```
DEBUG=False
SECRET_KEY=xxxxx
DATABASE_URL=xxxxx
```

Protect it:

```bash
chmod 600 .env
```

---

## 7️⃣ Virtual environment / runtime setup

### Python (Django / DRF)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Node / React

```bash
npm install
npm run build
```

---

## 8️⃣ Database access (least privilege)

Create DB user:

```sql
CREATE USER myappuser WITH PASSWORD 'strongpass';
GRANT ALL PRIVILEGES ON DATABASE myapp TO myappuser;
```

❌ Don’t use `postgres` or `root` DB user.

---

## 9️⃣ Web server & process manager

### 🔹 Gunicorn / Uvicorn (Django)

Run as **deploy user**, not root.

Systemd service:

```ini
User=deploy
Group=www-data
```

### 🔹 Nginx

- Runs as root only to bind ports
- Serves files owned by deploy
- Reads static files (755 permissions)

---

## 🔟 Static files & permissions (Django)

```bash
python manage.py collectstatic
```

Ensure:

```bash
chown -R deploy:www-data staticfiles
chmod -R 755 staticfiles
```

---

## 1️⃣1️⃣ Firewall & ports

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

---

## 1️⃣2️⃣ Logs & monitoring

Ensure deploy user can write logs:

```bash
sudo mkdir /var/log/myapp
sudo chown deploy:deploy /var/log/myapp
```

---

## 🔐 Security must-checks

✅ Root login disabled
✅ App runs as non-root
✅ Secrets in `.env`
✅ Correct file ownership
✅ Firewall enabled

---

## 🧠 Golden rule

> **Root installs & configures.
> Deploy user runs the app.**

---

### Want this checklist customized?

Tell me:

- Django / FastAPI / Node?
- Docker or bare metal?
- DigitalOcean / AWS / VPS?
- Nginx or Apache?

I’ll give you **exact commands for your stack** 🚀
