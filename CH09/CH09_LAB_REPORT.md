# Lab Report — Chapter 9: Dijkstra's Algorithm


## Test Results


```
=== Part 1: Book's warm-up graph ===
Costs: {'start': inf, 'a': 5, 'b': 2, 'finish': 6}
Parents: {'start': None, 'a': 'b', 'b': 'start', 'finish': 'a'}
Path: start -> b -> a -> finish

=== Part 2: Twin Peaks -> Golden Gate Bridge ===
BFS fewest-hops path: twin_peaks -> a -> b -> golden_gate
BFS hop count: 3
Dijkstra lowest-cost path: twin_peaks -> c -> d -> e -> golden_gate
Dijkstra total cost: 12

=== Part 3: Breaking Dijkstra with negative weights ===
Costs: {'start': inf, 'a': 2, 'b': -8, 'finish': 6}
Parents: {'start': None, 'a': 'start', 'b': 'a', 'finish': 'b'}
Path: start -> a -> b -> finish
Reported cost to finish: 6
True cheapest cost (by hand): 2 + (-10) + 5 = -3
```

## Reflection Questions

1. **Explain Dijkstra's algorithm to someone who has never programmed.**

    Suppose you are trying to drive from your home to a specific destination. You 
    have several different roads you can take, with each road having a different 
    travel time. Instead of simply choosing the route with the fewest roads, you 
    want to find the route that takes the least amount of total time.

    Start at your current location and look at the cost of reaching the locations 
    directly connected to you. Then, choose the cheapest path that has not already 
    been checked and use that location to see if it can find cheaper routes to 
    other locations.

    For example, with the Twin Peaks to the Golden Gate Bridge, the route through 
    `a` and `b` only takes 3 different roads, but each road is super expensive. 
    Instead, choose a route through `c`, `d`, and `e`, which takes 4 different 
    roads, but this has a total time of only 12 minutes. This is how Dijkstra's 
    algorithm, and you have found the shortest path.

2. **Why does the algorithm always pick the cheapest unprocessed node next, instead of going in order?**

    Dijkstra's algorithm picks the cheapest unprocessed node because it is trying 
    to find the lowest total cost to reach the destination. The cheapest 
    unprocessed node is the best candidate to explore next because, when there is 
    no negative edge costs present, any additional road taken from that node can 
    only increase the total cost.

3. **Where does the "cost" on an edge come from in real routing software, and how does changing what you measure change the answer without changing the algorithm?**

    The cost of an edge in real routing software can range from things like the 
    time it takes to reach a specific location between destinations, the amount of 
    fuel it takes to move something from one spot to another, the amount of 
    material to make a pathway between two options, etc. Changing what is being 
    measured can change which route Dijkstra's algorithm considers the cheapest, 
    even though the algorithm itself does not change. For example, one route could 
    be shorter in distance but take longer because of traffic. Another route could 
    be longer but have less traffic and therefore take less time.
