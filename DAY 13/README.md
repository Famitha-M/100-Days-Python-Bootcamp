# Day 13 – Debugging

### 📌 Describe the Problem
Some bugs are sneaky—they only appear under certain conditions.  
To fix them you must first **understand what’s happening**, then **reproduce** the bug so you can diagnose it.

---

### 🐞 Reproduce Bugs
- Try to **trigger the error consistently** so you can observe when and why it happens.  
- Knowing the exact conditions lets you narrow down the root cause.

---

### ✅ Fix Errors (Red Lines)
- **Red underlines** in the editor are actual errors that will stop your code.  
- **Yellow warnings** are optional: they may lead to problems later or may just be the editor not fully understanding your code.

---

### 🛡️ Catching Exceptions
Use a `try/except` block to prevent crashes when user errors or unexpected situations occur.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That’s not a valid number!")

