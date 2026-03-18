USD, EUR, and GBP are all different currencies. To convert between them, you can use the following exchange rates:
1 USD = float(0.92 EUR)
1 USD = float(0.79 GBP)
1 EUR = float(1.09 USD)
1 EUR = float(0.86 GBP)
1 GBP = float(1.27 USD)
1 GBP = float(1.16 EUR)
print(int(input("how much money do you have? "))
print("is this USD, EUR, or GBP?")
currency = input("enter the currency: ")
if currency == "USD":
    print("you have", int(input("how much money do you have? ")) * 0.92, "EUR")
    print("you have", int(input("how much money do you have? ")) * 0.79, "GBP")
elif currency == "EUR":
    print("you have", int(input("how much money do you have? ")) * 1.09, "USD")
    print("you have", int(input("how much money do you have? ")) * 0.86, "GBP")
elif currency == "GBP":
    print("you have", int(input("how much money do you have? ")) * 1.27, "USD")
    print("you have", int(input("how much money do you have? ")) * 1.16, "EUR")
else:
    print("invalid currency")
