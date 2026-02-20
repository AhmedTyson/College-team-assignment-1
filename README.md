# College Team Assignment — 1

> A Python console-based food delivery simulator inspired by Talabat — demonstrating OOP principles through collaborative team development.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-blueviolet?style=for-the-badge)
![Team Project](https://img.shields.io/badge/Type-Team_Assignment-green?style=for-the-badge)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Usage Example](#-usage-example)
- [Getting Started](#-getting-started)

---

## Overview

**Talabat Console Simulator** is a command-line application that mimics the core experience of a food and grocery delivery platform. Developed as a collaborative team assignment, the project applies Object-Oriented Programming concepts — classes, encapsulation, and method design — to model a real-world ordering workflow: user registration, restaurant browsing, cart management, payment, and receipt generation.

The project was built to practice version control collaboration and OOP design in a team context.

---

## ✨ Features

| Feature                 | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| **User Registration**   | Collects name, email, phone, address, and password with validation   |
| **Category Selection**  | Choose between Food or Groceries as a first-level filter             |
| **Restaurant Browsing** | Explore menus from multiple restaurants and stores                   |
| **Cart Management**     | Add items, update quantities, and remove items before checkout       |
| **Order Summary**       | Breakdown of subtotal, delivery fee, and service fee                 |
| **Payment Options**     | Choose Visa or Cash on Delivery                                      |
| **Receipt Generation**  | Timestamped receipt with order number, restaurant, and customer info |
| **Session Continuity**  | Place multiple orders in a single run without re-registering         |

---

## 💻 Tech Stack

| Layer            | Technology                  |
| ---------------- | --------------------------- |
| **Language**     | Python 3.x                  |
| **Paradigm**     | Object-Oriented Programming |
| **Interface**    | Command-Line (Console)      |
| **Dependencies** | Standard Library only       |

---

## 🏗️ Architecture

```
Talabat.py
├── User               # Registration, login, address management
├── Category           # Food / Groceries selection
├── Restaurant         # Menu listing and item management
├── Cart               # Add, remove, update items
├── Order              # Checkout, fee calculation, order number
└── Receipt            # Formatted order summary with timestamp
```

---

## 🖥️ Usage Example

```
Welcome To Talabat
Enter Your Full Name: John Doe
Enter Your Email: johndoe@gmail.com
Enter Your Password (minimum 8 characters): ********
Registration Successful! Welcome, John Doe!

Categories:
  1. Food
  2. Groceries
Choose the category (1-2): 1

Restaurants:
  1. Papa John's
  2. Heart Attack Grill
Choose an option: 1

The Menu:
  1. Hot & Spicy Pizza      EGP 149
  2. Pepperoni Classic      EGP 135

Enter item to add (0 to finish): 1
Enter quantity: 2

Your Cart:
  Hot & Spicy Pizza x2 — 298.0 EGP

Payment Summary:
  Subtotal:     298.0 EGP
  Delivery Fee:  20.0 EGP
  Service Fee:   14.9 EGP
  Total:        332.9 EGP

** Receipt **
  Order #1234 | Papa John's | 2025-06-01 12:34:56
  Thank you, John Doe!
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed ([Download](https://www.python.org/downloads/))
- No external libraries required

### Run

```bash
# Clone the repository
git clone https://github.com/AhmedTyson/College-team-assignment-1.git

# Navigate to the directory
cd College-team-assignment-1

# Run the simulator
python Talabat.py
```
