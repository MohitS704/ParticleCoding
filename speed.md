---
title: Speed
filename: speed
chapternum: '2'
numbersections: true
---

> "Gotta go fast", [Sonic the Hedgehog]

## Objectives

* Miscellaneous ways to speed up code
  * Remove redundancy
  * Loop unrolling
  * 
* Understand what vectorized calculations do
* Understand how to leverage these calculations for speed
* Be able to convert non-vectorized calculations into vectorized ones


## Why should I Care About Non-Asymptotic Speed?

Well, yes, asymptotic speed is the really important one - since that is an immutable aspect of a given algorithm. However, we always want things to be faster! Well... not necessarily _always_ - the fact that you're using Python and not coding everything in x86 is indicative of the fact that you care about the ease at which you can code more than the speed at times. After all, base Python is a slow language. 

## What is "vectorization"?

Remember in the [introduction](introduction.html) when operations were counted as additive constants? Take the following operation,

```python
x = [0, 1, 2, 3, 4, 5]
for i in range(len(x)):
  x[i] *= 10
```

This is simply multiplying all of the values in x by 10! This takes 10 operations to do (computation is _much_ more complicated than just treating these as simple constant time procedures, but for the purposes of this text this interpretation suffices).

Now, here comes the "_vector_" part of "vectorization" (In a very simplified format). Imagine loading the list x into a "vector" that is stored in memory simultaneously - now instead of having 10 discrete objects - you have 1 singular entity in memory to do with as you please. Now, just like in math, where $\vec{x} = {0, 1, 2, 3, 4, 5}*10 = {0, 10, 20, 30, 40, 50}$ takes only one operation, this should all take one "operation" as well. The savings may not seem like much, but they are __immense__ when dealing with large sets of data. The time difference between an operation on a dataset of, for example, 100,000 items is massive.

### How does one use this magic?

Well, much like many of the wonders of modern society like A/C, pre-sliced bagels, and airline food - it comes down to people who are dedicated to specific libraries! Sure, you can vectorize things yourself in C with SIMD libraries, but it's not like you're writing the machine code to do this - every vectorized operation is syntactic sugar (remember those sweet words?).

#### Base Python

The first, and best, option that comes to mind is the `map` function. The `map` function applies a given function to an entire list, and is very useful to things like type conversion. Here is an example:

```python
input_from_file = ['1.4E04', '2.5E06', '300', '1.23E-05']
numbers = map(float, input_from_file) #this is now a list of floats!
```

This is much faster, and produces much less clutter, than a for loop going over the list changing all the elements!

#### NumPy

Ahhh NumPy - truly one of the best things to happen to Python ever! It's base methods are compiled in C, and so they're super fast!

## Fast Base Python Operations

Sometimes, not everything can be vectorized (sad I know!). However, there are still things that are faster than pure loops over everything, One of those things is called a "_list comprehension_." This is a for loop that resides within a list, i.e.

```python
x = [i*10 for i in x] #x list from earlier with entries from 1 thru 5
[print(i) for i in x] #This would be a list of "None"s, but would print what you want!
```

This is slightly faster since it uses Python generators that are converted to lists because there are brackets around it. The map function, which was pointed out to be a simple speedup tactic, used those same generators. List comprehensions are nice little tools to help speed up your code when you are dealing with lists!