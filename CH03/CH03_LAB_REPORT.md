# Lab Report — Chapter 3: Recursion

*Complete both sections and commit this file with your code.*

## Test Results


```
Find File:
-> entering: /root
  -> entering: /root/readme.txt
  <- exiting: /root/readme.txt
  -> entering: /root/docs
    -> entering: /root/docs/notes.txt
    <- exiting: /root/docs/notes.txt (FOUND!)
  <- exiting: /root/docs
<- exiting: /root
/root/docs/notes.txt

Count Files:
-> entering: root
  -> entering: readme.txt
  <- exiting: readme.txt
  -> entering: docs
    -> entering: notes.txt
    <- exiting: notes.txt
  <- exiting: docs
  -> entering: empty_folder
  <- exiting: empty_folder
<- exiting: root
2

Total Size:
-> entering: root
  -> entering: readme.txt
  <- exiting: readme.txt
  -> entering: docs
    -> entering: notes.txt
    <- exiting: notes.txt
  <- exiting: docs
  -> entering: empty_folder
  <- exiting: empty_folder
<- exiting: root
320

File Tree:
root
  readme.txt
  docs
    notes.txt
  empty_folder
```

## Reflection Questions

1. **Explain recursion to someone who has never programmed.**
   

  Let's say that you need to find a key within some boxes, with some having more 
  boxes within them. To start, you can go about it by the following method: Grab 
  one box from the boxes you can grab, and open up the box to search the contents 
  of the box. If there is a key, you can claim you found the key, and end the 
  search. If there is another box inside the box, you can start searching inside 
  that box until it is empty to resume searching the rest of the initial box. Once 
  the box is empty, you can search the next box in the starting main box. Once 
  that is done, then you can search inside the boxes that were inside the starting 
  boxes you searched.

2. **An empty folder is a legitimate base case, not an error. Why does treating it as an error break the program?**


  
  Because it is indeed possible for a folder to be empty and not contribute. If 
  they were to be considred an error, the program would break due to the fact 
  that, when the program encounters an empty folder, the program would encounter 
  an unexpected error or return an incorrect result on the search.


3. **A folder nested 10,000 levels deep would crash your code. Why?**


  The reason for this deepy nested folder crashing the code is due to the fact 
  that the depth it is at would cause the program to encounter a recursion limit, 
  as there would be too many recursion calls waiting for the deepest one to finish 
  and return.
