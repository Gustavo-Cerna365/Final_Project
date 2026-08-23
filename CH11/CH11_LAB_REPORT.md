# Lab Report — Chapter 11: Dynamic Programming


## Test Results


```
Part 1: Measure the waste
3
15
10
2040
18
332408

Part 2: Fill the grid instead
row 0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
row 1: [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
row 2: [0, 0, 3, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
row 3: [0, 0, 3, 4, 5, 7, 8, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
row 4: [0, 0, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 15, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]
row 5: [0, 0, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 15, 18, 18, 19, 20, 22, 23, 24, 25, 25, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28]
row 6: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 19, 20, 22, 23, 24, 25, 26, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]
row 7: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 26, 28, 29, 30, 31, 32, 33, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]
row 8: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44]
row 9: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 53, 53, 53, 53, 53]
row 10: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 11: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 12: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 13: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 14: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 15: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 16: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 17: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 18: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 19: [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58]
row 20: [0, 2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59]
Best value (DP, all 20 items):
59

Naive call count (18 items):
332408
DP grid cells filled (20 items):
1071
The naive recursion redoes the same subproblems over and over;
the DP grid writes each subproblem's answer down exactly once.

Part 3: Point the same technique somewhere else
hish vs fish
longest common substring:
ish
longest common subsequence:
ish
hish vs vista
longest common substring:
is
longest common subsequence:
is

Why substring and subsequence can disagree:
Longest common substring requires the matching letters to be
consecutive in both strings, while longest common subsequence
only requires the letters to appear in the same relative order,
with gaps allowed. Two strings can share a long subsequence made
of scattered letters without ever sharing a long unbroken run,
which is exactly what happens with 'hish' and 'vista'.

Reflection: for the grid technique to work at all, a problem
must break into independent subproblems -- the answer to a
smaller piece cannot depend on choices made in a different,
unrelated piece. Other places this same idea shows up: spell
check suggestions, git diff, and DNA sequence alignment.
```

## Reflection Questions

1. **Explain dynamic programming to someone who has never programmed.**
   - *Writing answers down so you never solve the same problem twice is the core 
   of it.*

    Suppose you have a room that holds 5 different rooms with puzzles to open a 
    bigger door. Pick the first puzzle and solve the simple color matching puzzle 
    behind it. When you return to check on the other puzzles, you put a sign on 
    the room you just completed to note that the room is completed, so you don't 
    end up going back through a puzzle you already finish. Repeat this for all 5 
    puzzle doors, going in, solving the puzzle, and then placing a sign that shows 
    you finished the puzzle, until you reach the giant door, which has a lock with 
    a 5 digit code that needs the other puzzles to be solved to accomplish. With 
    all the other doors solved, and marked with the information that they held 
    when finishing their puzzles, you can input the code to finish the final door. 
    Congratulations, have performed an example of Dynamic Programming.

2. **What has to be true about a problem for the grid to work at all?**
   
    
    For the dynamic programming grid to work, the larger problem must be able to 
    be broken down into smaller subproblems whose answers can be reused. The 
    solution to the larger problem must depend on the solutions of the smaller 
    versions of that same problem. In addition, those smaller subproblems should 
    overlap, meaning the same smaller problem would otherwise need to be solved 
    multiple times. The grid works by calculating each smaller problem once, 
    storing its answer, and then using that stored answer to help solve larger 
    problems.

3. **Where does this show up in real software?**
   
   
    Dynamic programming can be used in something like a spell-check software when 
    comparing a word typed by a user to possible correct words. The program can 
    break the comparison into smaller parts by comparing sections or individual 
    letters of the two words. It stores the results of these smaller comparisons 
    in a grid instead of repeatedly calculating them. This allows the software to 
    efficiently determine how similar two words are and suggest possible 
    corrections.
