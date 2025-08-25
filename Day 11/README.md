# Day 11 - Blackjack Capstone Project

## Game Difficulty Levels
- **Normal 😎**: Use all provided hints to complete the project.  
- **Hard 🤔**: Use only Hints 1, 2, 3.  
- **Extra Hard 😭**: Use only Hints 1 & 2.  
- **Expert 🤯**: Use only Hint 1.  

## Blackjack House Rules
1. The deck is **unlimited** in size.  
2. No jokers are used.  
3. **Jack, Queen, King** each count as **10**.  
4. **Ace** can count as **11 or 1**.  
5. Deck of cards:  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

6. All cards have **equal probability** of being drawn.  
7. Cards are **not removed** from the deck as they are drawn.  
8. The **computer is the dealer**.  

## Program Structure

### Step 1 - Setup
- Create a function `deal_card()` that returns a random card from the deck.
- Deal **2 cards each** to the user and computer at the start.

### Step 2 - Scoring
- Create a function `calculate_score(cards)` to sum up the card values.  
- Special rules:
- If the hand has **Ace + 10 (Blackjack)**, return `0` to represent Blackjack.  
- If the score is over 21 and an Ace (11) is present, convert Ace from **11 → 1**.  

### Step 3 - User Gameplay
- Check if the user or computer has Blackjack (score = 0). If yes, game ends.  
- If not, ask the user:  
- **Draw another card** → add new card to hand and recalculate score.  
- **Stop drawing** → game moves to computer’s turn.  

### Step 4 - Computer Gameplay
- The computer (dealer) keeps drawing cards until its score is **17 or higher**.  

### Step 5 - Compare Scores
Create a function `compare(user_score, computer_score)` with rules:
- If scores are equal → Draw.  
- If computer has Blackjack (0) → User loses.  
- If user has Blackjack (0) → User wins.  
- If user’s score > 21 → User loses.  
- If computer’s score > 21 → Computer loses.  
- Otherwise → Higher score wins.  

### Step 6 - Restart Option
- After finishing a game, ask the user if they want to play again.  
- If yes, clear the console and start a new game.  
- Display the **Blackjack logo** from `art.py` each time a new game starts.  

## Helpful References
- Try out the game online: [Washington Post Blackjack](https://games.washingtonpost.com/games/blackjack/)  
- Completed project demo: [Blackjack Demo](https://appbrewery.github.io/python-day11-demo/)  
- Requirement breakdown: [Listmoz Breakdown](http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF)  
- Flowchart (App Brewery): [Download Flowchart](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt)  
