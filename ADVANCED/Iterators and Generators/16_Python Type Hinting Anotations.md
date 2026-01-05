Python type hinting (introduced in Python 3.5) is a way to formally annotate your code to specify what data types your variables, function parameters, and return values should be.

While Python remains a **dynamically typed** language—meaning the interpreter won't stop your code from running if types are mismatched—type hints make your code significantly more readable, maintainable, and less prone to bugs.

---

## 1. Basic Syntax

The syntax uses a colon `:` for variables and parameters, and `->` for function return values.

```python
# Variables
age: int = 25
name: str = "Alice"

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}"

```

---

## 2. Using the `typing` Module

For more complex structures like lists or dictionaries, you’ll often use the built-in `typing` module (or standard collections in Python 3.9+).

### Common Types

| Type           | Example Syntax   | Description                                 |
| -------------- | ---------------- | ------------------------------------------- |
| **List**       | `list[int]`      | A list containing only integers.            |
| **Dictionary** | `dict[str, int]` | Keys are strings, values are integers.      |
| **Optional**   | `Optional[str]`  | The value can be a string **or** `None`.    |
| **Union**      | `int             | str`                                        |
| **Any**        | `Any`            | Opt out of type checking for this variable. |

---

## 3. Why Should You Use Them?

1. **Better IDE Support:** Tools like VS Code and PyCharm use these hints to provide superior autocompletion and "Intellisense."
2. **Static Analysis:** You can use a tool called **mypy** to check your code for type errors before you ever run it.
3. **Documentation:** Hints serve as "living documentation" that stays updated as the code changes.
4. **Refactoring:** It is much safer to rename or change objects when the IDE understands the relationships between types.

---

## 4. Advanced Annotations

### Type Aliases

If you have a complex type you use often, you can give it a name:

```python
Coordinate = tuple[float, float]

def move_to(point: Coordinate) -> None:
    print(f"Moving to {point}")

```

### Classes as Types

You can use your own classes as type hints:

```python
class User:
    def __init__(self, id: int):
        self.id = id

def get_user(user_id: int) -> User:
    return User(user_id)

```

---

## 5. Summary Table: Dynamic vs. Type Hinted

| Feature         | Dynamic (Standard Python)         | With Type Hinting                         |
| --------------- | --------------------------------- | ----------------------------------------- |
| **Errors**      | Caught at runtime.                | Caught during development (via IDE/Mypy). |
| **Readability** | "What does this function return?" | "This returns a `List[User]`."            |
| **Speed**       | No impact on execution speed.     | No impact on execution speed.             |

> **Note:** Type hints are ignored at runtime by the Python interpreter. They are purely for developer productivity and tooling.

---

Would you like me to show you how to set up **mypy** to automatically check for type errors in your current project?
