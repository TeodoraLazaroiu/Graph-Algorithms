# Havel-Hakimi Algorithm

Check if it's possible to create a graph with a given list of degrees

1. Sort the sequence of non-negative integers in non-increasing order
2. Delete the first element called n and subtract 1 from the next n elements
3. Repeat 1 and 2 until one of the stopping conditions is met

Stopping conditions:

- All the elements remaining are equal to 0 - simple graph exists
- Negative number encounter after subtraction - no simple graph exists
- Not enough elements remaining for the subtraction step - no simple graph exists

### Example ###

1. First example: 
We are given the following list of degrees: 3, 4, 2, 1, 3, 4, 2, 1

```python
havel_hakimi([3, 4, 2, 1, 3, 4, 2, 1])
```
```
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

2. Second example:
We are given the following list of degrees: 3, 2, 1, 0

```python
havel_hakimi([3, 2, 1, 0])
```
```
3, 2, 1, 0 ----> sorting ----> 3, 2, 1, 0
3, 2, 1, 0 ---> algorithm ---> 1, 0, -1 (STOP)
```

We encounter a negative element which means we can NOT construct a graph with Havel-Hakimi algorithm

