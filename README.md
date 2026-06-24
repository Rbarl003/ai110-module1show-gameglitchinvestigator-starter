# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
A Streamlit number-guessing game: the app picks a secret number based on difficulty
(Easy 1–20, Normal 1–100, Hard 1–50), and the player has a limited number of
attempts to guess it, getting "higher/lower" hints and a score after each guess.
- [ ] Detail which bugs you found.
Glitch 1: "Too High" told the player to go HIGHER (and vice versa).
Glitch 2: the secret was cast to a string on every even attempt,
breaking the int-vs-string comparison so hints/results were wrong on those turns.
Glitch 3: a redundant `+ 1` made a first-attempt win score 80 instead
of 90.
- [ ] Explain what fixes you applied.
Backwards hints — "Too High" told you to guess higher (and the reverse), so you 
could never win. Now it points the right way: too high → go lower, too low → go 
higher.
The secret kept "changing" — every other guess, the code turned the secret number 
into text, so your number never matched it even when it was correct. Now the secret 
always stays a number, so a right guess actually wins.
Wrong score — a small math mistake made a first-try win worth 80 points instead of 90. Fixed the math so the score is correct.
## 📸 Demo Walkthrough

*Normal difficulty (1–100). Secret: **63**. Starting score: **0**.*
1. Guess **40** → "Too Low → 📈 Go HIGHER!" → score **−5**
2. Guess **70** → "Too High → 📉 Go LOWER!" → score **−10**
3. Guess **65** → "Too High → 📉 Go LOWER!" → score **−15**
4. Guess **63** → "🎉 Correct!" → win bonus `100 − 10×4 = 60` → final score **45**
5. Game ends, reveals the secret, and "New Game 🔁" resets for another round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
