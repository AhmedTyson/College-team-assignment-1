import datetime # To Generate the Date
import random   # To Generate the Random Order Number
# Declaring the Menus and Prices:
# Restaurants Menus
papa_johns_menu=["Hot & spicy pizza EGP 149","Chicken ranch pizza EGP 179","Shrimp ranch pizza EGP 184","Super papas EGP 149"]
papa_johns_prices = [149.0, 179.0, 184.0, 149.0]

heart_attack_menu=["Single mix EGP 210","Combo wrap EGP 120","French fries EGP 45","Coleslaw EGP 40","Rezetto EGP 65"]
heart_attack_prices = [210.0, 120.0, 45.0, 40.0, 65.0]

pizza_king_menu=["Combo mix crust EGP 478","King chicken pizza EGP 231","Chicken BBQ pizza EGP 319","Potato wedges EGP 55"]
pizza_king_prices = [478.0, 231.0, 319.0, 55.0]

elabd_menu=["Chocolate croissant EGP 38","Italian pizza EGP 39","Orange cake large EGP 170","Mini sandwich EGP 100","pink donut EGP 35"]
elabd_prices= [38.0, 39.0, 170.0, 100.0, 35.0]

bazooka_menu=["Onion rings EGP 35","Appetizers happiness EGP 120","Mozzarella sticks EGP 50","Bazooka golden snack box EGP 155"]
bazooka_prices = [35.0, 120.0, 50.0, 155.0]

# Stores Menus
bim_menu=["Atyab chicken strips EGP 95","Cooking cream EGP 95","Corona chocolate EGP 12","Puvana EGP 97","Face tissues EGP 59"]
bim_prices = [95.0, 95.0, 12.0, 97.0, 59.0]

mahmoud_elfar_menu=["Deep melt chocolate EGP 131","Almarai cheese spread EGP 194","Danone yoghurt EGP 68","Bubbly hand wash EGP 38"]
mahmoud_elfar_prices = [131.0, 194.0, 68.0, 38.0]

abu_auf_menu=["Cocoa drink bundle EGP 320","Hot chocolate bundle EGP 220","Abu Auf mixed nuts EGP 270","popcorn parmesan cheese EGP 25"]
abu_auf_prices=[320.0,220.0,270.0,25.0]

talabat_mart_menu=["Fresh Farm beef hotdog EGp 46","Juhayna vanilla pudding EGP 100","Tiger excellence premium EGP 15","Brunch toast EGP 33"]
talabat_mart_prices = [46.0, 100.0, 15.0, 33.0]

carrefour_menu=["Temmys corn flakes EGP 70","Break coffee EGP 35","Italiano pasta EGP 34","Dream jelly EGP 25","Cracks chips EGP 10"]
carrefour_prices = [70.0, 35.0, 34.0, 25.0, 10.0]

# Declaring the Cart Items, Prices, and Quantities
cart_items = []
cart_prices = []
cart_quantities = []

# Process 1: Registration 
def register():
  print("Welcome To Talabat")
  full_name = input("Enter Your Full Name: ")

  # Loop until valid Email is provided
  while True: 
    email = input("Enter Your Email: ")
    if not (email.endswith("@gmail.com")): # Check if the email ends with @gmail.com
        print("Enter a valid email, Email must end with @gmail.com")
        continue  
    break

  # Loop until valid Password is provided
  while True:
    password = input("Enter Your Password (minimum 8 characters) : ")
    if len(password) < 8: # Check if the password is at least 8 characters long
      print("Password is too short. It must be at least 8 characters long.")
      continue
    break
  
  # Loop until Passwords Match  
  while True:
    confirm_password =input("Re-enter Your Password to confirm it (minimum 8 characters) : ")
    if password != confirm_password: # Check if the passwords match
      print("Passwords do not match. Please try again.")
      continue
    break
    # Loop until valid Phone Number is provided
  while True:
    phone = input("Enter your Phone Number: ")
    if not phone.isdigit() or len(phone) < 10 or len(phone) > 11: # Check if the phone number is not a number or is not between 10 and 11 digits
        print("Enter a Valid Phone Number")
        continue
    break
  # Loop until valid Username is provided
  while True:
    username = input("Enter Your Username: ")
    if len(username) < 5 or len(username) > 15: # Check if the username is not between 5 and 15 characters long
      print("Username must be between 5 and 15 characters long. Please try again.")
      continue
    break

  address = input("Enter Your Address: ")
  #Welcome Message
  print("----------------------------------")
  print("Registration Successful!")
  print(f"Welcome, {full_name}!")
  print("----------------------------------")
  return [full_name, username, email, phone, address] # Return a list containing the user's information

# Process 2 : Display Category
def display_category():
  categories = ["Food", "Groceries"] 
  while True:
    print("Categories:")
    for i in range(len(categories)):
      print(f"{i+1}. {categories[i]}")
    print("----------------------------------")
    choice = int(input("Choose the category (1-2): "))
    if choice <= 0 or choice > len(categories): 
      print("Invalid Number. Choose from 1 to 2\n")
      print("----------------------------------")
      continue
    break
  print(f"You selected: {categories[choice -1]}")
  print("----------------------------------")
  selected_category = categories[choice -1]
  return selected_category 

# Process 3: Display Display_restaurants_shops 
def display_restaurants_shops(selected_category):
  restaurants = ["Papa John's", "Heart Attack", "Pizza King", "El Abd", "Bazooka"]
  stores = ["BIM", "Mahmoud ELFar","Abu Auf","Talabat Mart","Carrefour"]

  if selected_category == "Food":
    print("Restaurants:")
    for i in range(len(restaurants)):
      print(f"{i+1}. {restaurants[i]}")
    # Loop until valid restaurant option is selected
    while True:
      print("---------------------------------------")
      choice = int(input("Choose an option (1-5): "))
      if choice <= 0 or choice > len(restaurants): 
        print("Invalid input. Please choose a valid restaurant.")
        print("------------------------------------------------")
        continue
      break
    print(f"You selected: {restaurants[choice - 1]}") 
    print("-----------------------------------------")
    selected_restaurant_store = restaurants[choice - 1]

  elif selected_category == "Groceries":
    print("Stores:")
    for i in range(len(stores)):
      print(f"{i+1}. {stores[i]}")
    print("----------------------------------")
    # Loop until valid store option is selected
    while True:
      choice = int(input("Choose an option (1-5): "))
      if choice <= 0 or choice > len(stores):
        print("Invalid input. Please choose a valid Store.")
        print("----------------------------------")
        continue
      break
    print(f"You selected: {stores[choice - 1]}")
    print("-------------------------------------")
    selected_restaurant_store = stores[choice - 1]
  return selected_restaurant_store # Return the selected restaurant or store

# Process 4: Display Menu 
def display_menu(selected_restaurant_store): 
    print("The Menu: ")
    if selected_restaurant_store== "Papa John's":   
      for i in range(len(papa_johns_menu)):
        print(f"{i+1}. {papa_johns_menu[i]}")

    elif selected_restaurant_store=="Heart Attack":
      for i in range(len(heart_attack_menu)):
        print(f"{i+1}. {heart_attack_menu[i]}")

    elif selected_restaurant_store=="Pizza King":
      for i in range(len(pizza_king_menu)):
        print(f"{i+1}. {pizza_king_menu[i]}")

    elif selected_restaurant_store=="El Abd":
      for i in range(len(elabd_menu)):
        print(f"{i+1}. {elabd_menu[i]}")

    elif selected_restaurant_store == "Bazooka":
      for i in range(len(bazooka_menu)):
        print(f"{i+1}. {bazooka_menu[i]}")

    elif selected_restaurant_store=="BIM":
      for i in range(len(bim_menu)):
        print(f"{i+1}. {bim_menu[i]}")

    elif selected_restaurant_store=="Mahmoud ELFar":
      for i in range(len(mahmoud_elfar_menu)):
        print(f"{i+1}. {mahmoud_elfar_menu[i]}")

    elif selected_restaurant_store=="Abu Auf":
      for i in range(len(abu_auf_menu)):
        print(f"{i+1}. {abu_auf_menu[i]}")

    elif selected_restaurant_store=="Talabat Mart":
      for i in range(len(talabat_mart_menu)):
        print(f"{i+1}. {talabat_mart_menu[i]}")

    elif selected_restaurant_store=="Carrefour":
      for i in range(len(carrefour_menu)):
        print(f"{i+1}. {carrefour_menu[i]}")
    print("----------------------------------")

# Process 5: Add to Cart 
def add_to_cart(selected_restaurant_store):
  # Loop until the user finishes adding items
  while True:
    choice = int(input("Enter the number of the item you'd like to add to your cart (or 0 to finish): "))
    if choice == 0:
      break
    elif choice <= 0 or choice > 5:
      print("Invalid choice. Please try again.")
      continue
    quantity = int(input("Enter the quantity: ")) 
    if quantity <= 0:
      print("Invalid quantity. Please try again.")
      continue

    if selected_restaurant_store== "Papa John's":
      cart_items.append(papa_johns_menu[choice - 1]) 
      cart_prices.append(papa_johns_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = papa_johns_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {papa_johns_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")

    elif selected_restaurant_store=="Heart Attack": 
      cart_items.append(heart_attack_menu[choice - 1])
      cart_prices.append(heart_attack_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = heart_attack_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {heart_attack_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")

    elif selected_restaurant_store=="Pizza King":
      cart_items.append(pizza_king_menu[choice - 1])
      cart_prices.append(pizza_king_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = pizza_king_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {pizza_king_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")  

    elif selected_restaurant_store=="El Abd":
      cart_items.append(elabd_menu[choice - 1])
      cart_prices.append(elabd_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = elabd_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {elabd_menu[choice - 1]} added to your cart. Item total: {item_total} EGP") 

    elif selected_restaurant_store=="Bazooka":
      cart_items.append(bazooka_menu[choice - 1])
      cart_prices.append(bazooka_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = bazooka_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {bazooka_menu[choice - 1]} added to your cart. Item total: {item_total} EGP") 

    elif selected_restaurant_store=="BIM":
      cart_items.append(bim_menu[choice - 1])
      cart_prices.append(bim_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = bim_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {bim_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")   

    elif selected_restaurant_store=="Mahmoud ELFar":
      cart_items.append(mahmoud_elfar_menu[choice - 1])
      cart_prices.append(mahmoud_elfar_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = mahmoud_elfar_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {mahmoud_elfar_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")   

    elif selected_restaurant_store=="Abu Auf":
      cart_items.append(abu_auf_menu[choice - 1])
      cart_prices.append(abu_auf_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = abu_auf_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {abu_auf_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")   

    elif selected_restaurant_store=="Talabat Mart":
      cart_items.append(talabat_mart_menu[choice - 1])
      cart_prices.append(talabat_mart_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = talabat_mart_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {talabat_mart_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")  

    elif selected_restaurant_store=="Carrefour":
      cart_items.append(carrefour_menu[choice - 1])
      cart_prices.append(carrefour_prices[choice - 1])
      cart_quantities.append(quantity)
      item_total = carrefour_prices[choice - 1] * quantity
      print("---------------------------------------------------------------")
      print(f"{quantity}x {carrefour_menu[choice - 1]} added to your cart. Item total: {item_total} EGP")

    print("You can continue adding more items or type '0' to checkout.")
    print("---------------------------------------------------------------")

# Process 6: View Cart
def view_cart():
  if len(cart_items) == 0: # Check if the cart is empty
    print("Your cart is empty.")
    return

  while True:
    #Displaying Cart
    print("-----------------------------------------------------------------")
    print("Your Cart:")
    for i in range(len(cart_items)):
      print(f"{i + 1}. {cart_items[i]} | Quantity: {cart_quantities[i]} | Total Price: {cart_prices[i] * cart_quantities[i]} EGP")
    # Calculate Payment Summary
    subtotal = 0
    for i in range(len(cart_items)):
      subtotal += cart_prices[i] * cart_quantities[i]

    delivery_fee = 20.0
    service_fee = round(subtotal * 0.05, 2)  
    total_amount = subtotal + delivery_fee + service_fee
    payment_summary =[subtotal, delivery_fee, service_fee, total_amount] # A list to store all payment details
    print("---------------------------------")
    print("Payment Summary:")
    print(f"Subtotal: {subtotal} EGP")
    print(f"Delivery Fee: {delivery_fee} EGP")
    print(f"Service Fee: {service_fee} EGP")
    print(f"Total Amount: {total_amount} EGP")
    print("---------------------------------")

    print("Options:")
    print("1. Update Quantity")
    print("2. Remove Item")
    print("0. Check out")
    choice = int(input("Enter your choice (1-2) or (0 To check out): "))
    if choice == 1:
      item_index = int(input("Enter the item number to update: "))
      if 1 <= item_index <= len(cart_items):
        new_quantity = int(input("Enter the new quantity: "))
        cart_quantities[item_index - 1] = new_quantity
        print("----------------------------------------------------------------")
        print(f"Quantity for {cart_items[item_index - 1]} updated successfully.")
      else:
        print("Invalid item number.")
        continue


    elif choice == 2:
      item_index = int(input("Enter the item number to remove: "))
      if 1 <= item_index <= len(cart_items):
        print("----------------------------------------------------------------")
        print(f"{cart_items[item_index - 1]} removed from cart successfully.")
        cart_items.pop(item_index - 1)
        cart_prices.pop(item_index - 1)
        cart_quantities.pop(item_index - 1)
      else:
        print("Invalid item number.")
        continue

    elif choice == 0:
      break
    else:
      print("Invalid choice. Please try again.")
      continue
  return payment_summary 

# Process 7: Checkout
def checkout(user_data):
  print("---------------------------------------------------------------")
  print("** Checkout **")
  print(f"Address: {user_data[4]}")
  print(f"Phone: {user_data[3]}")
  print("----------------------------------")
  # Loop until a valid payment method is selected
  while True:
    payment_choice=int(input("choose a payment method (1 for Visa , 2 for Cash ):"))
    if payment_choice==1:
      payment_method = "Visa"

    elif payment_choice==2:
      payment_method = "Cash"
    else:
      print("Invalid choice)")  
      continue
    break
  print("----------------------------------")
  return payment_method

# Process 8: Place Order
def display_receipt(user_data, selected_restaurant_store, payment_method, payment_summary):
  print("Your Order is placed , It will be delivered within one hour Maximum.")
  print("------------------------------------------------------------------")
  print("** Receipt **")  
  print(f"Restaurant: {selected_restaurant_store}")
  print(f"Date :{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  print(f"Order Number: {random.randint(1000, 9999)}") 
  print(f"Customer Name: {user_data[0]}")
  print(f"Address: {user_data[4]}") 
  print(f"Phone: {user_data[3]}")
  print("Items:")
  for i in range(len(cart_items)):
    print(f"{i + 1}. {cart_items[i]} | Quantity: {cart_quantities[i]} | Total Price: {cart_prices[i] * cart_quantities[i]} EGP")
  print(f"Subtotal: {payment_summary[0]} EGP")
  print(f"Delivery Fee: {payment_summary[1]} EGP")
  print(f"Service Fee: {payment_summary[2]} EGP")
  print(f"Total Amount: {payment_summary[3]} EGP")
  print(f"Payment Method: {payment_method}")
  print("Thank you for your order!")

# Main program flow 
user_data = register()
while True:
  selected_category = display_category()
  selected_restaurant_store = display_restaurants_shops(selected_category)
  display_menu(selected_restaurant_store)
  add_to_cart(selected_restaurant_store)
  payment_summary=view_cart()
  payment_method=checkout(user_data)
  display_receipt(user_data, selected_restaurant_store, payment_method, payment_summary)
  print("-------------------------------------------------")
  choice = input("Do you want to place another order? (yes/no): ")
  if choice.lower() != "yes":
    break 