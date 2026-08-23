# Lab Report — Chapter 7: Trees and Huffman Coding


## Test Results


```
=== Part 1: Directory Traversal ===
BFS order:
root
docs
media
web
notes.txt
todo.txt
draft.docx
photo.png
song.mp3
index.html
style.css

DFS order:
root
docs
notes.txt
todo.txt
draft.docx
media
photo.png
song.mp3
web
index.html
style.css

=== Part 2: DFS vs BFS Shortest Path ===
DFS found target: target (took the FAR path)
BFS found target: target (took the CLOSE path)

=== Part 3: Huffman Coding ===
Frequencies: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
Codes: {'a': '0', 'c': '100', 'd': '101', 'r': '110', 'b': '111'}
Encoded bitstring: 01111100100010101111100
Decoded text: abracadabra
Huffman bits: 23  vs  fixed-width bits: 88
```

## Reflection Questions

1. **Explain the difference between BFS and DFS to someone who has never programmed.**

    Suppose you're exploring a dungeon to find a chest that was located somewhere 
    in the dungeon, and you see three different paths, Route A, Route B, and Route 
    C, laid before you. You can go about finding this chest in two ways.

    The first way is to pick the one path, and follow it all the way down to the 
    end of the path, and go back through the already explored rooms to the most 
    recent point that there was an unexplored path. For example, let's say you 
    take Route A, and reach another room that has two more paths, with one marked 
    with T (Route T) and one with S (Route S). Going Further down the path through 
    Route T, you find yourself at a deadend, so you turn back to head back and go 
    down Route S next. Once you find Nothing in that Room, you go all the way back 
    to the start to go down Route B, and repeat the cycle. That is Depth First 
    Search.

    The next method is by going it in groups. When you go down Route A, you would 
    find Route T and Route S. But, instead of going down either route, you go back 
    to see what lies behind Route B, and find Route Y and Route Z. You repeat it 
    for Route C, and soon start searching into the next Routes in the waiting 
    line, being Routes T and S. This is the Breadth First Search method.


2. **Why do frequent letters get shorter codes? Use your own code table.**

    In my code table, "a" appeared the most frquently in abracadabra, totaling 5 
    appearances. Because it showed up more often than other letters in the word, 
    it got the shortest code of "0", with "b" and "r" recieving 3 bit codes, as 
    well as "c" and "d", despite appearaing the least. This allows for the coding 
    to reduce the amount of bits needed to encode the message.

3. **Your decoder reads a stream of bits with no separators and still gets it right. Why is there never any ambiguity?**

    There is never any ambiguity because Huffman codes are prefix-free. This means 
    that no complete code for one character is the beginning of another 
    character's code. For example, in my code table, "a" is represented by "0", 
    while the other characters begin with "1". The decoder can start at the 
    beginning of the Huffman tree and follow each bit until it reaches a 
    character. Once it reaches a character, it knows that code is complete and 
    returns to the root to begin reading the next character. Because no 
    character's code can be mistaken for the beginning of another complete 
    character code, the decoder can correctly read a stream of bits even without 
    spaces or separators.
