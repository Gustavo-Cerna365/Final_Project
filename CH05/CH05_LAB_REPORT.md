# Lab Report — Chapter 5: Hash Tables

## Test Results

```
555-1234
Not found
Allowed to vote
Already voted!
Allowed to vote
MISS: http://site.test/home
Contents of http://site.test/home
MISS: http://site.test/about
Contents of http://site.test/about
HIT: http://site.test/home
Contents of http://site.test/home
MISS: http://site.test/contact
Contents of http://site.test/contact
HIT: http://site.test/home
Contents of http://site.test/home
10
20
None
0.6
6
3
8
4
```

## Reflection Questions

1. **Explain a hash table to someone who has never programmed.**
   - *Mailboxes in a lobby, or a coat check, both work. Say what the hash function corresponds to.*
   Suppose you're delivering mail to a mailbox that holds mail for 5 different 
   people. Grab one envelope and check to see who it is for. Say the name is 
   "Anja". Your system states that Anja is mailbox number 4, so you put it to Box 
   number 4. Grabbing the next one, you see that it goes to "Pattie", who has 
   mailbox number 2. Repeating this for each one works like a Hash Table, since 
   each name has a consistent corresponding box number, and once all the mail is 
   delivered, you have successfully used a Hash Table.

2. **Chapter 5 says lookups are fast "on average." When is that not true, and what makes it go wrong?**

This can be false when you encounter something such as a Collision, due to the 
fact that a collision has two keys going into the same index. When there are too 
many keys hashed into a single index, the lookup time can degrade to O(n), with 
"n" representing the number of keys that are in that slot, compared to the rate of 
O(1), which dictates a constant pace for the process.

3. **Your page cache avoided repeating expensive work. Where have you seen caching in software you use?**
 
 This could be seen in Web Browsers, especially in ones that use images. The first 
 time you load up a website, it would take time to download the images that are 
 there, but on subsequent visits, the data is instead pulled out from the cache 
 instead of the computer downloading it fully again.
