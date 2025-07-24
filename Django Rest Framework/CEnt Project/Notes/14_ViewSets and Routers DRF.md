In **Django REST Framework (DRF)**, **ViewSets** and **Routers** are tools that simplify and automate the creation of API endpoints. They work together to reduce boilerplate and make your API more concise and maintainable.

---

### 🔹 ViewSets

A **ViewSet** is a class-based abstraction that **combines the logic for multiple views** (e.g., list, retrieve, create, update, delete) into a **single class**.

Instead of writing separate views for `GET`, `POST`, `PUT`, `DELETE`, you define all of them in one place.

#### Common ViewSets:

- `ViewSet`: base class — you define all actions manually.
- `ReadOnlyModelViewSet`: includes only `list` and `retrieve`.
- `ModelViewSet`: includes `list`, `retrieve`, `create`, `update`, `partial_update`, and `destroy`.

#### Example:

```python
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

This class now handles:

- `GET /products/` → list
- `GET /products/1/` → retrieve
- `POST /products/` → create
- `PUT /products/1/` → update
- `PATCH /products/1/` → partial update
- `DELETE /products/1/` → destroy

---

### 🔹 Routers

A **Router** automatically maps ViewSets to **URL patterns** without needing to write them manually.

#### Example:

```python
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
```

This automatically creates:

```
/products/            -> list
/products/<id>/       -> retrieve, update, delete
```

---

### 🔸 Summary

| Feature   | ViewSet                           | Router                          |
| --------- | --------------------------------- | ------------------------------- |
| Purpose   | Combine multiple views in one     | Auto-generate URL patterns      |
| Benefit   | Less duplication                  | No need to manually define URLs |
| Used With | `ModelViewSet`, `ReadOnlyViewSet` | `DefaultRouter`, `SimpleRouter` |

---

### Optional: Customizing ViewSet Actions

You can override methods like:

```python
def list(self, request):
    ...

def create(self, request):
    ...
```

Or add custom actions:

```python
from rest_framework.decorators import action

class ProductViewSet(ModelViewSet):
    ...

    @action(detail=False, methods=['get'])
    def featured(self, request):
        products = Product.objects.filter(is_featured=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
```

Now `/products/featured/` becomes a valid endpoint.

---

Let me know if you want an example with nested routers, permissions, or filtering.
