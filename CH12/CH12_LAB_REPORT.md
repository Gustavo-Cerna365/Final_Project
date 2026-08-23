# Lab Report — Chapter 12: K-Nearest Neighbors


## Test Results


```
======================================================================
PART 1: Features and distance
======================================================================
New fruit features (size, redness): [7, 5]
Distance from new fruit to first training fruit [5, 2]: 3.61
3 nearest neighbors to the new fruit:
  features=[6, 4] label=orange
  features=[7, 3] label=orange
  features=[6, 3] label=orange
Predicted label for new fruit: orange

======================================================================
PART 2a: Failure mode -- the wrong k
======================================================================
k= 1 -> predicted label: dog
k= 3 -> predicted label: cat
k=15 -> predicted label: dog
Explanation:
  At k=1, the single nearest neighbor is the mislabeled 'dog'
  outlier sitting right on top of the test point, so a tiny
  labeling mistake in the data completely controls the answer.
  At k=15, EVERY training point is included, so locality no
  longer matters at all -- the prediction just becomes whichever
  class happens to have more members overall (dog, 8 vs 7),
  even though the test point sits inside the cat cluster.

======================================================================
PART 2b: Failure mode -- unscaled features
======================================================================
Raw features (weight in grams, quality rating 1-5):
  Prediction using raw features: junk
Normalized features (0-1 scale):
  Prediction using normalized features: healthy
Explanation:
  With raw features, the weight-in-grams values (hundreds) are
  so much larger than the 1-5 quality scores that distance is
  decided almost entirely by weight -- the quality feature is
  effectively drowned out because grams and stars are not the
  same units. Once every feature is rescaled to 0-1, both
  features contribute fairly, and the prediction changes.

======================================================================
PART 3: Same neighbors, different question -- regression
======================================================================
Classification and regression from the SAME k_nearest() call:
  classify(neighbors)       -> orange
  predict_rating(neighbors) -> 3.33
Predicted rating for Frank on 'Up': 4.67

======================================================================
Reflection
======================================================================
To recommend restaurants, useful features might be: average
price, cuisine type (encoded as a number), distance from home,
and average star rating. If one of those features were the
same value for every restaurant in the dataset (e.g. every
restaurant is in the same city), that feature would add zero
information -- it could never help distinguish one restaurant
from another, since its distance contribution would always be
the same for every comparison.
```

## Reflection Questions

1. **Explain k-nearest neighbors to someone who has never programmed.**
   
   
   Suppose you're relaxing on bed to watch videos on YouTube. As everyone does, 
   you have your own opinion on what videos you like. As you watch videos, the 
   system checks to see which ones you like and which ones you don't like, and the 
   way it checks is with things such as which videos you give a like to, which 
   ones you dislike, which ones you watch for a while, etc.

   Once that is done, YouTube cheks to see what videos other people with a similar 
   set of tastes/prefrences enjoyed, and they start to recommend those same videos 
   to you for you to watch and enjoy. Once that happens, you have experienced the 
   K-Nearest Neighbors process. Do note that it does not actually take physical 
   distance between you and the person into account for the System, only the 
   distance between your opinion and theirs on topics, and can usually be done by 
   a point based system.

2. **Two classmates pick k = 1 and k = 15 on the same data and get different answers. What is each one doing wrong, or right?**
    
    
    Classmate A is doing the process with an error of having too little of a pool 
    to compare to, since only comparing against one thing makes it way too 
    difficult to find what items an element is similar too, and Classmate B fixes 
    that issue well. But, it is important to note that if the pool is too small, 
    having k = 15 is a big risk, which is why something like k = 3 or k = 5 tends 
    to be the usual numbers for comparisons.

3. **Chapter 12 says Netflix-style recommendations work this way. Describe how someone's viewing history becomes the "features."**
    
    
    Someone's viewing history can become the features by turning their preferences 
    and watching habits into information that can be compared with other users. 
    For example, the system can look at which movies or shows a person watched, 
    how much of them they watched, whether they finished them, and how they rated 
    or liked them. Each of these pieces of information helps create a pattern 
    representing that person's interests.

    Netflix can then compare that pattern to other users. If two people have 
    watched and enjoyed many of the same types of movies or shows, they may be 
    considered close neighbors. The system can then look at what those similar 
    users watched and enjoyed that the first person has not seen yet and recommend 
    those movies or shows. In this way, a person's viewing history becomes the 
    "features" that are used to find people with similar tastes.
