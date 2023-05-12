---
title: Introduction
filename: introduction
chapternum: '0'
numbersections: true
---

# Introduction

> "Beautiful is better than ugly.\
> Explicit is better than implicit.\
> Simple is better than complex.\
> Complex is better than complicated.\
> Flat is better than nested.\
> Sparse is better than dense.\
> Readability counts.\
> Special cases aren't special enough to break the rules.\
> Although practicality beats purity.\
> Errors should never pass silently.\
> Unless explicitly silenced.\
> In the face of ambiguity, refuse the temptation to guess.\
> There should be one– and preferably only one –obvious way to do it.[\[a\]](https://en.wikipedia.org/wiki/Zen\_of\_Python#cite\_note-7)\
> Although that way may not be obvious at first unless you're Dutch.\
> Now is better than never.\
> Although never is often better than right now.[\[b\]](https://en.wikipedia.org/wiki/Zen\_of\_Python#cite\_note-8)\
> If the implementation is hard to explain, it's a bad idea.\
> If the implementation is easy to explain, it may be a good idea.\
> Namespaces are one honking great idea – let's do more of those!"\
> [_PEP (Python Enhancement Proposal) 20 - the Zen of Python_](https://peps.python.org/pep-0020/)

> "We’ve heard computer science PhDs explain they were embarrassed to know Python 'because it’s a language for idiots.'", [Model View Culture](https://modelviewculture.com/pieces/c-is-manly-python-is-for-n00bs-how-false-stereotypes-turn-into-technical-truths)

> "The major cause of complaints is C++ undoubted success. As someone remarked: There are only two kinds of programming languages: those people always bitch about and those nobody uses.", [Bjarne Stroustrup](https://en.wikipedia.org/wiki/Bjarne\_Stroustrup)

> "If you want a fancier language, C++ is absolutely the worst one to choose. If you want real high-level, pick one that has true high-level features like garbage collection or a good system integration, rather than something that lacks both the sparseness and straightforwardness of C, and doesn't even have the high-level bindings to important concepts.",[Linus Torvalds](https://en.wikipedia.org/wiki/Linus\_Torvalds)

## OBJECTIVES

* Briefly compare Python and C++
  * variable assignment
  * function declarations
* Recursion
* Complexity Classes
  * Time Complexity

Before the text starts getting into the ins and outs of using python to do analyses - one must first have a good grasp of some basic ideas about how to look at problems in coding. This chapter serves as an introduction to the concepts relating to functions and their analysis.

***

## Resources to Get Started

If you do not know Python or C++, fear not! This text will not be covering _how_ to code, I am assuming that you know _a priori_ how to code in Python, and at least know that C++ exists. There is just simply too much to cover in terms of programming knowledge to teach an entire programming language (there are bootcamps for that!). However, there are many resources available online to learn how to code - as well as your peers around you!

### Supplementary Jupyter Notebook

Trying to break a coding language is one of the fastest ways to learn a programming language. For each chapter, there is a supplementary Jupyter Notebook designed for exploration of certain concepts covered in the chapter - it is my recommendation that you use them to just try things out!

## Starting with Python

### Variable Assignment

In Python, variables can take any form that you would like. This isn't great for documentation purposes, but there are ways to document types without being as strict as C++. Similarly, in Python, you can "unpack" variables from iterable quantities, which is also shown below:

```python
x = 10
x = 1e6 #This is how you do scientific notation in python
x = "HELLO" #This code will work fine - python does not do typing like C++ does - which is one reason it's so flexible.
x, y, z = [1,2,3]
(w, x), (y, z) = [(0,1), (2,3)] #Here the extra parentheses are needed, as the list only has 2 items, and without the parentheses to evaluate the pairs separately, Python would expect 4 items in the list and throw an error.
```

### Functions

Functions in coding are similar to functions in math - they take an input and (sometimes) return an output. Imagine when you see a function that you are replacing the function call with its return value. Functions are one of the most useful things when coding - they allow someone to do something similar over and over again without having to rewrite nearly anything!

Functions in Python are not constrained by many limitations. They need to be defined, and that is really all it is.

### Useful Data Structures

TODO: cover lists, dictionaries, maps, ranges

### For and While Loops

## Recursion

Recursion in coding is when a function calls itself. Recursive functions need 2 things to really work:

1.  Basecase(s).

    Basecases are where the result for some "base" value that the recursive function works down to is a concrete answer. An example of this would be the n=0 and n=1 case of the Fibonacci Sequence.
2.  A shrinking size.

    This one might be more "obvious," but it's the cause of many problems when dealing with recursion. To go back to the Fibonacci Sequence, the solution to $F(n)$ is $F(n-1) + F(n-2)$, both of which are inputs smaller than n which work their way down to the base case.

Recursive functions need these two aspects since the size of the problem must keep shrinking down to a known quantity - otherwise recursion will continue infinitely. Some examples of recursive functions are placed in the supplementary Jupyter Notebook.

## Documenting Functions

There are ways to document code in both [C++](https://developer.lsst.io/cpp/api-docs.html) and [Python](https://numpydoc.readthedocs.io/en/latest/format.html). These methods are very important, especially so with Python, since there isn't any type information built into the code! One of the main goals of this course will be to hammer in the necessity of documentation into your skulls!

## Complexity Classes

> _"What is the most efficient way to sort a million 32-bit integers?"_, Eric Schmidt to Barack Obama, 2008
>
> _"I think the bubble sort would be the wrong way to go."_, Barack Obama.

Computational complexity classes are a sets of computational problems of "[related resource-based complexity](https://en.wikipedia.org/wiki/Complexity\_class)." This is a fancy way of saying that problems within the same complexity class take approximately the same time/memory asympototically. This is the basis of large tenets of theoretical computer science, and much work has been done on the subject over the years, with the most famous being the famous [P=NP](https://www.explainxkcd.com/wiki/index.php/287:\_NP-Complete) problem, which asks whether the two complexity classes can be reduced to one another.

![A representation of the relationships between several important complexity classes - courtesy of Wikipedia](https://en.wikipedia.org/wiki/Complexity\_class#/media/File:Complexity\_subsets\_pspace.svg)

### Time Complexity

![Graphs of functions commonly used in the analysis of algorithms, showing the number of operations N as the result of input size n for each function - courtesy of Wikipedia](https://en.wikipedia.org/wiki/Time\_complexity#/media/File:Comparison\_computational\_complexity.svg)

Of course, we will not be discussing these classes in great detail - this is not a [theoretical computer science](https://introtcs.org/public/index.html) text after all! However, what we will be discussing is _time_ complexity - as speed should always be a major factor when thinking about how to write code. Time complexity describes the amount of computer time it takes to run an algorithm - with each "operation" taken to be a _basic_ computational operation (such as addition, subtraction, list indexing, etc.). Other operations like insertion and deletion are not basic operations, and in fact often have runtimes that are nontrivial.

#### Upper Bounds on Time

Since running times can vary wildly by input-size, it is often commonplace to consider the worst-case runtime of a function or an algorithm. Similarly, it's also standard practice to look at asympotic behavior of a given algorithm - this means looking at large input sizes n - such that the difference between something taking 2n time and 16n time isn't really that large of a difference when dealing with large input sizes when compared with something like $\log(n)$ or $n^2$ time. Placing an upper bound on a given algorithm is given by something called ["Big-O"](https://en.wikipedia.org/wiki/Big\_O\_notation) notation, which is formally defined as such:

$$f(n) \in \mathcal{O}\left(g(n)\right) \implies \left|f(n)\right| \leq c \cdot g(n) \forall n \geq n_0 \in \mathbb{R}$$

This is a very formal way of stating that if you can find a function that is greater than or equal to your runtime (your algorthm's time complexity function "function") for all values of n greater than a some number times any finite constant c, then your function is in $\mathcal{O}(g(n))$.

There's a similar notation known as ["Little-o"](https://en.wikipedia.org/wiki/Big\_O\_notation#Related\_asymptotic\_notations) notation - which is for when something is _strictly_ less than a given function - and the definition changes slightly:

$$f(n) \in \mathcal{o}\left(g(n)\right) \implies \left|f(n)\right| \leq c \cdot g(n) \forall n \geq n_0 \in \mathbb{R}, c > 0$$ There is also a definition for Little-o that involves limits that may be more useful at times:

$$f(n) \in \mathcal{o}\left(g(n)\right) \implies \lim_{n\rightarrow\infty} \frac{f(n)}{g(n)} = 0$$

The difference here is that while Big-O has to be true for at least some constant c, Little-o must hold for every possible positive constant. Little-o then makes a stronger statement about the time complexity - every function $\in \mathcal{o}\left(g(n)\right)$ is also $\in \mathcal{O}\left(g(n)\right)$, however the other way around is not necessarily true (think squares and rectangles!).

#### Lower Bounds on Time

Bounding the time taken by something on the lower end is much less useful, except when it is required to prove that something takes a long time. The notation for these bounds are "Big-Omega" and "Little-Omega", respectively, and are analogs to their upper bound counterparts. This is evidenced by their definitions:

* Big-Omega $ f(n) \in \mathcal{\Omega}\left(g(n)\right) \implies \left|f(n)\right| \geq c \cdot g(n) \forall n \geq n\_0 \in \mathbb{R} $
* Little-Omega $ \begin{aligned} f(n) \in \mathcal{\omega}\left(g(n)\right) &\implies \left|f(n)\right| \geq c \cdot g(n) \forall n \geq n\_0 \in \mathbb{R}, c > 0 \ f(n) \in \mathcal{\omega}\left(g(n)\right) &\implies \lim\_{n\rightarrow\infty} \frac{f(n)}{g(n)} = \infty \end{aligned} $

#### Tight Bounds on Time

The real usefulness of a lower bound is when there's what's called a tight bound, or a "Big-Theta" bound, on a process. Tight bounds are useful since Big-O and Big-Omega bounds can be really useless sometimes (i.e. do I really need a notation to tell me that $n^{1\times 10^6} > \log(n)$?) even though the may technically fall into bounds. The definition of Big-Theta relies on the definitions for both Big-Omega and Big-O bounds, as the definition is as follows:

$$f(n) \in \mathcal{\Theta}\left(g(n)\right) \implies f(n) \in \mathcal{\Omega}\left(g(n)\right) \And f(n) \in \mathcal{O}\left(g(n)\right)$$

This means that the $f(n)$ is simultaneously $\geq$ and $\leq$ $g(n)$ for a given $g(n)$, or that they are in the same complexity class! Big-Theta bounds are useful for stating exactly what time complexity class a process is - as it doesn't suffer from the possible overly-generous bounds that are possible with Big-O or Big-Omega bounds.

#### Examples

* Is $n^2 \in \mathcal{\Theta}\left(n^2\right)$? $ \begin{aligned} |n^2| &\overset{?}{\leq} c \cdot n^2\ 1 &\leq c \text{ for some choice of c } \geq 1\ &\therefore n^2 \in \mathcal{O}\left(n^2\right)\ \ |n^2| &\overset{?}{\geq} c \cdot n^2\ 1 &\geq c \text{ for some choice of c} \leq 1\ &\therefore n^2 \in \mathcal{\Omega}\left(n^2\right)\ \end{aligned} $ Since $n^2$ is in both bounds, $n^2 \in \mathcal{\Theta}\left(n^2\right)$.
* Is $\log(n) \in \mathcal{o}\left(n^\epsilon\right)$, where $\epsilon$ is any real number > 0? $ \begin{aligned} \lim\_{n\rightarrow\infty}\frac{\log(n)}{n^\epsilon} &= 0 \forall \epsilon > 0 \implies \log(n) \in \mathcal{o}(n^\epsilon) \forall \epsilon > 0\ L.H.S.: &\lim\_{n\rightarrow\infty}\frac{\log(n)}{n^\epsilon}\ &= \lim\_{n\rightarrow\infty} \frac{\epsilon\log(n^\frac{1}{\epsilon})}{n^\epsilon}\ &< \lim\_{n\rightarrow\infty} \frac{\epsilon n^\frac{1}{\epsilon\}}{n^\epsilon}\ &= \lim\_{n\rightarrow\infty} \frac{\epsilon}{n^{\epsilon - \frac{1}{\epsilon\}}} = 0\ &\therefore \log(n) \in \mathcal{o}\left(n^\epsilon\right) \forall \epsilon > 0 \end{aligned} $

#### Determining Time Complexity

So a bunch of math stuff has been convered, but how does someone really tell when something is a certain time complexity? Well, there are a few simple ways. Imagine giving your algorithm some input of size n, and think about how many times your algorithm goes through those elements. For example, if there was some code that looked like this

```python
for i in range(n):
  for j in range(n):
    do_something()
```

it would be a process that takes $\mathcal{\Theta}(n^2)$ time. It takes practice to develop an intuition for it, but it's best to think about how many times something is computed over in the worst case to judge the runtime. For instance, in the example above, a nested for loop means that there are n operations done n times, making for a runtime of $n^2$.

There are other analyses of code timing, such as [amortized](https://en.wikipedia.org/wiki/Amortized\_analysis) time and [average](https://en.wikipedia.org/wiki/Average-case\_complexity) time, but they will not be covered in this text. However, should algorithm analysis prove to be something you enjoy, please look into it! It's very interesting stuff!

If you'd like more information on determining time complexity in a real and applicable way, this [Stack Overflow](https://stackoverflow.com/questions/3255/big-o-how-do-you-calculate-approximate-it) post from 2008 is a really good starting point.

### Space Complexity

Much like time complexity, there is also space complexity. The categorizations are _exactly_ the same as the time complexity bounds (Big-O, Big-Omega, Big-Theta, etc.), however this deals with the amount of memory required for an algorithm. For example - using a $n\times n$ sized cartesian grid to simulate something (like maybe a Boundary-Value Problem from Electrodynamics) - takes $\mathcal{\Theta}\left(n^2\right)$ memory. While not used as often as time complexity in everyday analysis - especially since space has become more plentiful on modern computers - it's still a useful quantity to measure.

## Basic Recursive Analysis

### Recursion Relations

Another useful tool to think about is to combine time complexity and recursion. These come in the form of recursion relations - and are expressed in functional form. Going back to the Fibonacci Sequence, the recurrence relation looks as such: $$f(n) = f(n - 1) + f(n - 2) + \mathcal{O}\left(1\right), \quad f(0) = f(1) = 1$$ What this equation means is that to calculate the function for a value n, the value at $(n - 1)$ and $(n - 2)$ must also be calculated, with one additional operation (addition). The basecases are then listing the time required for the basecases, such that an end is defined. Keep in mind that the numbers provided are not the answer to the function, but rather the amount of time it takes for the function to run, or the number of operations! As long as this time is within the same asympotic bound (i.e. all constant time steps go to 1) it is _usually_ okay.

For "divide and conquer" algorithms - which are useful tools for a wide range of problems - recursion relations may look more like the following: $$f(n) = f\left(\frac{n}{2}\right) + g(n)$$ Where c is a constant. This recursion relation means that to calculate the function at a value of n, the value at $\frac{n}{2}$ must also be calculated. The function g(n) is some function that indicates how many operations are done at every step of recursion - it can be anything ranging from a constant, like in the Fibonacci relation, to any other function like $n!$.

### Determining Runtime

For recursion, it is a bit harder to think about the runtime in the same way that an iterative solution would. Imagine two functions that are used to print a list starting from a specific index, shown below:

```python
def print_list_iterative(lst, i):
  for i in range(i, len(lst)):
    print(lst[i])
  return

def print_list_recursive(lst, i):
  if i >= len(lst):
    return
  print(lst[i]) #There is no need for an else statement since a function will end at the return statement
  print_list_recursion(lst, i+1) #notice how this is recursing "upwards" to a basecase. This is still okay since the sample space is decreasing!
```

Taking the size n to be the size of the list starting at index i, the runtime of the iterative function can be taken to be $\mathcal{\Theta}(n)$. The recursive function also takes $\mathcal{\Theta}(n)$, but it may be harder to see that. It helps to then think about the number of operations something has to do in the recurrence relation, which in this case is $f(i) = f(i+1) + 1, f(n) = 1$. Due to our definition of n, this function would take n recursion steps. Since each step takes 1 operation, the runtime looks as follows: $$f(i) = \sum_{i}^n 1 = n \in \mathcal{\Theta}(n)$$

Another useful tool is the recursion tree. The Fibonacci function is actually _very_ costly, with a runtime of about $\mathcal{O}\left(2^n\right)$ - which is not obvious at all! Looking at the recursion tree, however, clues you into why this is the case: ![Recursion tree for the Fibonacci Sequence](https://i.stack.imgur.com/QVSdv.png) For a Fibonacci tree, the height of the tree is proportional to the input number (aka the input "size"). There are on the order of $2^n$ "leaves," or endpoints, of this tree - meaning that the runtime is $2^n\times 1 = 2^n$! This is super slow!

### The Master Theorem

The Master Theorem is a useful method for determining the runtime of recurrence relations that contain division of the sample space in some way. It is given by the following, for equations of the form $f(n) = a f\left(\frac{n}{b}\right) + g(n)$:

$$
\begin{cases} g(n) \in \mathcal{\Theta}(n^c) \text{ for some } c < \log_b(a) \qquad \implies f(n) \in \mathcal{\Theta}(n^{\log_b(a)})\\ g(n) \in \mathcal{\Theta}(n^c) \text{ for some } c = \log_b(a) \qquad \implies f(n) \in \mathcal{\Theta}(n^c\log(n))\\ g(n) \in \mathcal{\Theta}(n^c) \text{ for some } c > \log_b(a) \qquad \implies f(n) \in \mathcal{\Theta}(g(n)) \end{cases}
$$

Each case is an illustration of what terms dominate in the calculations with regards to the recursion tree. In the first case, the actual calculations are relatively inexpensive, so the main contribution to the runtime is the number of divisions itself. In the second case, the constribution from the number of divisions and the contribution from the calculation at each level are about the same. In the third case, the calculation at each level dominates the runtime.

## Exercises

### 1) Recursion

1. Write a simple function called `fib(n)` that calculates the Fibonacci numbers in Python recursively. Run your code over a range of values from 1 to 25, and try plotting the runtimes of each in a line. What does it look like? _**HINT:**_** What is/are the base case(s) of the Fibonacci Sequence?**
2. One of the major drawbacks to basic recursion is that values have to calculated repeatedly. For instance, in the Fibonacci sequence, $Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)= (Fibonacci(n-2) + Fibonacci(n-3)) + (Fibonacci(n-3) + Fibonacci(n-4))$ and so on. This wastes computational time! Is there a way that you can think of to speed this process up? Implement it and compare the time of your new function with `fact(n)` from part 1. _**HINT:**_** It involves storing values.**
3. Congratulations! You have now discovered [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic\_programming), an extremely powerful algorithmic tool for solving complex problems that have [optimal substructure](https://en.wikipedia.org/wiki/Optimal\_substructure). What is the spatial complexity of your dynamic programming approach? Plot the runtimes of this algorithm versus the original one for the same range of values. _**HINT:**_** Use Matplotlib to plot your values**

### 2) Floating Point Accuracy

1. The following code block calculates $e^{-x}$ via its Taylor Series (using the factorial function you created in Problem 1!), however it is wildly inaccurate even for small integers. The reason is that this code is not good for maintaining the accuracy of a floating point number. Try and improve upon it, and compare it to the value returned by `exp(-x)` (which is well optimized for accuracy!). Afterwards, implement the C++ code below in Python, and notice how the same problem does _not_ occur _**HINT:**_** Accuracy breaks down for really large numbers - maybe scaling down then scaling back up somehow would help? Similarly, try an iterative approach to calculating the sum, it's much easier for C++ to do $x^6\*x$ than $x^7$.**

```cpp
const int MAXIT=10000;
const double EPS=1e-9;
long double mexp(double x){
    long double value=1.0;
    int sign;
    for (int n=1;n<MAXIT;n++){
        if(i%2 == 0){
            sign = 1;
        } else{
            sign = -1;
        }
        long double term=sign*pow(x,n)/fact(n); // This line is the issue!
        value += term;
        if (fabs(term/value) < EPS || !isfinite(value) ) break;
    }
    return value;
}
```

### 3) Algorithm Analysis

1. Given a pair of positive integers a and n, provide pseudo-code for a function `eff_exp(a, n)` that computes $a^n$ using only $\mathcal{O}(\log(n))$ multiplications. Prove that `eff_exp` $\in \mathcal{O}(\log(n))$. Assume that every operation (i.e. addition, multiplication) takes 1 "operation."
2. Consider the following code block that permutes an array A of size n (remembering that ranges in python are integer ranges from $\[start, end)$ ):

```python
def permute(A):
    for i in range(n):
        Swap(A[i], A[random.randrange(0,n)])
    return A
```

Show that for any $n > 2$ all permutations are not equally probable. _**HINT:**_** Something is not equally probable if the number of possible outcomes is not evenly divisible by the number of permutations**
