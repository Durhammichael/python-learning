
temp = float(input("Enter temperature: "))

scale = input("Enter scale (C/F): ").strip().upper()

if scale == "C":
    converted = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {converted:.1f}°F")

elif scale == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {converted:.1f}°C")

else:
    
    print("Invalid scale.")