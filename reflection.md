# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|1      | Too low go Higher | Go lower instead| Same error after new game|
|100    | Too high go lower | Go Higher instead| Same error after new game |
|101    | Out of bound.     | Go Higher instead| No error message if you pick a number higher thn 100|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project, I use Claude to explain the logic step by step.
- Give one example of an AI suggestion that was correct (including what the AI
suggested and how you verified the result).

I tried to ask claude to explain the update_score function step by step and what it
does line by line. I found out that the function lowers your score on wrong guesses
and awards a speed-bonus on a win. There are 2 glitches the %2 quirk that randomly
rewards a too high guess and the second glitch attempt_number + 1 in the win bonus.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I asked to fix the backwards hints and it suggest me to swap the labels "too high"
to "too low" and vice versa in check_guess, and the hints will be correct." I found
out that was wrong answer since fliping the outcome label would then break the 
tests-test_guess_too_high expects check_guess(60,50) == "Too High", and swapping the
labels makes it return "Too Low" instead. The real bug was in the message text("Go
Higher!" vs "Go Lower!") at app.py line 37-40, not the outcome labels. The labels
were already correct. I figured that out after i ran pytest after the swap 
test_guess_too_high and test_guess_too_low both failed, which showed the AI fixed
the wrong half of the function
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed only when an automated test asserted the correct output 
for a known input and passed. I moved the game logic into logic_utils.py so it could 
be tested without launching Streamlit, then ran pytest. A bug was "really fixed" 
when the test that targets it went green and stayed green alongside the others.

- Describe at least one test you ran (manual or using pytest)  and what it showed you about your code.

I wrote test_win_on_first_attempt_scores_90, which calls update_score(0, "Win", 1) 
and asserts it returns 90. This targets the off-by-one score bug: the original code 
computed 100 - 10 * (attempt_number + 1), so a first-attempt win scored 80 instead 
of 90. Before the fix this test would fail (got 80, expected 90); after removing the 
extra + 1 it passes. Running python3 -m pytest tests/ -v showed all 6 tests passing, 
including the three provided check_guess tests and my three update_score tests.

- Did AI help you design or understand any tests? How?
Yes. I used Claude Code to explain app.py lines 14–64 step by step, which is how I understood the three bugs inverted hint message, the int-vs-string secret mismatch, and the off by one score. It also pointed out that the provided test in tests/
test_game_logic.py expected check_guess to return a bare outcome string like "Win", 
not a outcome, message tuple So it helped me design the refactor to separate 
logic outcome from UI message, and suggested the update_score test cases 
first-attempt win, the 10 point floor that actually exercise the bug I fixed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A rerun re-runs the whole script on every interaction; session state is the small
box of things you ask Streamlit not to forget between those reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
Separating logic from the UI so it can be tested. We moved the game functions out of
app.py into logic_utils.py, which let me run pytest on them without launching
Streamlit. I want to keep this testing habit: before trusting a fix, write a test
that asserts the correct output for a known input (like update_score(0, "Win", 1) 
== 90) and confirm it passes. A green test convinced me a bug was fixed far more
than just reading the code did.
- What is one thing you would do differently next time you work with AI on a coding task?
I'd ask the AI to write a failing test before applying the fix, instead of fixing
first and testing after. That way I'd actually watch the test go from red to green,
which proves the test catches the bug rather than just passing by coincidence. I'd
also be more careful not to claim I ran a test until I really had.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code can look clean and "production-ready" while quietly hiding logic
bugs like the inverted hint and the off-by-one score. I now treat AI output as a
draft to verify with my own tests, not as a finished answer.