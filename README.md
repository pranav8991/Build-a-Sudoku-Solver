# 😎 Project: Build a Sudoku Solver 🎯

## Welcome to my Sudoku Solver Extravaganza! 🎉🧠

In this project, I set out on a heroic quest to extend a humble Sudoku-solving agent into a **diabolically** difficult **diagonal Sudoku solver**. But wait, there’s more! I also learned the mystical art of **Naked Twins** 👫 [Click Here](https://www.sudokudragon.com/guidenakedtwins.htm)
. Yes, that’s right — *Naked Twins*, because apparently Sudoku needed to sound a little more scandalous! 

So grab your calculators (you won’t need them) and prepare to be amazed by my Pythonic wizardry. 🧙‍♂️🐍

---

## Introduction 🧐

In this project, you will extend the Sudoku-solving agent developed in the classroom lectures to solve **diagonal Sudoku puzzles**. A diagonal Sudoku puzzle is like traditional Sudoku but with the added twist that numbers on the **two main diagonals** must also contain unique digits from 1 to 9. 😱

### I also implemented the **Naked Twins** strategy — trust me, it’s more exciting than it sounds. 🤓

---

## Solver Functionality 💪

| Criteria                               | Submission Requirements                                                                                                                                                  |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 👫 Naked Twins Implemented Correctly    | **(AUTOGRADED)** The student cleverly deploys constraint propagation to solve the Naked Twins problem by enforcing that no squares outside the two Naked Twins can contain the same values. 💃🕺 |
| ➕ Diagonal Sudoku Implemented Correctly | **(AUTOGRADED)** The solver successfully incorporates the diagonal constraint, ensuring the diagonals play nicely with the rows, columns, and blocks. Because everyone should get along. 😇|

---

## How I Survived the Project 🚀

### Step 1: Setup the Doom Environment 🏗️

As all good programmers know, the journey of 1,000 bugs begins with a single command. So, I started by creating my **conda environment** and downloading the project files.

```bash
(aind) $ git clone https://github.com/udacity/artificial-intelligence.git
```

What could possibly go wrong? 😅 Well, after a few attempts (and realizing my Wi-Fi was slower than a snail 🐌), I was finally ready to dive in!

---

### Step 2: Solving Sudoku – The Easy Part (Ha, Yeah Right 😬)

At first glance, Sudoku seems simple: place the numbers 1 through 9 in all the right places. What could be easier, right? WRONG. After battling my initial setup and looking at the code, I realized I had stumbled into a war zone of logic puzzles. 🧩

---

### Step 3: Conquering the Diagonals 🔀

Next, I unleashed the power of **constraint propagation** to solve **diagonal Sudoku**. What’s that, you ask? Well, it's when you convince the diagonals to behave themselves by using the same set of rules as the rows and columns. 🎯

```python
def apply_diagonal_constraints():
    # I might have screamed at the screen a little here
    pass
```

*What I felt*: "I am Sudoku’s master."
*Reality*: "Why are there 32 errors in my code?!" 😱

---

### Step 4: Entering the Naked Twins 👫💥

Now, let’s talk about **Naked Twins**. Not as scandalous as it sounds, but equally dangerous in the Sudoku world. These sneaky twins only have two possible values, and they like to mess up everyone else's plans. So I had to tell the rest of the numbers: "Sorry guys, these values are taken!" ✋

```python
def naked_twins(values):
    # All hail the Naked Twins! 👯‍♂️
    for boxA in values:
        for boxB in PEERS[boxA]:
            # If they match and are only 2 digits long, we found the twins 👀
            if values[boxA] == values[boxB] and len(values[boxA]) == 2:
                for peer in PEERS[boxA] & PEERS[boxB]:
                    values[peer] = values[peer].replace(values[boxA][0], '')
                    values[peer] = values[peer].replace(values[boxA][1], '')
```

---

### Step 5: Testing (aka The Moment of Truth 😬)

I nervously typed the command to run my unit tests. Was this the moment I would achieve coding glory or face utter failure?

```bash
(aind) $ python -m unittest -v
```

**Expectation**: 🎉 Green dots of victory.
**Reality**: ❌ Red lines of doom.

BUT WAIT! After hours of debugging, I finally saw the **green light** of success. All tests passed. **ALL TESTS PASSED!** 🎊🎉🙌

---

## How to Run This Beauty of a Solver 👩‍💻

Wanna take my Diagonal Sudoku Solver for a spin? Here’s what you need to do:

1. Clone this repo:
   ```bash
   git clone <this-repo-url>
   ```
   
2. Activate the **aind** environment:
   ```bash
   conda activate aind
   ```

3. Navigate to the project folder:
   ```bash
   cd Projects/1_Sudoku
   ```

4. Run the solver with test cases:
   ```bash
   python -m unittest -v
   ```

---

## Conclusion 🏁

In conclusion, building this Sudoku solver has been a wild ride filled with bugs, breakthroughs, and far too many coffee breaks. ☕ If you want a taste of victory, or simply want to make your friends believe you're a Sudoku wizard, feel free to download and play with the solver. 😎

##Just remember — even the mightiest programmers start with baby steps (and occasional tantrums). And hey, sometimes those baby steps mean seeking help from fellow coders, dissecting their code, and piecing together solutions. So yes, I’ve had my fair share of peeking into others' projects, learning from their work, and figuring out how things tick. It’s all part of the journey. So, maff kar do muja if I borrowed an idea or two along the way—because, in the end, it’s about growing and improving. 😅

---

## License ⚖️

This project is released under the “Don’t Take My Code Too Seriously” License, because let’s face it, I had fun with this. 😆 Feel free to fork, share, and add your own flavor of chaos to the solver! 

---
