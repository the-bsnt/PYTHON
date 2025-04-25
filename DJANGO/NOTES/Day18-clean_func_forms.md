Use of message module in django
message.success
message.error;

---

In Django, the `messages` framework is used to temporarily store messages in one request and retrieve them for display in a subsequent request—commonly after a redirect. It is often used for showing success, error, or informational messages to users.

Here's a quick breakdown of how to use `messages.success`, `messages.error`, and other message levels in Django.

---

### ✅ **Setup (Usually Already Done)**

Make sure `'django.contrib.messages'` is included in your `INSTALLED_APPS`, and middleware includes `'django.contrib.messages.middleware.MessageMiddleware'`.

Your `settings.py` should look like:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.messages',
]

MIDDLEWARE = [
    ...
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

### 📦 **Usage in Views**

Import the messages module:

```python
from django.contrib import messages
```

Then, use it in your views like this:

```python
from django.shortcuts import redirect
from django.contrib import messages

def my_view(request):
    # On success
    messages.success(request, 'Your profile was updated successfully.')

    # On error
    messages.error(request, 'There was an error updating your profile.')

    # Redirect or render template
    return redirect('some-view-name')
```

Other message types include:

- `messages.debug(request, 'This is a debug message.')`
- `messages.info(request, 'This is an info message.')`
- `messages.warning(request, 'This is a warning message.')`

---

### 💻 **Display Messages in Template**

In your template (e.g., `base.html` or a specific page):

```html
{% if messages %}
<ul class="messages">
  {% for message in messages %}
  <li class="{{ message.tags }}">{{ message }}</li>
  {% endfor %}
</ul>
{% endif %}
```

You can style messages using CSS classes that match the tags (`success`, `error`, `warning`, etc.).

---

### 🎨 Example with Bootstrap (Optional)

If you’re using Bootstrap, you can easily integrate:

```html
{% if messages %} {% for message in messages %}
<div
  class="alert alert-{{ message.tags }} alert-dismissible fade show"
  role="alert"
>
  {{ message }}
  <button
    type="button"
    class="btn-close"
    data-bs-dismiss="alert"
    aria-label="Close"
  ></button>
</div>
{% endfor %} {% endif %}
```

---

what is cleaned_data in form

---

In Django, `cleaned_data` is a dictionary that holds **validated** form input data after `is_valid()` is called on a `Form` or `ModelForm`.

---

### ✅ **How it works**

When you submit a form and call `.is_valid()`:

```python
form = MyForm(request.POST)
if form.is_valid():
    name = form.cleaned_data['name']
```

Here's what happens:

1. Django runs validation on each field.
2. If the form is valid, `form.cleaned_data` is populated with cleaned (i.e., validated and possibly converted) Python values.
3. You can access your safe, cleaned values using standard dictionary syntax.

---

### 🔍 Example

```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# views.py
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Use cleaned data (e.g., save to DB, send email)
```

---

### 🧹 What “Cleaned” Means

- String inputs are stripped of leading/trailing whitespace.
- Email is validated to be a valid format.
- Integer fields are converted from strings to Python `int`.
- Custom `clean_fieldname()` or `clean()` methods are applied.

---

```python
def clean_discount(self):
        try:
            discount = self.cleaned_data["discount"]
            if int(discount) > 100:
                raise forms.ValidationError('Discont cannot be more then 100%')
            if int(discount) < 0 :
                raise forms.ValidationError('Discount cannot be in negative')
        except Exception as e:
            raise forms.ValidationError(e)
        return discount
```

You're on the right track with the `clean_discount` method in your Django form! This is a **field-specific validation** method, and Django will automatically call it when validating the form.

Let’s walk through what your function does, and then I’ll suggest a cleaned-up version with minor improvements.

---

### ✅ **What This Does**

- It gets the `discount` value from `cleaned_data`.
- It checks if `discount` is more than 100 or less than 0.
- If either condition is true, it raises a `ValidationError`.
- If all checks pass, it returns the cleaned `discount`.

---

### ⚠️ **Possible Issues**

- You're using `try/except`, but if the key `"discount"` isn't in `cleaned_data`, that usually means the field already failed earlier validation.
- Catching `Exception` broadly isn't necessary unless you're doing something risky (e.g., typecasting).

---

### ✅ **Improved Version**

```python
def clean_discount(self):
    discount = self.cleaned_data.get("discount")

    if discount is None:
        return discount  # Let Django handle required field errors

    if discount > 100:
        raise forms.ValidationError("Discount cannot be more than 100%.")

    if discount < 0:
        raise forms.ValidationError("Discount cannot be negative.")

    return discount
```

---

### 💡 Tips

- If `discount` is defined as a `forms.IntegerField`, no need to cast it using `int()`.
- Use `.get()` to avoid a KeyError if the field fails earlier validation.
- Don't catch general exceptions unless truly needed—let Django’s built-in validators do their thing first.

---

```python
class DebitForm(forms.ModelForm):
    class Meta:
        model = Debit
        fields = ["amount", "date"]
        widgets = {

            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
                "id": "date",
                "value": now().date(),
            }),
        }

    def clean_amount(self):
        amount = self.cleaned_data["amount"]

        if amount < 0:
            raise forms.ValidationError("Amount Cannot be in Negative")

        return amount
```

---

### why clean_amount function need to return amount , give example use view function of it??

Great question!

### 🔁 Why `clean_amount` must return `amount`

In Django form validation, when you define a method like `clean_amount()`, Django **expects you to return the cleaned (validated) value** at the end of the method. If you don't return it, Django won't include that field in `form.cleaned_data`, which means you won't be able to access it later in your view — or worse, the form won't save properly.

---

### 📦 Your `clean_amount` is perfect:

```python
def clean_amount(self):
    amount = self.cleaned_data["amount"]
    if amount < 0:
        raise forms.ValidationError("Amount Cannot be in Negative")
    return amount  # This is required
```

If you don’t return `amount`, Django assumes the field is invalid or missing, even if it passed all checks.

---

### 🧾 Example View Function Using `DebitForm`

Here’s how your form might be used in a view:

```python
from django.shortcuts import render, redirect
from .forms import DebitForm

def add_debit(request):
    if request.method == "POST":
        form = DebitForm(request.POST)
        if form.is_valid():
            debit = form.save()  # cleaned_data['amount'] is used here
            # You can also access the value directly if needed:
            # amount = form.cleaned_data['amount']
            return redirect('debit_list')  # or wherever you want
    else:
        form = DebitForm()

    return render(request, "debit_form.html", {"form": form})
```

---

### 🧠 In Summary:

- You **must return** the cleaned value from `clean_<field>()` methods.
- If not returned, Django treats the field as missing/invalid.
- That value is then accessible via `form.cleaned_data['amount']` and used in `.save()`.

---

### clean \_field () method is used to specially custom validate the input given by user. this method is defiened inside form model ???

Exactly! You nailed the concept — let me just clean up and expand your sentence for clarity and correctness:

---

### ✅ Refined Explanation

The `clean_<fieldname>()` method in Django is used to **apply custom validation to a specific form field**. It is defined **inside a Django `Form` or `ModelForm` class** and is automatically called by Django when `form.is_valid()` is invoked.

---

### 🧪 Example

```python
class DebitForm(forms.ModelForm):
    class Meta:
        model = Debit
        fields = ["amount", "date"]

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount < 0:
            raise forms.ValidationError("Amount cannot be negative.")
        return amount
```

This will:

- Automatically validate the `amount` field.
- Raise a validation error if the value is negative.
- Ensure that only valid data reaches `form.cleaned_data`.

---

Would you like me to explain how to write a `clean()` method for **validating across multiple fields** too?

### YES

Great! Let's talk about the general `clean()` method in Django forms — it's used when you need to **validate multiple fields together** (i.e., cross-field validation).

---

### ✅ What is `clean()` in Django Forms?

- The `clean()` method is a special method inside a `Form` or `ModelForm` that is called **after all individual field validations** (including `clean_<fieldname>()`).
- It’s used when the validation logic depends on more than one field.

---

### 🧪 Example: Validate That `end_date` Is After `start_date`

```python
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()  # Always call the parent method
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be before start date.")
```

---

### 💡 Key Points

- Use `cleaned_data.get('field')` to safely access values.
- Always call `super().clean()` first — it sets up `cleaned_data`.
- You can raise a `ValidationError` with a **global message** or pass a dictionary to assign errors to specific fields.

```python
# Example of assigning error to specific field
raise forms.ValidationError({'end_date': "End date must come after start date."})
```

---

### cleaned_data is dictionary right . what it contains basically???

Yes — you're absolutely right!

### ✅ `cleaned_data` is a **dictionary** in Django forms.

It contains the **cleaned (i.e., validated and converted) data** from all the fields that passed validation after calling `form.is_valid()`.

---

### 🧠 What Does `cleaned_data` Contain?

It contains:

- Keys: the names of the form fields.
- Values: the cleaned and type-converted Python values for each field.

---

### 🧪 Example

Given this form:

```python
class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField()
    in_stock = forms.BooleanField(required=False)
```

And using it in a view:

```python
form = ProductForm({
    'name': 'Laptop',
    'price': '1500.00',
    'in_stock': 'on'
})

if form.is_valid():
    print(form.cleaned_data)
```

---

### 📦 Output of `cleaned_data`:

```python
{
    'name': 'Laptop',               # str
    'price': Decimal('1500.00'),   # Decimal (converted from string)
    'in_stock': True               # Boolean
}
```

---

### 🔁 Important Notes

- Fields that fail validation are **not included** in `cleaned_data`.
- If you’re in a `clean()` or `clean_<field>()` method, always use `.get('field')` to avoid `KeyError`.

---

Great question! Understanding the difference between `clean()` and `clean_<field>()` in Django forms is essential for proper validation. Here's a clear breakdown:

---

### ✅ `clean_<field>()`

- Used to **validate a specific field only**.
- Runs **after the field’s built-in validation** (e.g., required, type, max_length).
- Must return the cleaned (valid) value.
- Method name follows the pattern: `clean_<fieldname>`

#### 🧪 Example:

```python
class MyForm(forms.Form):
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old.")
        return age
```

---

### ✅ `clean()`

- Used to **validate multiple fields together** (cross-field validation).
- Runs **after all field-specific validation** (including `clean_<field>()`).
- Operates on `self.cleaned_data`, which contains all the cleaned values.
- You can raise form-wide errors or assign errors to specific fields.

#### 🧪 Example:

```python
class MyForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
```

---

### 🔁 Summary Table

| Feature      | `clean_<field>()`                 | `clean()`                                 |
| ------------ | --------------------------------- | ----------------------------------------- |
| Validates    | One specific field                | Multiple fields together                  |
| When it runs | After field’s default validation  | After all fields are individually cleaned |
| Return value | Must return the cleaned value     | Returns nothing (modifies `cleaned_data`) |
| Useful for   | Field-level rules (e.g., min age) | Cross-field rules (e.g., match passwords) |

---

Sure! You can use a `clean_username()` method with a regular expression (`regex`) to validate the format of a username in Django.

---

### 🎯 **Goal:**

Let's say you want the username to:

- Only contain **letters**, **numbers**, **underscores**.
- Be at least **4 characters** long.
- Not start with a number.

---

### ✅ `clean_username()` with Regex

```python
import re
from django import forms

class UserForm(forms.Form):
    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]

        # Regex: Must start with a letter or underscore, then allow letters, numbers, underscores
        pattern = r'^[A-Za-z_][A-Za-z0-9_]{3,}$'

        if not re.match(pattern, username):
            raise forms.ValidationError(
                "Username must start with a letter or underscore, be at least 4 characters long, and contain only letters, numbers, or underscores."
            )

        return username
```

---

### 🧪 Explanation of Regex:

```regex
^              # Start of string
[A-Za-z_]      # First character must be a letter or underscore
[A-Za-z0-9_]{3,}  # At least 3 more characters (total 4+), any letter/number/underscore
```

---

Exactly — you're absolutely right!

### ✅ `clean()` in Django forms **does not return anything**.

Instead, it works by:

- Calling `super().clean()` to initialize and populate `self.cleaned_data`
- Optionally modifying `self.cleaned_data`
- Raising `ValidationError` if needed

---

### 📌 Why it doesn’t return anything?

Because Django internally uses `self.cleaned_data` for further processing. You don’t return it — you just update or validate it.

---

### 🧪 Example (Validating Email & Confirm Email)

```python
class EmailForm(forms.Form):
    email = forms.EmailField()
    confirm_email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')

        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Emails do not match.")
```

✔️ **No `return` statement is needed.**

---
