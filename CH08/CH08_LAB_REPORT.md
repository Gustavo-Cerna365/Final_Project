# Lab Report — Chapter 8: Balanced Trees


## Test Results


```
=== Part 2: Watch it degenerate ===
Tree A height: 4
Tree B height: 12
Tree A in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
Tree B in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
Tree A search comparisons for largest value: 3
Tree B search comparisons for largest value: 12

=== Part 3: Rotate to fix it ===
AVL height after sorted insertion: 4
AVL in-order: [10, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 80]
```

## Reflection Questions

1. **Explain a binary search tree to someone who has never programmed.**

    Suppose you are playing a guessing game where someone is thinking of a number 
    between 1 and 100. Instead of guessing every number one by one, you can make a 
    guess and ask whether the correct number is higher or lower.

    For example, if the number the person is thinking of is 80 and the first hint 
    you have is 50, you know that 80 must be somewhere on the right side because 
    80 is greater than 50. You can then continue comparing the value you are 
    searching for with the next number until you find it. This allows you to 
    narrow down where to search instead of checking every value individually. That 
    is how Binary Search Tree Works

2. **A tree built from sorted input performs no better than a plain list. Explain why, using your own two trees.**

    A tree built from sorted input can become unbalanced because every new value 
    is greater than the previous value. Because of this, each new node is placed 
    to the right of the previous node. Instead of creating branches that allow the 
    search to narrow down quickly, the tree becomes a long chain.

    In the trees that I have, Tree A was built using a mixed-order stype input and 
    came out with a height of 4. Searching for the largest value only required 3 
    comparisons. Meanwhile, Tree B used the exact same values, but they were 
    inserted in sorted order, which caused Tree B to end up with a height of 12, 
    and searching for the largest value required 12 comparisons, thus needing 12 
    searches to find the biggest value, and completely removing the benefits of 
    using a Binary Tree

3. **Chapter 8 says balanced trees are used for database indexes. Based on what you built, why is a tree a good fit for that job?**

    A balanced tree is a good fit for a database index because it keeps data 
    organized in a way that allows searches to quickly narrow down where the 
    needed information could be.

    In the program, the normal Binary Search Tree built from sorted input had a 
    height of 12. However, after AVL insertion and rotations were applied to the 
    tree, the AVL tree containing the same values had a height of only 4. The AVL 
    tree also kept the values in the correct sorted order.

    This can help greatly when a database contains a super large amount of 
    records, and searching through every record one by one would take a long time. 
    Keeping the tree balanced would prevent it from becoming a long chain, 
    allowing the database to find and organize records more efficiently.
