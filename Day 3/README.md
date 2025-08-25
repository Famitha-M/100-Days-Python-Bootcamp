Day 3: Conditionals and Control Flow in Python
📋 Overview
Day 3 introduces conditional statements in Python, teaching how to make decisions in code based on different conditions.
We'll explore if/else statements, comparison operators, logical operators, and practical applications like building a pizza ordering system and a text-based adventure game.

🎯 Learning Objectives
Understand and implement conditional statements (if/elif/else)
Master Python's indentation system for code blocks
Use comparison and logical operators effectively
Apply modulo operator for remainder calculations
Build practical applications using conditional logic

📖 Core Concepts
1. Conditional Statements
Python uses conditional statements to make decisions in code:
# Basic if/else structure
if condition:
    # Execute if condition is True
else:
    # Execute if condition is False

# Example
if pigs_can_fly:
    print("Magic!")
else:
    print("This is real life")

2. Python Indentation
Python uses indentation (whitespace) to define code blocks:
if 5 > 2:           # Parent line
    print("yes")    # Child line (must be indented)
   
4. Comparison Operators
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to

4. Modulo Operator
Returns the remainder of a division operation:
6 % 2    # 0
6 % 5    # 1
10 % 3   # 1 (PAUSE 1 Answer)

5. Nested and Multiple If Statements
# Nested if statements
if condition1:
    if condition2:
        # Both conditions must be true
        
# Multiple if statements
if condition1:
    # Code block
if condition2:
    # Code block (independent of condition1)

6. Logical Operators
and: Both conditions must be true
or: At least one condition must be true
not: The condition must be false


🍕 Practical Projects
1. Python Pizza Order System
Build an automatic pizza order program with the following pricing:
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Pepperoni for small: +$2
Pepperoni for medium/large: +$3
Extra cheese: +$1

Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.

