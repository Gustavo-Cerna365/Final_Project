# Lab Report — Chapter 2: Selection Sort

## Test Results

The selection sort test has yielded the following sorted list:

```
[2, 3, 5, 6, 7, 9, 10, 11, 13, 22, 33, 56, 74, 88]

['Artist B', 'Artist C', 'Artist A']
```

## Reflection Questions

1. **Explain selection sort to someone who has never programmed.**

   
   Let's say that you have a set of 5 cards, each numbered 5, 3, 7, 9, 1, and you need to sort the cards
   from smallest to biggest. Look through the set to find the smallest number that has not been moved
   yet. Once that card is found, you would then pick it up, and move it over to the beginning of the 
   sorted set. When that step is done, you can repeat it for every card you do, finding the next 
   smallest card, and then the next smallest, until you have every card in order, and finishing the
   sorting with the set arranged into 1, 3, 5, 7, 9. This is the process that is Selection Sort.

2. **Your list gets twice as long. Does selection sort do twice the work, or more?**


   If the list doubles, Selection sort would do more than double the amount of work needed. With about 
   5 items in a list, there would be about 5+4+3+2+1 checks, totaling about 15 checks, as each time you 
   check the items in a list, you would have to check the other cards again to see which one meets the 
   requirement, and be arranged to the start of the set as the second sorted item. If we have a list of 
   10 items, thereby doubling the list, the amount of work done would increase to about 10+9+8+7+6+5+4+3
   +2+1 checks, or a total of 55 checks, compared to the 15 checks with only 5 items

3. **Chapter 2 says arrays are used more often than linked lists in practice. Based on what you built, why would that be?**


Arrays are much quicker in reading compared to the ever rapidly expanding number of operations 
needed to sort a list out using linked list, since a linked list would go through every item on the 
list one by one in the order that they are placed, while Arrays can go at it from any specific 
position, rather than starting from the very start, then reaching that number. Based on how the program 
works, having an array would make it easier to access specific positions in the list, although 
Selection Sort would still need to search through the remaining items to find the smallest value.
