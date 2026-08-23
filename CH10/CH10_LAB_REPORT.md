# Lab Report — Chapter 10: Greedy Algorithms


## Test Results


```
Part 1: Scheduled classes
[('Art', 9.0, 10.0), ('Math', 10.0, 11.0), ('Music', 11.0, 12.0)]
Part 2: Greedy knapsack choice
[('stereo', 3000, 4)]
Part 2: Greedy knapsack value
3000
Part 2: Brute-force knapsack choice
[('laptop', 2000, 3), ('guitar', 1500, 1)]
Part 2: Brute-force knapsack value
3500
Part 2: Gap between brute force and greedy
500
Part 3: Stations chosen by greedy set cover
['kone', 'ktwo', 'kthree', 'kfive']
Part 3: Number of subsets an exact solver checks for n=5
32
Part 3: Number of subsets an exact solver checks for n=20
1048576
Part 3: Number of subsets an exact solver checks for n=100
1267650600228229401496703205376
```

## Reflection Questions

1. **Explain the greedy strategy to someone who has never programmed.**
   
    Suppose you are building a schedule for a trip to California for a week plus 
    an extra day. You have can go to a few different places for some fun and some 
    dining, with Disney World being about 3 whole days, a trip to Dave and Busters 
    taking 2 days to achieve, a stay with some family members at their home taking 
    about 1 day only, and staying with a friend of you father taking yet another 2 
    days, and the final day is a return trip to the airport to go back home. So, 
    you decide to pick the one that takes the most amount of days, which is Disney 
    World. Following that, you decide to stay at your dad's friend's home, and 
    finish it off with a trip to Dave & Busters, with the final, extra eigth day 
    being the trip back to the airport. Congratulations, you have performed a 
    greedy algorithm.

2. **Greedy was perfect for scheduling and wrong for the knapsack. What changed about the problem?**

    The reason for this contrast is due to the fact that the knapsack had items 
    that, when combined, were worth more than the most valuable individual item. 
    available on the list, which were the laptop and the guitar. But, because the 
    Stereo was the most expensive item to grab by the value (selling value) rather 
    than the cost (weight), it resulted in a non-fully optimized solution. 
    Meanwhile, for the classroom situation, it chose the classes that ended the 
    earliest, allowing for the the classes to be chosen at their earliest, and not 
    have any harm be done to any future choices, as opposed to the limit 
    preventing more items from being taken in the knapsack situation.

3. **You already wrote a greedy algorithm in an earlier lab — building the Huffman tree in Chapter 7 repeatedly merges the two lowest-frequency nodes. Is that one exactly optimal, or an approximation?**

    The coding used in chapter 7 is an exactly optimal solution for the algorithm 
    that it was used in, as the Huffman coding repeatedly merged two nodes that 
    were the lowest frequencies, and this allowed the greedy choice to 
    mathematically guarantee creating an optimal prefix-free encoding.
