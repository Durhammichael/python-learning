a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))


expr1 = a < b < c
expr2 = not (a > b or b > c)
expr3 = a <= b and b <= c

print("Expression 1 (a < b < c):", expr1)
print("Expression 2 (not (a > b or b > c)):", expr2)
print("Expression 3 (a <= b and b <= c):", expr3)

if expr2 == expr3:
    print("\nDe Morgan's law confirmed: not (a > b or b > c) is equivalent to a <= b and b <= c")
else:    print("\nDe Morgan's law not confirmed: not (a > b or b > c) is not equivalent to a <= b and b <= c")