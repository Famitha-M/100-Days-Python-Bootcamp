# Day 7 - Hangman Game Project

Your goal is to build a Hangman game using everything you have learnt about Python programming.  

**Demo Final Project:**  
[Play Here](https://appbrewery.github.io/python-day7-demo/)  

The project is split into major steps. Each step has multiple TODOs that guide you to build the game.  

---

## Step 1 - Basic Setup

### TODO-1  
Randomly choose a word from the `word_list` and assign it to a variable called `chosen_word`. Then print it.  

---

### TODO-2  
Ask the user to guess a letter and assign their answer to a variable called `guess`.  
Make the String stored in `guess` lowercase.  

---

### TODO-3  
Check if the letter the user guessed (`guess`) is one of the letters in the `chosen_word`.  
Loop through each of the letters in the `chosen_word` and print **"Right"** if the letter is a match, **"Wrong"** if it’s not.  

---

## Step 2 - Create Placeholders

### TODO-1  
Create an empty String called `placeholder`.  
For each letter in the `chosen_word`, add a `_` to `placeholder`.  
Example: If the word is `apple`, the placeholder should be `_ _ _ _ _`.  

---

### TODO-2  
Create an empty string called `display`.  
Loop through each letter in the `chosen_word`:  
- If the letter at that position matches `guess`, reveal that letter in the display at that position.  
- Otherwise, put `_`.  

Example: If the user guessed "p" and the word is `apple`, the display should be `_ p p _ _`.  

---

## Step 3 - Keep Guessing

### TODO-1  
Use a **while loop** to let the user guess again.  
The loop should only stop once the user has guessed all the letters in the `chosen_word`.  
When no blanks ("_") remain, the user wins.  

---

### TODO-2  
Update the for loop so that **previous guesses are stored**.  
Currently, a new guess replaces old progress.  
Fix this by storing matched letters and re-using them in the display.  

---

## Step 4 - Add Lives

### TODO-1  
Create a variable called `lives` to keep track of the number of lives left.  
Set `lives = 6`.  

---

### TODO-2  
If the guessed letter is **not in the chosen_word**, reduce lives by 1.  
If lives reach 0, end the game with **"You lose."**  

---

### TODO-3  
Print the ASCII art from the list `stages` that corresponds to the current number of lives.  

---

## Step 5 - Enhancements & Modules

### TODO-1  
Update the word list to use the `word_list` from **hangman_words.py**.  

---

### TODO-2  
Update the code to use the `stages` from **hangman_art.py**.  

---

### TODO-3  
Import the `logo` from **hangman_art.py** and print it at the start of the game.  

---

### TODO-4  
If the user has entered a letter they’ve already guessed, print the letter and let them know.  
⚠️ Do not deduct a life.  
Example:  
