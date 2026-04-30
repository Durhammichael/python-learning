# FizzBuzz Problem 1
for x in range(1, 31):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

# Times Table Pattern problem 2
for n in [
          [1, 2, 3, 4, 5, 6,],
          [2, 4, 6, 8, 10, 12,],
          [3, 6, 9, 12, 15, 18,],
          [4, 8, 12, 16, 20, 24,],
          [5, 10, 15, 20, 25, 30,],
          [6, 12, 18, 24, 30, 36]
          ]:
    print(end=" ")
    print(n)


        
