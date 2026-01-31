# Simple Receipt Generator
customer_name: str = input("Enter Customer name: ")
quantity = int(input("Enter Quantity of item: "))
price_per_item = float(input("Enter price per item: $"))

Subtotal = quantity * price_per_item
tax = Subtotal * 0.07
total = Subtotal + tax

print("\n" + "="*30)
print("Reciept")
print("="*30)
print(f"Customer: {customer_name}")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price_per_item:.2f}")
print("-"*30)
print(f"Subtotal: ${Subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print("-"*30)
print(f"Total: ${total:.2f}")
print("="*30)
print("Thank you for your purchase!")
