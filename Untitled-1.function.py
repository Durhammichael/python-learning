def greet(name="guest"):
    print(f"hello, {name}!")
greet("alice")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)

def register(first_name, last_name, age, email=""):
    print(f"{first_name} {last_name}, age {age}")
if email:
    print(f"Email: {email}")
register("michael", "durham", "20", email="michaeld05@gmail.com")


