# Day 8 - Functions with Inputs & Caesar Cipher

## Functions with Inputs
- Functions can take inputs to modify behavior each time they are called.
- The variable inside the function definition is called a **parameter**.
- The value passed when calling the function is called an **argument**.

### Multiple Inputs
- Functions can accept multiple inputs by separating them with commas.

### Positional Arguments
- By default, arguments are assigned based on their position.

### Keyword Arguments
- Arguments can be passed with keywords to avoid confusion about order.

---

## Caesar Cipher - Part 1
- Build an encryption program using the Caesar cipher.
- **Steps**:
  - Create a function `encrypt()` with parameters `original_text` and `shift_amount`.
  - Loop through each character in the text.
  - Shift letters by the given amount.
  - Handle cases where shifting goes beyond `'z'`.
- Test the function with different inputs.

---

## Caesar Cipher - Part 2
- Create a function `decrypt()` to shift letters backward.
- Combine `encrypt()` and `decrypt()` into a single function `caesar()`.
- The function should:
  - Take direction (`encode` or `decode`), text, and shift.
  - Perform the operation accordingly.
  - Print encoded or decoded results.

---

## Caesar Cipher - Part 3
- Import and display a logo from `art.py` when program starts.
- Handle non-alphabet inputs (numbers, symbols, spaces) by keeping them unchanged.
- Add the ability to restart the program:
  - Ask if user wants to run again.
  - If "yes", request new inputs and rerun.
