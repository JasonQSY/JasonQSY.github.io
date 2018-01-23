---
layout: post
title:  "Experience of Google foobar"
date:   2018-01-06
categories: algorithm
---

Google foobar is an interesting challenge. Invited by my friend, I spent some time to completeit. There are actually some interesting ideas which can be talked about.

## Level 1

### The cake is not a lie!

```
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members
of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of
minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are
multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so
you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z)
corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called answer(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the
maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = "abccbaabccba"
Output:
    (int) 2

Inputs:
    (string) s = "abcabcabcabc"
Output:
    (int) 4

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
```

It seems that we cannot optimize based on the brute force approach. Hence,

```python
def answer(s):
    best = 1
    # lets try from len(subarray) n to 1
    for i in range(len(s)):
        length = len(s) / (i + 1)
        succ = True
        for j in range(len(s)):
            if s[j] != s[j % length]:
                succ = False
                break

        if succ:
            best = i + 1

    return best
```

## Level 2

### Lovely Lucky LAMBs

```
Lovely Lucky LAMBs
==================

Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's
All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen
will revolt and you'll all get demoted back to minions again!

There are 4 key rules which you must follow in order to avoid a revolt:
    1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
    2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
    3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note
that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require
at least as many LAMBs as the most junior henchman.)
    4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman
could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of
LAMBs.

Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return
an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as
possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you
had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were
as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts. You can expect total_lambs to always be a positive integer less
than 1 billion (10 ^ 9).

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) total_lambs = 10
Output:
    (int) 1

Inputs:
    (int) total_lambs = 143
Output:
    (int) 3

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
```

The greedy approach in this problem can lead to a correct answer. If we use $f(n)$ to denote the number of LAMBs shared by henchman n, there are only two constrains

$$f(n) \ge f(n-1) + f(n-2)$$

$$f(n) \le 2 f(n-1)$$

Then the solution is straightforward.

```python
def answer(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)

def generous(total_lambs):
    """
    Return: the number of henchmen sharing the LAMBs
        if as generous as possible.
    """
    num = 1
    last = 0
    cur = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < cur * 2:
            if total_lambs >= cur + last:
                num += 1
            break
        num += 1
        cur, last = cur * 2, cur
        total_lambs -= cur

    return num

def stingy(total_lambs):
    """
    Return: the number of henchmen sharing the LAMBs
        if as stingy as possible.
    """
    num = 1
    last = 0
    cur = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < last + cur:
            break
        num += 1
        cur, last = cur + last, cur
        total_lambs -= cur

    return num
```
### Gearing Up for Destruction

```
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation
gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and
the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on
each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can
choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per
minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function answer(pegs) which,
if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its
simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support
configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function answer(pegs) should return
the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the
last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and answer(pegs) should
return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and
10000 inclusive.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) pegs = [4, 30, 50]
Output:
    (int list) [12, 1]

Inputs:
    (int list) pegs = [4, 17, 50]
Output:
    (int list) [-1, -1]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
```

I think this is the most interesting question among those in level 1-3. The problem is actually to solve a kind of linear system. For example, if `pegs = [4, 30, 50]`, let the radius of the last gear be $r_0$, the first gear $2r_0$, the second gear  $r_1$, respectively. Then

$$\begin{cases} 2r_0 + r_1 = 30 - 4\\ r_1 + r_0 = 50 - 30\end{cases}$$

It is a `len(pegs) - 1` dimensional linear system. We can solve it by Gauss Elimination. However, actually such a special kind of system can be solved in linear time. Here is my solution.

```Python
from fractions import Fraction

def answer(pegs):
    if len(pegs) == 2:
        # it is not a linear system
        x = [Fraction(pegs[1] - pegs[0]) / 3]
    else:
        # solve linear system
        dim = len(pegs) - 1
        A = [[Fraction(0) for _ in range(dim)] for _ in range(dim)]
        b = [Fraction(0) for _ in range(dim)]
        for i in range(dim):
            n = (i + 1) % dim
            b[i] = Fraction(pegs[i + 1] - pegs[i])
            A[i][i] = Fraction(1)
            A[i][n] = Fraction(1)

        A[0][0] = Fraction(2)
        x = solve(A, b)

    # result
    for i in range(len(x)):
        if x[i] < 0 or x[i].numerator < x[i].denominator:
            return [-1, -1]

    x[0] *= 2
    return [x[0].numerator, x[0].denominator]

def solve(A, b):
    """
    Solve a linear system Ax = b, adaptive for the matrix in this problem.
    Inputs:
        A - a nxn matrix. n >= 2.
        b - a nx1 vector.
    Returns:
        x - the nx1 vector satisfying Ax = b.
    """
    dim = len(b)

    # A -> Upper triangle
    for i in range(dim - 1):
        if A[dim - 1][i] != 0:
            frac = A[dim -1][i] / A[i][i]
            b[dim - 1] -= frac * b[i]
            A[dim - 1][i] = Fraction(0)
            for j in range(i + 1, dim):
                A[dim - 1][j] -= frac * A[i][j]

    b[dim - 1] /= A[dim - 1][dim - 1]
    A[dim - 1][dim - 1] = Fraction(1)

    # backward subs
    for i in range(dim - 2, -1, -1):
        b[i] -= b[i+1]

    # deal with row 0
    b[0] /= 2

    return b
```
## Level 3

### Queue To Do

```
Queue To Do
===========

You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the security checkpoints that guard the underlying systems of the
LAMBCHOP are going to be a problem. You were able to take one down without tripping any alarms, which is great! Except that as Commander Lambda's
assistant, you've learned that the checkpoints are about to come under automated review, which means that your sabotage will be discovered and your
cover blown - unless you can trick the automated review system.

To trick the system, you'll need to write a program to return the same security checksum that the guards would have after they would have checked
all the workers through. Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the checkpoint guards have
found ways to quicken the pass-through rate. Instead of checking each and every worker coming through, the guards instead go over everyone in line while
noting their security IDs, then allow the line to fill back up. Once they've done that they go over the line again, this time leaving off the last
worker. They continue doing this, leaving off one more worker from the line each time but recording the security IDs of those they do check, until they
skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the
workers' orderly nature causes them to always line up in numerical order without any gaps.

For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:
0 1 2 /
3 4 / 5
6 / 7 8
where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.

Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
17 18 19 20 /
21 22 23 / 24
25 26 / 27 28
29 / 30 31 32
which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at least 1 worker long.

With this information, write a function answer(start, length) that will cover for the missing security checkpoint by outputting the same checksum the
guards would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the
line (length) before the automatic review occurs, so your program must generate the proper checksum with just those two values.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) start = 0
    (int) length = 3
Output:
    (int) 2

Inputs:
    (int) start = 17
    (int) length = 4
Output:
    (int) 14

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.

```

The key idea is how to find the xor sum from $a$ to $b$, i.e.
$$s(a, b) = a \oplus (a+1) \oplus \cdots \oplus (b-1) $$

It can be solved in $O(1)$. Firstly, if $a = 0$ or $a = 1$, it can be solved in $O(1)$. See [Calculate XOR from 1 to n](https://www.geeksforgeeks.org/calculate-xor-1-n/). Then,

$$s(a, b) = s(1, a) \oplus s(1, b)$$

since the inverse of a group whose operation is xor is the element itself. Then the solution is

```python
def answer(start, length):
    checksum = 0
    cur = start
    cur_len = length
    while cur_len > 0:
        checksum ^= xorsum(cur) ^ xorsum(cur + cur_len)
        cur += length
        cur_len -= 1

    return checksum

def xorsum(n):
    """
    Return 0^1^2^....^(n-1)
    """
    if n == 0:
        return 0

    if (n-1) % 4 == 0:
        return n-1
    elif (n-1) % 4 == 1:
        return 1
    elif (n-1) % 4 == 2:
        return n
    else:
        return 0
```
### The Grandest Staircase Of Them All

```
The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance,
she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for
example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each
amount of bricks, so she can pick the one with the most options.

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous
one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a
height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown
below:

#
#
#
##
41

#
##
##
32

Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n
bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) n = 3
Output:
    (int) 1

Inputs:
    (int) n = 200
Output:
    (int) 487067745

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
```
```python
def answer(n):
    # your code here
    memo = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    return staircase(1, n, memo) - 1

def staircase(h, l, memo):
    if memo[h][l] != 0:
        return memo[h][l]
    if l == 0:
        return 1
    if l < h:
        return 0
    memo[h][l] = staircase(h + 1, l - h, memo) + staircase(h + 1, l, memo)
    return memo[h][l]
```
### Find the Access Codes

```
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is
secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access
codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains
the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky
triples" in order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z,
such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door
when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list
indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  
The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples
are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) l = [1, 1, 1]
Output:
    (int) 1

Inputs:
    (int list) l = [1, 2, 3, 4, 5, 6]
Output:
    (int) 3

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
```

It is not hard, but the time limit is a bit weird. I think the key idea is that the problem can be solved in $O(n^2)$, like

```python
def answer(l):
    cnt = 0
    pairs = []
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            if l[j] % l[i] == 0:
                pairs.append([l[i], l[j]])

    for pair in pairs:
        for k in range(pair[1] + 1, len(l)):
            if l[k] % pair[1] == 0:
                cnt += 1

    return cnt
```

However, it still exceeds the time limit. A  better solution is like

```Python
def answer(l):
    cnt = 0
    memo = [0] * len(l)
    for i in xrange(len(l) - 1):
        for j in xrange(i + 1, len(l)):
            if l[j] % l[i] == 0:
                memo[j] += 1
                cnt += memo[i]

    return cnt
```

## Level 4

TODO

## Level 5

TODO
