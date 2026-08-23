# Lab Report — Chapter 6: Breadth-First Search


## Test Results


```
user@e2b:~$ cd /home/user && python3 main.py
Checking alice for skill python
Searched so far: {'alice'}
Checking bob for skill python
Searched so far: {'bob', 'alice'}
Checking claire for skill python
Searched so far: {'claire', 'bob', 'alice'}
Checking peggy for skill python
Searched so far: {'peggy', 'claire', 'bob', 'alice'}
Checking anuj for skill python
Searched so far: {'claire', 'peggy', 'anuj', 'bob', 'alice'}
Checking thom for skill python
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'bob', 'alice'}
Checking jonny for skill python
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'alice'}
Checking you for skill python
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'you', 'alice'}
Checking maria for skill python
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'maria', 'you', 'alice'}
Checking diego for skill python
Does anyone in my network know Python? True
Checking alice for skill astronomy
Searched so far: {'alice'}
Checking bob for skill astronomy
Searched so far: {'bob', 'alice'}
Checking claire for skill astronomy
Searched so far: {'claire', 'bob', 'alice'}
Checking peggy for skill astronomy
Searched so far: {'peggy', 'claire', 'bob', 'alice'}
Checking anuj for skill astronomy
Searched so far: {'claire', 'peggy', 'anuj', 'bob', 'alice'}
Checking thom for skill astronomy
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'bob', 'alice'}
Checking jonny for skill astronomy
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'alice'}
Checking you for skill astronomy
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'you', 'alice'}
Checking maria for skill astronomy
Searched so far: {'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'maria', 'you', 'alice'}
Checking diego for skill astronomy
Searched so far: {'diego', 'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'maria', 'you', 'alice'}
Checking sam for skill astronomy
Searched so far: {'diego', 'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'maria', 'sam', 'you', 'alice'}
Checking lee for skill astronomy
Searched so far: {'diego', 'claire', 'peggy', 'anuj', 'thom', 'jonny', 'bob', 'maria', 'sam', 'lee', 'you', 'alice'}
Does anyone know astronomy? False
Checking alice for skill manufacturing, distance: 1
Adding peggy to search queue.
Checking bob for skill manufacturing, distance: 1
Adding anuj to search queue.
Checking claire for skill manufacturing, distance: 1
Adding thom to search queue.
Adding jonny to search queue.
Checking peggy for skill manufacturing, distance: 2
Adding you to search queue.
Adding maria to search queue.
Checking anuj for skill manufacturing, distance: 2
Hops to nearest manufacturing contact: 2
Checking alice for skill python, distance: 1
Adding peggy to search queue.
Checking bob for skill python, distance: 1
Adding anuj to search queue.
Checking claire for skill python, distance: 1
Adding thom to search queue.
Adding jonny to search queue.
Checking peggy for skill python, distance: 2
Adding you to search queue.
Adding maria to search queue.
Checking anuj for skill python, distance: 2
Checking thom for skill python, distance: 2
Adding diego to search queue.
Checking jonny for skill python, distance: 2
Adding sam to search queue.
Checking you for skill python, distance: 3
Checking maria for skill python, distance: 3
Adding lee to search queue.
Checking diego for skill python, distance: 3
Hops to nearest python contact: 3
Checking alice for skill astronomy, distance: 1
Adding peggy to search queue.
Checking bob for skill astronomy, distance: 1
Adding anuj to search queue.
Checking claire for skill astronomy, distance: 1
Adding thom to search queue.
Adding jonny to search queue.
Checking peggy for skill astronomy, distance: 2
Adding you to search queue.
Adding maria to search queue.
Checking anuj for skill astronomy, distance: 2
Checking thom for skill astronomy, distance: 2
Adding diego to search queue.
Checking jonny for skill astronomy, distance: 2
Adding sam to search queue.
Checking you for skill astronomy, distance: 3
Checking maria for skill astronomy, distance: 3
Adding lee to search queue.
Checking diego for skill astronomy, distance: 3
Checking sam for skill astronomy, distance: 3
Checking lee for skill astronomy, distance: 4
Hops to nonexistent skill: -1
Checking alice for skill manufacturing
Added alice to searched.
Checking bob for skill manufacturing
Added bob to searched.
Checking claire for skill manufacturing
Added claire to searched.
Checking peggy for skill manufacturing
Added peggy to searched.
Checking anuj for skill manufacturing
Path to manufacturing contact: ['you', 'bob', 'anuj']
```

## Reflection Questions

1. **Explain breadth-first search to someone who has never programmed.**


    Suppose you're looking for a specific friend who has some good banana bread 
    through social media. Unfortunately, you don't have the friend, named "Lola", 
    directly as a friend since you forgot to add their contact. However, you do 
    know that Lola is friends with some of the people that you are friends with.
   
    You can check to see if any of the other friends are friends with Lola. For 
    example, you can check if Jeremy is friends with Lola or has someone who is 
    friends with Lola. If none of your direct friends are in contact with Lola, 
    you can go to the friends of your friends to see if they have contact with 
    Lola. You continue searching outward through the network of friends until Lola 
    is found. This serves as a queue, or a waiting line that keeps track of where 
    to search next, as you go through the groups of friends. Your direct friends 
    are the first ones in the queue, followed by the friends of your friends.
    
    Say that the paths you found were through three friends named Jeremy, Yonta, 
    and Hector. Now, between those three, you checked to see who took the least 
    amount of time to reach Lola to talk about the Banana Bread. Jeremy took 5 
    friends, Hector took 7 friends, while Yonta took 3. You conclude that it's 
    faster to reach out to Yonta to find Lola. Congrats, you had conducted Breadth 
    First Search!

2. **Two people in your network each know the other. Walk through what happens without the `searched` set.**

    In this situation, using a program without the searched set would result in 
    the system falling into an endless cycle between the two until the program 
    crashes or until someone forcibly turns off the program.

3. **Where does this show up in real software?**


    This shows up in Software like a GPS system, tracking the route that would 
    take the shortest amount of distance to reach the destination between two 
    places, such as the distance between your home and the local all-you-can-eat 
    buffet.
