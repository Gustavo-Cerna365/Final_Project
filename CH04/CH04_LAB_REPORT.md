# Lab Report — Chapter 4: Quicksort

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your benchmark table — all six rows, including any `RecursionError`.*

```
Part 1: Divide & Conquer warm-ups
recursive_sum: 52
recursive_count: 12
recursive_max: 10
binary_search_recursive (target=8): 9
binary_search_recursive (target=99): -1

Part 2: Quicksort
first pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Part 3: Benchmark
shape             strategy    result            
------------------------------------------------
unsorted          first       0.001561 s        
unsorted          random      0.001699 s        
sorted            first       RecursionError    
sorted            random      0.001662 s        
reverse sorted    first       RecursionError    
reverse sorted    random      0.001604 s  
```

## Reflection Questions

1. **Explain quicksort to someone who has never programmed.**


Say you have a stack of work paper, and you have to sort it alphabetically by last 
name. Looking through them one by one would take a long while, so here is what can 
be done: Grab an paper with a last name to sort other paper by, and label that 
paper you chose as a 'Pivot'. For this example, let us say our pivot is a name 
that starts in 'L'. Then, group the left side of the pivot names with a letter 
before the pivot (A-K), and the right names with a letter after the pivot (M-Z). 
Afterwards, grab a paper you grab that is not you pivot, place them to the left 
and the right of the pivot accordingly. So, if you have a Last Name that starts 
with "C", then set it to the left. If you have a last name that starts with a "P", 
place it on the right stack. Repeat this process until you got the stack set 
into those two sets. Now, you can repeat this process for both stacks to sort 
those more thouroghly. Once completed, you would have all the last names sorted 
alphabetically, and that would be the quicksort process completed.


2. **A random pivot usually avoids the worst case. Why does randomness help here?**

This helps as this would reduce the chance of the sorting becoming very lopsided 
to the point you have to sort the entire stack repeatedly, especially when the 
stack that needs to be sorted is a large list of elements. Most importantly, it 
will deeply assist in ensuring a bad pivot is not repeatedly chosen.

3. **Where does sorting show up in software you actually use?** 

Sorting shows up in all sorts of things, with a good example being Database 
Management Systems, specifically those with filter options to sort with different 
bases to sort by, such as Name, Date, ID, Price, etc., and this would make
large collections of information easier to organize and find.
