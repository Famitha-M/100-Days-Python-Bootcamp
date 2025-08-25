# Day 4 - Randomisation & Lists in Python

## Pseudorandom Number Generators
- Computers are not truly random because they are built with circuits and switches.  
- Randomness is important in software, especially in games.  
- Pseudorandom Number Generators (PRNG) are algorithms that simulate randomness.  
- Example: [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)  
- Recommended resource: [Khan Academy video](https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs)  

## The Random Module in Python
- Python provides a `random` module to generate random values.  
- Documentation: [Python Random Module](https://docs.python.org/3/library/random.html)  

### Random Whole Numbers
- Generate random integers within a specified range (inclusive).  

### Random Floats
- Generate floating-point numbers between `0.0` and `1.0`.  
- Multiply to expand range, e.g., `0 to 5`.  
- `uniform(a, b)` generates random floating numbers between `a` and `b` (inclusive).  

### Modules in Python
- Code can be organised into separate `.py` files (modules).  
- Use `import` to access variables or functions from another file.  

---

## Lists in Python
- A **list** is a collection of ordered items.  
- Example: list of fruits or states of America.  

### Accessing Items
- Access items by index (starting from `0`).  
- Negative indices allow access from the end of the list.  

### Modifying Items
- Items in a list can be reassigned using indices.  

### Adding Items
- Use `append()` to add new items to a list.  

### Length of List
- Use `len()` to get the number of items in a list (or characters in a string).  

### IndexError
- Occurs when trying to access an index outside the valid range of a list.  

### Nested Lists
- Lists can contain other lists (2D lists).  
- Example: fruits list + vegetables list combined.  

---

## Mini Projects & Challenges
- **Heads or Tails** → Simulate a coin flip.  
- **Random Name Picker** → Select a random name from a list of friends.  
- **Rock, Paper, Scissors** → Build a simple game using randomisation and lists.  

---

## Additional Resources
- [Python Random Module Documentation](https://docs.python.org/3/library/random.html)  
- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)  
- [Built-in Functions: len()](https://docs.python.org/3/library/functions.html#len)  
