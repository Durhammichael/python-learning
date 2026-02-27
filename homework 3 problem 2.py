temp = int(input("Enter the temperature in fahrenheit: "))

rain_input = input("Is it raining? (yes/no): ").lower()

raining = rain_input == "yes"

if temp > 100:
    print("Extreme Heat Warning: stay indoors!")
elif temp > 85 and raining:
    print("warm rain watch for flash floods")
elif temp > 85 and not raining:
    print("It's hot outside, stay hydrated!")  
elif 60 <= temp <= 85 and raining:
    print("It's a nice day, but take an umbrella just in case.")
elif 60 <= temp <= 85 and not raining:
    print("It's a pleasant day, enjoy!")
elif temp < 60 and raining:
    print("It's cold and wet, bundle up!")
else:
    print("It's cold outside, dress warmly!")