**Token Authentication** in **Django REST Framework (DRF)** is one of the simplest ways to authenticate users via an API. Instead of using sessions or cookies (as in traditional Django), token authentication uses a token — a unique string assigned to each user.

---

### 🔑 **How Token Authentication Works**

1. **User logs in** using username and password.
2. **Server responds with a token** (if the credentials are valid).
3. **Client stores the token** (usually in localStorage or an HTTP header).
4. For subsequent requests, the client **sends the token in the `Authorization` header**:

   ```
   Authorization: Token <your_token>
   ```

5. DRF checks the token and authenticates the user accordingly.

---

### ✅ Setup Token Authentication in DRF

#### 1. **Install DRF**

```bash
pip install djangorestframework
```

#### 2. **Add `rest_framework` and `rest_framework.authtoken` to `INSTALLED_APPS`**

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```

#### 3. **Run migrations to create the token table**

```bash
python manage.py migrate
```

#### 4. **Create Token for existing users (optional)**

```bash
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='your_username')
token = Token.objects.create(user=user)
print(token.key)
```

#### 5. **Add token authentication to your settings**

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

#### 6. **Enable the endpoint to obtain token**

In your `urls.py`:

```python
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    ...
    path('api-token-auth/', obtain_auth_token),
]
```

#### 7. **Client sends token in headers**

```http
GET /api/some-protected-endpoint/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

---

### 🔒 Example View with Token Protection

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}"})
```

---

### 🔄 Token vs Session Auth

| Feature       | TokenAuth                | SessionAuth                   |
| ------------- | ------------------------ | ----------------------------- |
| Stateless     | ✅ Yes                   | ❌ No (uses cookies/sessions) |
| Best for      | APIs consumed by clients | Web apps with browsers        |
| CSRF Required | ❌ No                    | ✅ Yes                        |
| Storage       | Client stores token      | Server stores session         |

---

### ⚠️ Notes

- Token authentication is simple but **not the most secure for production**. Consider **JWT** or **OAuth2** for more robust use cases.
- Token can be leaked if not handled securely (e.g., stored in insecure client-side storage).

---

Would you like an example with `SimpleJWT` as well for comparison?
