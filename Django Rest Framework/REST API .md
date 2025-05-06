# REST API: An Overview

## What is a REST API?

A **REST API** (Representational State Transfer Application Programming Interface) is a way for computer systems to communicate over the internet using standard HTTP methods, typically in a stateless and scalable way.

### Key Concepts:

- **REST** is an architectural style, not a protocol or standard.
- **API** is a set of rules that allow one software program to interact with another.

### In a REST API:

- **Resources** are represented by URLs (e.g., `https://example.com/users`).
- **HTTP methods** are used to perform actions on resources.

## HTTP Methods in REST

- **GET**: Retrieve a resource or data
- **POST**: Create a new resource
- **PUT**: Update an existing resource
- **DELETE**: Remove a resource
- **PATCH**: Partial update of a resource

## Example Endpoints

API for managing users.

```
GET    /api/v1/users          - Get list of users
POST   /api/v1/users          - Create new user
GET    /api/v1/users/{id}     - Get specific user
PUT    /api/v1/users/{id}     - Update user
DELETE /api/v1/users/{id}     - Delete user
```

### and

Suppose you have an API for managing books:

- `GET /books` → Fetch all books
- `GET /books/1` → Fetch the book with ID 1
- `POST /books` → Add a new book
- `PUT /books/1` → Update book with ID 1
- `DELETE /books/1` → Delete book with ID 1

### NOTE: REST APIs usually return data in **JSON** or **XML** format.

## Key Characteristics

1. **Client-Server Architecture**: The client and servers are not depended to each other.
   In Traditional Web application, the html document is already rendered in Server Side (Server Side Scripting)
   and sent to Client Side in the form of HTTP response. With this, the Client is depended on Server.;
   For seperate client and servers, Server sends raw data in JSON format. With this Client fetches the raw data and build the page dynamically.
2. **Statelessness**: Each request contains all necessary information.
3. **Alwarys respect all the HTTP methods** ie. There are HTTP request methods such as GET, POST, PUT, PATCH, DELETE for specific purposes. Use them accordingly.

## Best Practices

1. Use nouns (not verbs) in endpoint paths (`/users` not `/getUsers`)
2. Use HTTP status codes appropriately (200, 201, 400, 404, 500, etc.)
3. Version your API (`/v1/users`)
4. Provide filtering, sorting, and pagination for collections
5. Use consistent naming conventions (camelCase or snake_case)
6. Implement proper error handling with meaningful messages
7. Secure your API with authentication (OAuth, JWT) and HTTPS

## Question?

## What i know is:

#### generally the server responds the browser with some data in the form of http response. that format might be html document. but server renders the html doc and send to the client side like django renders the html document and make it http response and respond to the browser.

Yes, you're absolutely right! What you described is how **traditional web applications** work — where the server renders full HTML pages and sends them to the browser as HTTP responses. Let me expand on that and show how it's different from REST APIs.

---

### ✅ Traditional Web App (e.g., Django with Templates)

- The **server renders HTML** using a template engine (like Django templates).
- The **browser (client)** receives a fully prepared HTML page and displays it.
- Example flow:

  1. Browser requests `/profile`.
  2. Django queries the database and renders `profile.html`.
  3. Django sends back an HTML document as the HTTP response.
  4. Browser displays it directly.

---

### 🔁 REST API

- The server **does not render HTML**. Instead, it sends **raw data**, usually in **JSON**.
- It's mostly used for **frontend-backend separation** or **mobile apps**, where the **frontend handles rendering** (e.g., React, Vue, Flutter).
- Example flow:

  1. Frontend requests `/api/profile` via `GET`.
  2. Backend (e.g., Django REST Framework) returns JSON:

     ```json
     {
       "username": "davidtim",
       "email": "david@example.com"
     }
     ```

  3. The frontend JavaScript code (like in React) takes that data and builds the page dynamically.

---

### 🧠 Key Differences

| Feature              | Traditional Django Views  | REST API (Django REST Framework etc.) |
| -------------------- | ------------------------- | ------------------------------------- |
| Response format      | HTML                      | JSON (or XML)                         |
| Rendering handled by | Server (Django templates) | Client (React, Android, etc.)         |
| Use case             | Web pages                 | Web/mobile apps, SPAs                 |
| Navigation           | Page reloads              | Dynamic updates via AJAX/fetch        |

---

## Question?

#### So, We build APIs so that the client which can be a browser, mobile app, or any device can get raw data from server side and use it accordingly

**And the API that follows restful architecture are RESTful APIs**

## ?

Exactly! You've got the idea spot on.

Here’s a refined summary of what you said:

---

### ✅ Why We Build APIs

We build **APIs** so that any **client**—whether it's:

- a **browser running JavaScript (like React)**,
- a **mobile app (iOS, Android)**,
- or even another **server or IoT device**—

can **request raw data** from a backend/server, and then use that data however it needs.

---

### 🌐 What Is a RESTful API?

An API is called **RESTful** if it follows the principles of **REST (Representational State Transfer)**. This includes:

- Using **standard HTTP methods** (`GET`, `POST`, `PUT`, `DELETE`)
- Having **resource-based URLs** (e.g., `/users/1`)
- Being **stateless** (each request contains all info needed)
- Returning **raw data**, often in **JSON format**
- Following **conventions** (like using plural nouns for resources: `/products`, `/orders`)

---

### 📱 Use Case Example

Let’s say you have a REST API that returns a list of products:

- A **React web app** fetches the products via:

  ```
  GET /api/products
  ```

  and shows them in a shopping grid.

- A **mobile app** fetches the **same API** and renders them in a list.

Both are using the **same backend API**, but rendering is handled on the **client side**.

---

## Question?

#### So can i build my backend apis using django and build my android app using flutter and fetch the data ?

Yes, absolutely! That's a great and modern tech stack.

You can build your **backend APIs using Django (especially Django REST Framework)** and then build your **mobile app using Flutter**, which will **fetch data from those APIs** over HTTP.

---

### 🔧 How It Works

#### 1. **Django REST Framework (DRF) Backend**

- You define endpoints like:

  - `GET /api/products/` – list of products
  - `POST /api/orders/` – create an order

- These endpoints return **JSON**.

#### 2. **Flutter Frontend (Mobile App)**

- Use `http` or `dio` package in Flutter to call your Django APIs.
- Parse the JSON response and use it to build the UI.

---

### 📱 Example Scenario

#### Django (API):

```python
# views.py using Django REST Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    data = [
        {'id': 1, 'name': 'Shoes', 'price': 49.99},
        {'id': 2, 'name': 'Bag', 'price': 29.99}
    ]
    return Response(data)
```

API URL: `http://yourserver.com/api/products/`

#### Flutter:

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> fetchProducts() async {
  final response = await http.get(Uri.parse('http://yourserver.com/api/products/'));

  if (response.statusCode == 200) {
    List products = jsonDecode(response.body);
    print(products);
  } else {
    throw Exception('Failed to load products');
  }
}
```

---

### ✅ Benefits of This Setup

- Clear **separation of concerns**: Django handles data and logic, Flutter handles UI.
- Highly **scalable**: You can reuse the same API for web, mobile, or even third-party apps.
- Great for learning **full-stack mobile development**.
