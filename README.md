# 🛒 Advanced Shopping Cart CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Tests](https://img.shields.io/badge/Tests-Passing-success)
![Status](https://img.shields.io/badge/Status-Active-blue)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)
![CLI](https://img.shields.io/badge/Interface-Command--Line-informational)
![Repo Size](https://img.shields.io/github/repo-size/crispusomollo/Advanced-Shopping-Cart-CLI)
![Last Commit](https://img.shields.io/github/last-commit/crispusomollo/Advanced-Shopping-Cart-CLI)
[![Build](https://github.com/crispusomollo/Advanced-Shopping-Cart-CLI/actions/workflows/tests.yml/badge.svg)](https://github.com/crispusomollo/Advanced-Shopping-Cart-CLI/actions/workflows/tests.yml)
[![Coverage Status](https://codecov.io/gh/crispusomollo/Advanced-Shopping-Cart-CLI/branch/main/graph/badge.svg)](https://codecov.io/gh/crispusomollo/Advanced-Shopping-Cart-CLI)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
[![CodeQL](https://github.com/crispusomollo/Advanced-Shopping-Cart-CLI/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/crispusomollo/Advanced-Shopping-Cart-CLI/actions/workflows/codeql-analysis.yml)
![Dependabot](https://img.shields.io/badge/Dependabot-Automated%20Updates-blue?logo=dependabot)

---

## 📘 Overview

The **Advanced Shopping Cart CLI** is a Python-based command-line shopping system designed for learning and experimentation.
It simulates a real-world shopping experience with inventory management, cart operations, and user session tracking — all from your terminal.

This project demonstrates:
- File-based persistence using JSON
- Modular design and object-oriented structure
- Unit testing and error handling
- A colorful CLI interface using `termcolor`

---

## ⚙️ Features

✅ Multi-user sessions
✅ Add, remove, and view items in cart
✅ Checkout with total calculation
✅ Persistent storage using JSON
✅ Input validation and error handling
✅ Clean and colorized CLI experience

---

## 🧰 Technologies Used

- **Language:** Python 3.10+
- **Libraries:**
  - `termcolor` – for colorized terminal output
  - `json` – for local data storage
  - `unittest` – for automated testing

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/chrisorigi/Advanced-Shopping-Cart-CLI.git
cd Advanced-Shopping-Cart-CLI
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Run the Application
```
python3 shopping_cart_multi.py
```

🧪 Testing

The project includes automated tests for cart logic, user management, and helper utilities.

▶️ Run All Tests
```
python3 -m unittest discover -s tests
```

✅ Example Output
........
----------------------------------------------------------------------
Ran 8 tests in 0.45s

OK


If you see OK, it means all tests passed successfully 🎉

## 🧰 Test Files Overview
```
File    Purpose
tests/test_cart.py      Tests helper utilities, data handling, and inventory setup
tests/test_multi.py     Tests user sessions, cart operations, and checkout logic
```

## 🗂️ Project Structure
```
Advanced-Shopping-Cart-CLI/
│
├── shopping_cart_multi.py     # Main CLI application
├── data/
│   ├── inventory.json          # Inventory data
│   ├── users.json              # User session data
│   └── carts.json              # User cart data
├── tests/
│   ├── test_cart.py            # Unit tests for helper functions
│   └── test_multi.py           # Unit tests for main logic
├── requirements.txt
├── LICENSE
└── README.md
```

## 🧑‍💻 Example CLI Session
=== Advanced Shopping Cart CLI ===
1. View Inventory
2. Add Item to Cart
3. View Cart
4. Checkout
5. Exit

Enter your choice: 1
Available Inventory:
- Apple (Groceries): 50 KES
- Bread (Bakery): 80 KES
- Milk (Dairy): 60 KES

Enter your choice: 2
- Enter item name: Apple
- Enter quantity: 3
✅ Added 3 Apple(s) to your cart!

Enter your choice: 4
🧾 Checkout Summary:
- Apple x3 = 150 KES
💰 Total: 150 KES
Thank you for shopping with us!

# 🤝 Contributing

Contributions are welcome!
If you’d like to improve features, fix bugs, or extend the project (e.g., Flask API version), feel free to:

- Fork the repository
- Create a new branch (feature/your-feature-name)
- Commit your changes
- Push and submit a Pull Request


# 🧾 License

This project is licensed under the MIT License — see the LICENSE
 file for details.


## 🌟 Future Enhancements

- 🧩 Flask-based Web API version
- 🗃️ SQLite/MySQL data persistence
- 🧠 Recommendation engine for frequently bought items
- 🧾 Receipt generation in PDF/CSV


Developed with ❤️  by Crispus Omollo

“Learning Python, one project at a time.” 🐍
