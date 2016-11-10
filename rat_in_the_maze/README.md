Problem Description
--------------------

Given a square maze of size n, a rat, and a piece of cheese, you are trying to get the rat to the piece of cheese. 

```
Example:

n = 4
rat = (3, 3)
cheese = (3, 0)

+===+===+===+===+
|   |   |     R |
+   +   +---+   +
|         7   8 |
+---+   +   +---+
|   | 3       1 |
+   +   +   +   +
|     4   5 | C |
+===+===+===+===+

solution = 9
```

At every turn, you can prod the rat in one of four directions ('N', 'E', 'S', 'W') and the rat will run in that direction until it hits a wall or reaches the piece of cheese (yes, it's a really dumb rat).


```
Solve: What is the minimum distance the rat needs to travel before it can eat?
```