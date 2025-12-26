You select **another SSH key** depending on **where** you want to use it (Git, server login, GitHub/GitLab, etc.).
Here are the **correct and practical ways**, from most common to interview-safe.

---

## 1️⃣ Temporarily select an SSH key (one command)

```bash
ssh -i ~/.ssh/id_ed25519_work user@server_ip
```

- Uses **only this key**
- Does **not** change global config
- Best for testing or one-time access

---

## 2️⃣ Permanent selection using `~/.ssh/config` (BEST PRACTICE)

This is what professionals do 👇

### Edit config file

```bash
nano ~/.ssh/config
```

### Example configuration

```ssh
# GitHub personal
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes

# GitHub work
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes
```

### Use it

```bash
git clone git@github-work:company/repo.git
```

✅ Clean
✅ No env hacks
✅ Interview-approved

---

## 3️⃣ Using SSH Agent (multiple keys loaded)

### Start agent

```bash
eval "$(ssh-agent -s)"
```

### Add specific key

```bash
ssh-add ~/.ssh/id_ed25519_work
```

### List loaded keys

```bash
ssh-add -l
```

### Remove a key

```bash
ssh-add -d ~/.ssh/id_ed25519_work
```

👉 SSH will automatically try loaded keys.

---

## 4️⃣ Select SSH key for Git only (per-repo)

Inside repo:

```bash
git config core.sshCommand "ssh -i ~/.ssh/id_ed25519_work"
```

Check:

```bash
git config --get core.sshCommand
```

---

## 5️⃣ Common GitHub / GitLab issue fix ⚠️

If Git keeps using the wrong key:

```bash
ssh -T git@github.com
```

If wrong key:

```bash
ssh-add -D
ssh-add ~/.ssh/id_ed25519_correct
```

Or force it with:

```ssh
IdentitiesOnly yes
```

---

## 6️⃣ Quick decision guide

| Situation                | Best method                  |
| ------------------------ | ---------------------------- |
| One-time login           | `ssh -i`                     |
| GitHub multiple accounts | `~/.ssh/config`              |
| CI / automation          | `ssh-agent`                  |
| Per repo                 | `git config core.sshCommand` |

---

## One-line interview answer

> SSH key selection is done either temporarily using `ssh -i` or permanently using the `~/.ssh/config` file with `IdentityFile`, which is the recommended approach.

---

If you want, tell me:

- **GitHub / GitLab / Bitbucket?**
- **Linux / WSL / Mac?**
- **Personal + Work setup?**

I’ll give you an exact config tailored to your setup.
