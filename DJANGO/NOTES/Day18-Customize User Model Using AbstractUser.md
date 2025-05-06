### **exact steps to customize the Django user model using `AbstractUser`** (not `AbstractBaseUser`), and allow login using **either email or username**, plus add extra fields like `address`.

---

## ✅ GOAL

- Custom user model with `address` field
- Allow login via email or username
- Keep using Django admin
- No changes to built-in password hashing/auth/etc.

---

## ✅ STEP-BY-STEP SETUP USING `AbstractUser`

---

### ✅ 1. **Create Custom User Model**

In `accounts/models.py`:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    address = models.TextField(blank=True)
```

---

### ✅ 2. **Register Custom User in `settings.py`**

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

> Do this **before your first `migrate`** or wipe DB if already migrated.

---

### ✅ 3. **Create a Custom User Form (optional)**

In `accounts/forms.py`:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "address", "password1", "password2")
```

---

### ✅ 4. **Update Django Admin to use your model**

In `accounts/admin.py`:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ("username", "email", "address", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("address",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("address",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```

---

### ✅ 5. **Create a Custom Auth Backend (for email or username login)**

In `accounts/backends.py`:

```python
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
```

---

### ✅ 6. **Tell Django to use your custom backend**

In `settings.py`:

```python
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailOrUsernameBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

---

### ✅ 7. **Run migrations**

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

---

### ✅ 8. **Create a superuser**

```bash
python manage.py createsuperuser
```

You’ll now have email, username, and address — all working!

---

### ✅ Optional: Create Login Form or View

Your `username` input field can say:

> `Username or Email`

Because your backend will now check both.

---

## ✅ Done! 🎉

---

### now admin can login with email also?

---

Great question — and the answer is: **yes**, the **Django admin** will also accept email **as a login credential**, **if you're using the custom authentication backend** correctly.

Let me explain how this works and how to make sure it’s active:

---

## ✅ Why It Works

You added this to your `settings.py`:

```python
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailOrUsernameBackend',  # your custom logic
    'django.contrib.auth.backends.ModelBackend',  # default fallback
]
```

- This means **when Django tries to log in a user (including admin)**, it will:
  1. First try your `EmailOrUsernameBackend`
  2. Then fall back to the default one if needed

So in the **admin login page**, you can enter either:

- A **username**, or
- An **email** — and it will work.

---

## ✅ How to Test Admin Email Login

1. Go to `/admin/`
2. Enter your **email** in the username field
3. Enter your correct password
4. 🎉 You should be logged in

> Because the form still says “username”, it’s just a label — the backend now accepts both.

---

## 🛠 Optional Improvement: Rename Label to “Username or Email”

If you want the admin login form to say **“Username or Email”**:

### In `accounts/admin.py`, override the login template:

1. Create a template:  
   `templates/admin/login.html`

2. Copy the default admin template and just change this line:
   ```html
   <label for="id_username">Username or Email:</label>
   ```

That’s optional, purely cosmetic.

---

## ✅ Summary

- Yes, admin login now works with **email or username**
- You don’t need to modify the admin form
- The login field label is “username”, but your backend makes it smart

Let me know if you want to fully customize the admin login form or style it!
