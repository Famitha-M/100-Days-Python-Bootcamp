# Day 12 - Scope & Number Guessing Game  

## 1. Namespaces and Scope  

### Local Scope  
- Variables (or functions) declared inside functions have **local scope**.  
- They are only visible inside that function.  

### Global Scope  
- Variables declared at the top level (outside functions) have **global scope**.  
- They can be accessed anywhere in the file.  

### Python and Block Scope  
- Unlike some other programming languages, Python **does not have block scope**.  
- Variables created inside loops, if statements, etc. do not get block scope.  
- They are given function scope (if inside a function) or global scope (if not).  

---

## 2. Global Variables  

- By default, you cannot modify global variables inside a function.  
- Use the `global` keyword to modify a global variable inside a function.  

---

## 3. Global Constants  

- **Global constants** are values defined once and never meant to change.  
- Commonly written in **ALL_CAPS** with underscores.  
- Example usage: PI, API keys, URLs, etc.  

---

## 4. Project: Number Guessing Game  

### Game Rules  
1. Computer randomly selects a number between 1 and 100.  
2. Player has to guess the number.  
3. Player chooses difficulty:  
   - **Easy** → 10 attempts  
   - **Hard** → 5 attempts  
4. The program should give hints:  
   - “Too high”  
   - “Too low”  
   - “Correct!”  

---

### Steps to Build  
1. Create a function to check guesses against the chosen number.  
2. Keep track of the number of attempts left.  
3. Loop until the player guesses correctly or runs out of attempts.  
4. Add difficulty selection (easy or hard).  
5. Add the game logo from `art.py`.  

---

## 5. Learning Outcome  
- Understanding **local vs global scope**.  
- Using **global constants** effectively.  
- Building a **fully interactive game** using conditionals, loops, and functions.  
