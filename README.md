# 📨 email-inspector

[![PyPI version](https://img.shields.io/pypi/v/email-inspector.svg)](https://pypi.org/project/email-inspector/)
[![Python versions](https://img.shields.io/pypi/pyversions/email-inspector.svg)](https://pypi.org/project/email-inspector/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/jahanviraycha/email-inspector/actions/workflows/python-package.yml/badge.svg)](https://github.com/jahanvir/email-inspector/actions)

**Detect free/public email provider domains (like Gmail, Yahoo, Outlook, etc.)**

`email-inspector` is a lightweight Python library that helps you identify whether an email address or domain belongs to a **free/public email provider** or a **custom business domain**.

---

## 🚀 Installation

```bash
pip install email-inspector
````

---

## 🧠 Usage

### 1. Check if an email is free/public

```python
from email_inspector.free_providers import is_free_email

print(is_free_email("john.doe@gmail.com"))   # True
print(is_free_email("ceo@company.com"))      # False
```

### 2. Check if a domain is free/public

```python
from email_inspector.free_providers import is_free_domain

print(is_free_domain("yahoo.com"))    # True
print(is_free_domain("mybiz.io"))     # False
```

### 3. Get the provider name

```python
from email_inspector.free_providers import get_provider

print(get_provider("john.doe@gmail.com"))   # "gmail"
print(get_provider("outlook.com"))          # "outlook"
```

### 4. (Optional) Check MX records for free mail hosts

> Requires `dnspython`

Install optional dependency:

```bash
pip install dnspython
```

Usage:

```python
from email_inspector.free_providers import mx_indicates_free

print(mx_indicates_free("gmail.com"))   # True
print(mx_indicates_free("company.org")) # False
```

---

## 📦 Data Source

The package includes a precompiled list of **16,000+ free email domains**.
This list is automatically updated twice a year via GitHub Actions (January 1st and July 1st).

---

## 🧑‍💻 Development

Clone and install locally for development:

```bash
git clone https://github.com/jahanvir/email-inspector.git
cd email-inspector
pip install -e .
pytest -q
```

---

## 🔁 Auto Updates

A GitHub Action runs every **January 1st** and **July 1st** to:

* Fetch the latest free email providers list
* Run tests
* Automatically bump the version and publish to PyPI if changes are detected

---

## 🧾 Example Output

| Function                           | Input     | Output |
| ---------------------------------- | --------- | ------ |
| `is_free_email("test@gmail.com")`  | ✅ True    |        |
| `is_free_email("ceo@startup.com")` | ❌ False   |        |
| `get_provider("user@yahoo.com")`   | `"yahoo"` |        |
| `mx_indicates_free("gmail.com")`   | ✅ True    |        |

---

## 📄 License

MIT License © 2025 [Jahanvi Raycha](mailto:raychajahanvi@gmail.com)

---

## ⭐ Support

If you find this package helpful, please consider **starring the repository** on GitHub 🌟
Your support helps keep the project maintained and updated!

👉 [GitHub Repository](https://github.com/jahanvir/email-inspector)

```

---
