# College-team-assignment-1

## Talabat App (Console Version)

A simple Python console-based application that mimics the Talabat food and grocery delivery service. Users can register, explore restaurants or stores, add items to their cart, and place orders with an auto-generated receipt.

---

## Features

- **User Registration:** Collects name, email, phone number, address, and secures with password confirmation.
- **Category Selection:** Choose between Food or Groceries.
- **Restaurant/Store Browsing:** Explore menus from popular restaurants and stores.
- **Cart Management:** Add, update quantities, or remove items from your cart.
- **Order Summary:** Detailed breakdown including subtotal, delivery, and service fees.
- **Checkout Options:** Select payment via Visa or Cash.
- **Receipt Generation:** Displays order number, restaurant name, customer info, and timestamp.
- **Session Continuity:** Users can place multiple orders in a single session.

---

## Usage Examples

### Run the Application

```bash
python Talabat.py
````

### Follow the Prompts

```text
Welcome To Talabat
Enter Your Full Name: John Doe
Enter Your Email: johndoe@gmail.com
Enter Your Password (minimum 8 characters): ********
Re-enter Your Password to confirm it: ********
Enter your Phone Number: 01234567890
Enter Your Username: johndoe123
Enter Your Address: 123 Main St
Registration Successful!
Welcome, John Doe!
----------------------------------
Categories:
1. Food
2. Groceries
Choose the category (1-2): 1
You selected: Food
----------------------------------
Restaurants:
1. Papa John's
2. Heart Attack
...
Choose an option (1-5): 1
You selected: Papa John's
The Menu:
1. Hot & spicy pizza EGP 149
...
Enter the number of the item you'd like to add to your cart (or 0 to finish): 1
Enter the quantity: 2
2x Hot & spicy pizza EGP 149 added to your cart. Item total: 298.0 EGP
...
Your Cart:
1. Hot & spicy pizza EGP 149 | Quantity: 2 | Total Price: 298.0 EGP
...
Payment Summary:
Subtotal: 298.0 EGP
Delivery Fee: 20.0 EGP
Service Fee: 14.9 EGP
Total Amount: 332.9 EGP
...
** Receipt **
Restaurant: Papa John's
Date: 2025-06-01 12:34:56
Order Number: 1234
Customer Name: John Doe
...
Thank you for your order!
```

---

## Requirements

* Python 3.x

---

## License

This project is for educational purposes only.

