# Day 5 - Python Loops and Password Generator

## Loops
Loops allow us to tell the computer to repeat actions without having to write repeated code.  
For example, instead of typing `print()` statements for numbers 1 through 100, we can create a loop to do this automatically.

### Syntax
for <variable> in <a List>:
<do something>
<do something else>


---

## Indentation
Indentation is very important in Python. Whenever you see the `:` symbol, the code that follows must be indented properly. Incorrect indentation changes program behavior.

---

## Sum
Python provides a built-in function `sum()` to calculate totals.  
Behind the scenes, this works by looping through each number and adding them together.  

Similarly, Python also provides:
- `max()` → gives the highest value
- `min()` → gives the lowest value

### Challenge: Max Score
Without using the `max()` function, write a program that prints the highest score from a list of exam scores.  

Example:  
Input → `8 65 89 86 55 91 64 89`  
Output → `91`

---

## Range Function
The `range()` function is often combined with loops to repeat actions a set number of times.  

For example:  
`range(1, 10)` → generates numbers from **1 to 9** (start inclusive, end exclusive).  

---

## Challenge: The Gauss Problem
Work out the total of the numbers between **1 and 100**, inclusive of both ends.  

---

## Project: Password Generator
The program will ask:
1. How many letters would you like in your password?  
2. How many symbols would you like?  
3. How many numbers would you like?  

Using these inputs, generate a random password.

### Easy Version
Generate the password in sequence (letters → symbols → numbers).  
Example: `fgdx$*924`

### Hard Version
Shuffle the characters so that letters, numbers, and symbols appear in random order.  
Example: `x$d24g*f9`

---

## Key Skills Practiced
- For Loops  
- Indentation Rules  
- Using `sum()`, `max()`, and `min()`  
- Range with Loops  
- Problem Solving with Loops and Lists  
- Random Module for Password Generation  

---
