# Lab Report — Chapter 1: Binary Search

*Complete both sections and commit this file with your code.*

## Test Results

Linear search for 67:
Index: 9
Steps 10

Binary Search for 67:
Index: 9
Steps: 2



List Size: 10
Linear Search Steps: 10
Binary Search Steps: 3

List Size: 100
Linear Search Steps: 100
Binary Search Steps: 6

List Size: 1,000
Linear Search Steps: 1,000
Binary Search Steps: 9

List Size: 10,000
Linear Search Steps: 10,000
Binary Search Steps: 13

List Size: 100,000
Linear Search Steps: 100,000
Binary Search Steps: 16

List Size: 1,000,000
Linear Search Steps: 1,000,000
Binary Search Steps: 19

```
As the list becomes Larger and Larger, the steps required to finish
the task using linear search increases alongside the list, as it needs
to check every single item individually. However, Binary Search removes
half of the list with every comparison that is done, showing just how much
more efficient Binary Search is compared to Linear Search.
```

## Reflection Questions

1. **Explain binary search to someone who has never programmed.**
      Imagine you have a phone book open in front of you, and you're looking for 
      someone in said phone book. Going about it from the start, one name at a time, 
      thus, performing linear search, is not a good idea, as that would end up taking 
      too long to find them. Instead, you can go about things by picking the item in
      the middle of the list and comparing it to what you want. Let's say you are
      looking for someone named Smith. If the middle name is a name like Williams, then,
      knowing that the letter W comes AFTER the letter S, the name Smith must be to
      the left, and you can remove the right half of the list at that very moment. If
      the middle name ends up being Brown, then you know you are somewhere BEFORE Smith,
      meaning that the name Smith is somewhere to the right of where you are, allowing
      you to remove all the items to the left of that name. This process can be done
      again, and again until you find the name that you are looking for, showing you
      had performed the Binary Search.


3. **Doubling the list adds only one step to binary search. Why does that happen?**
      
      The reason for this happening is because of how Binary Search handles the 
      searches by placing a guess on the number that is in the middle of the number, 
      and if the number is too big or too small, it would remove half of the list, 
      which means by adding twice the amoung to the list, the list would remove said 
      half already in a single guess, and each operation that is done in Binary Search 
      is counted as a single step. 

4. **Where does binary search show up in real software?**
      
      Binary Search can appear often in things like Databases to search for a specific 
      record in the database, in libraries to find titles and sort them out from a 
      large selection, and even with search engines as they implement it rather 
      frequently to quickly find documents or data that is relevant and within sorted 
      indexes.
