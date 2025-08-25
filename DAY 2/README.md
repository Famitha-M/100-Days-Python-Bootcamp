# Day 2 – Python Basics
Data Types: Strings, Integers, Floats, Booleans

TypeError: These errors occur when you are using the wrong data type. Example: len(12345) (works only on strings). Fix: len("12345")

Type Checking: You can check the data type of any value or variable in python using the type() function.
print(type("abc")) # <class 'str'>
print(type(123))   # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type(True))  # <class 'bool'>

Type Conversion: Convert data into different data types using int(), float(), str().
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

Basic Operators: +, -, *, /, //, ** | PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 3 + 3 / 3 - 3) # Output: 7.0
print(3 * 3 / 3) # Output: 3.0

Flooring a Number: int(3.738492) # 3
Rounding a Number: round(3.738492) # 4, round(3.14159) # 3, round(3.14159, 2) # 3.14

Assignment Operators: +=, -=, *=, /=
x = 5
x += 3 # 8

f-Strings: age = 12; print(f"I am {age} years old") # Output: I am 12 years old

Tip Calculator: If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay: (150.00 / 5) * 1.12 = 33.6
After formatting to 2 decimal places = 33.60
