# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 # each topping, any size
# ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
# Your code goes below this line.
# EXERCISE 1 — Display the size menu
# Your code here
ordering = True 
while ordering:    
    print("=" * 30)
    print("         PIZZA SIZES")
    print("=" * 30)

    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]:<15} ${size_prices[i]:>5.2f}")
    print("=" * 30)
    # EXERCISE 2 — Get a valid size choice
    # Your code here
    while True:
        choice = input('Pick a pizza size (1-4): ')
        if not choice.isdigit():
            print("Invalid input. Plese enter a number.")
            continue
        choice = int(choice)
        if choice < 1 or choice > 4:
            print('Invalid choice. Please enter a number between 1 and 4')
            continue 
        sizes_choice = choice - 1
        base_price = size_prices[sizes_choice]
        break
    print(f"you selected option {choice}.")
    # Exercise 3 -- Add Toppings
    # Your code here
    selected_toppings = []
    print("\n available toppings (1.50 each): ")
    for i in range(len(topping_names)):
        print(f"{i + 1}. {topping_names[i]}")
    while True:
        choice = input("add topping # (or done): ").lower()
        if choice == "done":
            break
        if not choice.isdigit():
            print("invalid input!")
            continue
        choice = int(choice)
        if choice < 1 or choice > len(topping_names):
            print("invalid topping number")
            continue 
        topping = topping_names[choice - 1]
        if topping in selected_toppings:
            print(f"already added {topping}")
            continue
        selected_toppings.append(topping)
        print(f"added {topping}")
    # Exercise 4 -- calculate prices
    # Your code here
    price = base_price + len(selected_toppings) * topping_price
    if selected_toppings:
        description = sizes[sizes_choice] + " " + ", ".join(selected_toppings)
    else:
        description = sizes[sizes_choice] + " cheese"
    order_descriptions.append(description)
    order_prices.append(price)
    # 
    while True:
        again = input("order another pizza? (yes/no):  ")
        if again in ["yes", "y"]:
            break
        elif again in ["no", "n"]:
            ordering = False
            break
        else:
            print("please enter yes or no")
if not order_descriptions:
    print("\n no pizzas ordered see you next time.")
else:
    discount = 0
    attempts = 0
    while attempts < 3:
        code = input("\n enter discount code ('or none'): ").upper()
        if code == "NONE":
            break
        elif code == "STUDENT10":
            discount = 0.10
            print("10% discount")
            break
        elif code == "MIKEYISAWESOME":
            discount = 0.50
            print("50% discount")
            break
        elif code == "ITISAWESOME":
            discount = 0.15
            print("15% discount")
            break
        else:
            attempts += 1
            print("invalid code, try again")
    if attempts >= 3:
        print("no discount applied")

    print("\n" + "=" * 30)
    print("YOUR ORDER RECEIPT")
    print( "=" * 30)
    subtotal = 0
    for i in range(len(order_descriptions)):
        print(f"{i + 1}. {order_descriptions[i]}")
        print(f"${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    tax_rate = 0.0825
    discount_amount = subtotal * discount
    tax_amount = subtotal * tax_rate
    total = subtotal - discount_amount + tax_amount

    print(f"\nSubtotal: ${subtotal:,.2f}")
    if discount > 0:
        print(f"Discount: -${discount_amount:,.2f}")
    print(f"Tax: ${tax_amount:,.2f}")
    print(f"Total: ${total:,.2f}")
    max_price = order_prices[0]
    max_index = 0
    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i
    print(f"\n most expensive pizza: {order_descriptions[max_index]} (${max_price:.2f})")
    size_counts = [0, 0, 0, 0]
    for desc in order_descriptions:
        for i in range(len(sizes)):
            if sizes[i] in desc:
                size_counts[i] += 1
    print("\n pizza count by size: ")
    for i in range(len(sizes)):
        print(f"{sizes[i]}: {size_counts[i]}")
    print("\n thank you for the order")