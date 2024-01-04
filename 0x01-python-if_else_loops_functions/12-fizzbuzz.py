#!/usr/bin/python3
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz", end=" ")
        continue
    elif i % 3 == 0:
        print("Fizz", end=" ")
        continue
    elif i % 5 == 0:
        if i == 100:
            print("Buzz")
        print("Buzz", end=" ")
        continue
    print(f"{i}", end=" ")    
