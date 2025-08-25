# Day 10 - Functions with Outputs and Building a Calculator Program

## Functions with Outputs
- Functions can not only execute code but also **return values**.
- `return` sends a result back to the caller, unlike `print` which only displays it.
- Once a `return` is executed, the function terminates.

### Key Notes
- Functions can have **multiple return statements** when using conditional logic.
- An **empty return** (`return` without a value) simply exits the function.
- Returned values can be reused in further calculations.

## Title Case Example
- Use `.title()` method to format text inputs (e.g., names) into Title Case.
- Practice writing functions that both take inputs and return properly formatted results.

## Docstrings
- Write **multi-line comments** with triple quotes `"""`.
- When placed directly below a function definition, they serve as **documentation**.
- Docstrings appear when hovering over the function, acting as reminders of its purpose.

## Storing Functions as Variables
- Functions in Python can be stored in variables and passed around like data.
- This allows flexible execution and dynamic program design.

## Building a Calculator Program
- The program should support **addition, subtraction, multiplication, and division**.
- Use a **dictionary** to map mathematical operators (`"+", "-", "*", "/"`) to their corresponding functions.
- Perform calculations by retrieving the correct function from the dictionary.

### Calculator Flow
1. Ask the user for the **first number**.
2. Ask for the **operator** (`+`, `-`, `*`, `/`).
3. Ask for the **second number**.
4. Perform the calculation using the dictionary of operations.
5. Display the result.
6. Ask if the user wants to **continue with the previous result** or start fresh.
7. Loop until the user decides to stop.

## Additional Notes
- Add a **logo** from `art.py` for program branding.

