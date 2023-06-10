---
title: Introduction
filename: introduction
chapternum: '0'
numbersections: true
---

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
> There should be one– and preferably only one –obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.\
> Now is better than never.\
> Although never is often better than right now.
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

In keeping with our motto - try and make variable names useful! While it's certainly entertaining to make variable names like "oops", "fucky_wucky", or "my_professor_is_a_dingbat", it's much more useful to you and any other debuggers if the variable names are something like "error_checker", "velocity_list", or "phi1."

And another thing, try not to make variable names the same as types For example, don't make a list with the name list, that's a type! Python will get confused as to whether you're referring to the type or the variable __- remember - _Tu Stultes Es___.

### Functions

Functions in coding are similar to functions in math - they take an input and (sometimes) return an output. Imagine when you see a function that you are replacing the function call with its return value. Functions are one of the most useful things when coding - they allow someone to do something similar over and over again without having to rewrite nearly anything!

Functions in Python are not constrained by many limitations. They need to be defined, and that is really all it is. Why do I say this? Well, in Python, [everything is an object](https://www.pythonmorsels.com/everything-is-an-object/), so anything can be provided as input to a function - even other functions! When would this be useful? Well, let's say you wanted to time a bunch of functions with repetitive code. You _could_ 

### For and While Loops

#### For Loop Basics

For loops in Python are actually all what are known as "for each loops." The basic for loop is just a repeating structure that goes between set values. For instance, a for loop in C++ might look like this:

```C++
for(int i = 0; i < 10; i++){
  cout << i << endl;
}
```

This code block is told to start from an integer initialized at 0, and add 1 to i at each iteration. The loop will keep doing this until the ending condition is no longer satisfied - once $i > 10$ - the loop will end. However, _there is no equivalent in Python_! All loops in Python loop over iterable values. For instance, to do the same thing as the C++ code, you can do the following:

```python
for i in range(10):
  print(i)

#Now let's see an alternate formulation
x = range(10)
for i in x:
  print(i)

#The two things above are functionally the same as what's below
x = [0,1,2,3,4,5,6,7,8,9]
for i in x:
  print(i)
```

Let's deconstruct this. This loop is going to move one at a time through every item in `range(10)`, and set i to that value each time. What `range(10)` does is makes an iterable "range" object containing the numbers 0 through 9, and the for loop will go through that object and set to i at each step. 

#### More Complication with For Loops

Let's now have a more complicated setup. Let's say we wanted to print something as well as its index in a for loop. Here are two ways to do that, one in C++ and one in Python.

```C++
x = [1,2,3]
for(int i = 0; i < 3; i++){
  cout << x[i] << " at index " << i << endl;
}
```

```python
x = [1,2,3]

for i in range(len(x)):
  print(x[i], "at index", i)

for n, i in enumerate(x): #This is a better and more "pythonic" way of doing things
  print(i, "at index", n)
```

_You can unpack variables in python loops!_ Just like we did earlier when assigning variables, assigning temporary variables in for loops works the same. If you were to `print(enumerate(x))`, you would see something that looks like `((0,1), (1,2), (2,3))`, where the first entry is the index the second entry the value at that index. What the for loop is doing at each step is `n, i = (index, value)` and keeping those the same. 

This leads us to the `zip` command. What zip does is it creates tuples you can unpack between two different iterables. Let's say you have two lists you want to iterate over at the same time that are (importantly!) the same length. There are three ways of doing this well, shown below:

```python
x = [1,2,3]
y = ["one", "two", "three"]

#These will print 1 = one, 2 = two, etc.

for i in range(len(x)): #This has nested functions in one line. Might be easy to read, but kind of ugly!
  print(x[i], "=", y[i])

for n, xi in enumerate(x): #Mixing the usage of indices and loop iteration is confusing! Which one is which?
  print(xi, "=", y[n])

for xi,yi in zip(x,y): #easy to understand and type out!
  print(xi, "=", yi) 
```

The same rules apply here as they did for variable assignment! Always take advantage of the way that Python constructs loops so that you don't have to access iterables all the time!

#### While Loops

There's no real difference between while loops in C++ and in Python. A while loop keeps going until it is satisfied. Let's look at an example:

```C++
int i = 0;
while(i < 10){
  cout << i << endl;
  i++;
}
```

```python
i = 0
while i < 10:
  print(i)
  i += 1
```

Notice how you _have_ to iterate i each time the loop progresses. Without this, the condition will never be met, and the while loop will run forever! It is simlarly bad practice to write a while loop that runs forever then breaks manually, such as:

```python
while True:
  some_function()
  #If this was far down in the while loop (say if some_function() was 1000 lines long), it would be hard to find!
  if condition: 
    break #blegh!

while not condition: #This is a much better way of doing things
  # the stop condition is located at the while loop, making it easy to find!
  some_function()
```

While both approaches are technically valid, the second one is bad practice! Should your break statement be somewhere that's not obvious, it could be hard to find/understand! While it might take some overhead, try to always have the primary condition be in the argument of the while loop. Always try to make sure that conditions are explicitly stated, as it both helps readability and bugfixing abilities should things go wrong with you loops!

## Recursion

Recursion in coding is when a function calls itself. Recursive functions need 2 things to really work:

1. Basecase(s).

    Basecases are where the result for some "base" value that the recursive function works down to is a concrete answer. An example of this would be the n=0 and n=1 case of the Fibonacci Sequence.
2. A shrinking size.

    This one might be more "obvious," but it's the cause of many problems when dealing with recursion. To go back to the Fibonacci Sequence, the solution to $F(n)$ is $F(n-1) + F(n-2)$, both of which are inputs smaller than n which work their way down to the base case.

Recursive functions need these two aspects since the size of the problem must keep shrinking down to a known quantity - otherwise recursion will continue infinitely. Some examples of recursive functions are placed in the supplementary Jupyter Notebook.

## Documenting Functions

There are ways to document code in both [C++](https://developer.lsst.io/cpp/api-docs.html) and [Python](https://numpydoc.readthedocs.io/en/latest/format.html). These methods are very important, especially so with Python, since there isn't any type information built into the code! One of the main goals of this course will be to hammer in the necessity of documentation into your skulls!

## Complexity Classes

> _"What is the most efficient way to sort a million 32-bit integers?"_, Eric Schmidt to Barack Obama, 2008
>
> _"I think the bubble sort would be the wrong way to go."_, Barack Obama.

Computational complexity classes are a sets of computational problems of "[related resource-based complexity](https://en.wikipedia.org/wiki/Complexity\_class)." This is a fancy way of saying that problems within the same complexity class take approximately the same time/memory asympototically. This is the basis of large tenets of theoretical computer science, and much work has been done on the subject over the years, with the most famous being the famous [P=NP](https://www.explainxkcd.com/wiki/index.php/287:\_NP-Complete) problem, which asks whether the two complexity classes can be reduced to one another.

![A representation of the relationships between several important complexity classes - courtesy of Google Images](https://www.csc.liv.ac.uk/~ped/teachadmin/algor/pic19.gif)

### Time Complexity

![Graphs of functions commonly used in the analysis of algorithms, showing the number of operations N as the result of input size n for each function - courtesy of Google Images](https://hyperspec.ai/wp-content/uploads/2023/01/3D7CAC80-4CF0-452A-81D5-8540D3C6C8CB.png)

Of course, we will not be discussing these classes in great detail - this is not a [theoretical computer science](https://introtcs.org/public/index.html) text after all! However, what we will be discussing is _time_ complexity - as speed should always be a major factor when thinking about how to write code. Time complexity describes the amount of computer time it takes to run an algorithm - with each "operation" taken to be a _basic_ computational operation (such as addition, subtraction, list indexing, etc.). Other operations like insertion and deletion are not basic operations, and in fact often have runtimes that are nontrivial.

#### Upper Bounds on Time

Since running times can vary wildly by input-size, it is often commonplace to consider the worst-case runtime of a function or an algorithm. Similarly, it's also standard practice to look at asympotic behavior of a given algorithm - this means looking at large input sizes n - such that the difference between something taking 2n time and 16n time isn't really that large of a difference when dealing with large input sizes when compared with something like
$\log(n)$ or $n^2$ time. Placing an upper bound on a given algorithm is given by something called ["Big-O"](https://en.wikipedia.org/wiki/Big\_O\_notation) notation, which is formally defined as such:

$$f(n) \in \mathcal{O}\left(g(n)\right) \implies \left|f(n)\right| \leq c \cdot g(n) \forall n \geq n_0 \in \mathbb{R}$$

This is a very formal way of stating that if you can find a function that is greater than or equal to your runtime (your algorthm's time complexity function "function") for all values of n greater than a some number times any finite constant c, then your function is in $\mathcal{O}(g(n))$.

There's a similar notation known as ["Little-o"](https://en.wikipedia.org/wiki/Big\_O\_notation#Related\_asymptotic\_notations) notation - which is for when something is _strictly_ less than a given function - and the definition changes slightly:

$$f(n) \in \mathcal{o}\left(g(n)\right) \implies \left|f(n)\right| \leq c \cdot g(n) \forall n \geq n_0 \in \mathbb{R}, c > 0$$

There is also a definition for Little-o that involves limits that may be more useful at times:

$$f(n) \in \mathcal{o}\left(g(n)\right) \implies \lim_{n\rightarrow\infty} \frac{f(n)}{g(n)} = 0$$

The difference here is that while Big-O has to be true for at least some constant c, Little-o must hold for every possible positive constant. Little-o then makes a stronger statement about the time complexity - every function $\in \mathcal{o}\left(g(n)\right)$ is also $\in \mathcal{O}\left(g(n)\right)$, however the other way around is not necessarily true (think squares and rectangles!).

#### Lower Bounds on Time

Bounding the time taken by something on the lower end is much less useful, except when it is required to prove that something takes a long time. The notation for these bounds are "Big-Omega" and "Little-Omega", respectively, and are analogs to their upper bound counterparts. This is evidenced by their definitions:

* Big-Omega
  $$f(n) \in \mathcal{\Omega}\left(g(n)\right) \implies \left|f(n)\right| \geq c \cdot g(n) \forall n \geq n\_0 \in \mathbb{R}$$
* Little-Omega
  $$\begin{aligned} f(n) \in \mathcal{\omega}\left(g(n)\right) &\implies \left|f(n)\right| \geq c \cdot g(n) \forall n \geq n\_0 \in \mathbb{R}, c > 0 \\
  f(n) \in \mathcal{\omega}\left(g(n)\right) &\implies \lim\_{n\rightarrow\infty} \frac{f(n)}{g(n)} = \infty \end{aligned}$$

#### Tight Bounds on Time

The real usefulness of a lower bound is when there's what's called a tight bound, or a "Big-Theta" bound, on a process. Tight bounds are useful since Big-O and Big-Omega bounds can be really useless sometimes (i.e. do I really need a notation to tell me that $n^{1\times 10^6} > \log(n)$?) even though the may technically fall into bounds. The definition of Big-Theta relies on the definitions for both Big-Omega and Big-O bounds, as the definition is as follows:

$$f(n) \in \mathcal{\Theta}\left(g(n)\right) \implies f(n) \in \mathcal{\Omega}\left(g(n)\right) \land f(n) \in \mathcal{O}\left(g(n)\right)$$

This means that the $f(n)$ is simultaneously $\geq$ and $\leq$ $g(n)$ for a given $g(n)$, or that they are in the same complexity class! Big-Theta bounds are useful for stating exactly what time complexity class a process is - as it doesn't suffer from the possible overly-generous bounds that are possible with Big-O or Big-Omega bounds.

#### Examples

* Is $n^2 \in \mathcal{\Theta}\left(n^2\right)$?
  $\begin{aligned} |n^2| &\overset{?}{\leq} c \cdot n^2\ 1 &\leq c \text{ for some choice of c } \geq 1\ &\therefore n^2 \in \mathcal{O}\left(n^2\right)\ \ |n^2| &\overset{?}{\geq} c \cdot n^2\ 1 &\geq c \text{ for some choice of c} \leq 1\ &\therefore n^2 \in \mathcal{\Omega}\left(n^2\right)\ \end{aligned} $ Since $n^2$ is in both bounds, $n^2 \in \mathcal{\Theta}\left(n^2\right)$.
* Is $\log(n) \in \mathcal{o}\left(n^\epsilon\right)$, where $\epsilon$ is any real number > 0? 
$$\begin{aligned}
\lim_{n\rightarrow\infty}\frac{\log(n)}{n^\epsilon} &= 0 \forall \epsilon > 0 \implies \log(n) \in \mathcal{o}(n^\epsilon) \forall \epsilon > 0\\
L.H.S.: &\lim_{n\rightarrow\infty}\frac{\log(n)}{n^\epsilon}\\
&= \lim_{n\rightarrow\infty} \frac{\epsilon\log(n^\frac{1}{\epsilon})}{n^\epsilon}\\
&< \lim_{n\rightarrow\infty} \frac{\epsilon n^\frac{1}{\epsilon}}{n^\epsilon}\\
&= \lim_{n\rightarrow\infty} \frac{\epsilon}{n^{\epsilon - \frac{1}{\epsilon}}} = 0\\
&\therefore \log(n) \in \mathcal{o}\left(n^\epsilon\right) \forall \epsilon > 0\end{aligned}$$

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

Another useful tool is the recursion tree. The Fibonacci function is actually _very_ costly, with a runtime of about $\mathcal{O}\left(2^n\right)$ - which is not obvious at all! Looking at the recursion tree, however, clues you into why this is the case:

![Recursion tree for the Fibonacci Sequence](https://i.stack.imgur.com/QVSdv.png)

For a Fibonacci tree, the height of the tree is proportional to the input number (aka the input "size"). There are on the order of $2^n$ "leaves," or endpoints, of this tree - meaning that the runtime is $2^n\times 1 = 2^n$! This is super slow!

### The Master Theorem

The Master Theorem is a useful method for determining the runtime of recurrence relations that contain division of the sample space in some way. It is given by the following, for equations of the form $f(n) = a f\left(\frac{n}{b}\right) + g(n)$:

$$
\begin{cases} g(n) \in \mathcal{\Theta}(n^c) \text{ for some } c < \log_b(a) \qquad \implies f(n) \in \mathcal{\Theta}(n^{\log_b(a)})\\ g(n) \in \mathcal{\Theta}(n^c) \text{ for some } c = \log_b(a) \qquad \implies f(n) \in \mathcal{\Theta}(n^c\log(n))\\ g(n) \in \mathcal{\Theta}(n^c) \text{ for some } c > \log_b(a) \qquad \implies f(n) \in \mathcal{\Theta}(g(n)) \end{cases}
$$

Each case is an illustration of what terms dominate in the calculations with regards to the recursion tree. In the first case, the actual calculations are relatively inexpensive, so the main contribution to the runtime is the number of divisions itself. In the second case, the constribution from the number of divisions and the contribution from the calculation at each level are about the same. In the third case, the calculation at each level dominates the runtime.

## Exercises

### 1) Recursion

1. Write a simple function called `fib(n)` that calculates the Fibonacci numbers in Python recursively. Run your code over a range of values from 1 to 25, and try plotting the runtimes of each in a line. What does it look like? ___HINT:What is/are the base case(s) of the Fibonacci Sequence?___
2. One of the major drawbacks to basic recursion is that values have to calculated repeatedly. For instance, in the Fibonacci sequence,

$$\begin{aligned}
  Fibonacci(n) &= Fibonacci(n-1) + Fibonacci(n-2) + ...\\
   &= (Fibonacci(n-2) + Fibonacci(n-3)) + (Fibonacci(n-3) + Fibonacci(n-4)) + ...
\end{aligned}$$

and so on. This wastes computational time! Is there a way that you can think of to speed this process up? Implement it and compare the time of your new function with `fib(n)` from part 1. ___HINT:It involves storing values.___

1. Congratulations! You have now discovered [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic\_programming), an extremely powerful algorithmic tool for solving complex problems that have [optimal substructure](https://en.wikipedia.org/wiki/Optimal\_substructure). What is the spatial complexity of your dynamic programming approach? Plot the runtimes of this algorithm versus the original one for the same range of values. ___HINT:Use Matplotlib to plot your values___

### 2) Loops

1. Given a list x, write two functions that take a string in and determine whether or not is it a [palindrome](https://en.wikipedia.org/wiki/Palindrome). Name one function `for_f` (and use a for loop to do this), and another `while_f` (using a while loop to do this)
2. Given three lists, one of data in the form `[ [((x1(t0),y1(t0)), (x1(t0)',y1(t0)'), (x1(t0)'',y1(t0)'')), ...], ...]` (the 2d position, velocity, and acceleration for multiple objects), one detailing the time values of t0, t1, etc. for each list (`[ [t0, t1, ...], ... ]`), and another list listing the labels for each object in list 1, plot the position, velocity, and acceleration of each for the range of t values using at ___most___ two for loops. place this in a function `visualize(data, labels, times)`, and save the output to `trajectories.png`. ___HINT: Try unpacking and zipping values!___

### 3) Floating Point Accuracy

1. The following code block calculates $e^{-x}$ via its Taylor Series, however it is wildly inaccurate even for small integers. The reason is that this code is not good for maintaining the accuracy of a floating point number. Try and improve upon it, and compare it to the value returned by `exp(-x)` (which is well optimized for accuracy!). Afterwards, implement the C++ code below in Python, and notice how the same problem does _not_ occur ___HINT:Accuracy breaks down for really large numbers - maybe scaling down then scaling back up somehow would help? Similarly, try an iterative approach to calculating the sum, it's much easier for C++ to do $x^6*x$ than $x^7$.___

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

### 4) Algorithm Analysis

1. Given a pair of positive integers a and n, provide pseudo-code for a function `eff_exp(a, n)` that computes $a^n$ using only $\mathcal{O}(\log(n))$ multiplications. Prove that `eff_exp` $\in \mathcal{O}(\log(n))$. Assume that every operation (i.e. addition, multiplication) takes 1 "operation."
2. Consider the following code block that permutes an array A of size n (remembering that ranges in python are integer ranges from $[start, end)$ ):

```python
def permute(A):
    for i in range(n):
        Swap(A[i], A[random.randrange(0,n)])
    return A
```

Show that for any $n > 2$ all permutations are not equally probable. ___HINT:Something is not equally probable if the number of possible outcomes is not evenly divisible by the number of permutations___
