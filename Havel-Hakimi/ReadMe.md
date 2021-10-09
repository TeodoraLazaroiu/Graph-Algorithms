## Havel-Hakimi Algorithm ##

Check if it's possible to create a graph with a given list of degrees

### Example ###

We are given the following list of degrees: 3, 4, 2, 1, 3, 4, 2, 1

```
havel_hakimi([3, 4, 2, 1, 3, 4, 2, 1])

3, 4, 2, 1, 3, 4, 2, 1 ----> sorting ----> 4, 4, 3, 3, 2, 2, 1, 1
4, 4, 3, 3, 2, 2, 1, 1 ---> algorithm ---> 3, 2, 2, 1, 2, 2, 1

3, 2, 2, 1, 2, 2, 1 ----> sorting ----> 3, 2, 2, 2, 2, 1, 1
3, 2, 2, 2, 2, 1, 1 ---> algorithm ---> 1, 1, 1, 2, 1, 1

1, 1, 1, 2, 1, 1 ----> sorting ----> 2, 1, 1, 1, 1, 1
2, 1, 1, 1, 1, 1 ---> algorithm ---> 0, 0, 1, 1, 1

0, 0, 1, 1, 1 ----> sorting ----> 1, 1, 1, 0, 0
1, 1, 1, 0, 0 ---> algorithm ---> 0, 0, 0, 0 (STOP)
```

All the values are 0 which means we can construct a graph with the given sequence of degrees
