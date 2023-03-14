---
title: "Introduction"
filename: "introduction"
chapternum: "0"
numbersections: true
---

# Introduction {#introchap}

>_"Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one– and preferably only one –obvious way to do it.[[a]](https://en.wikipedia.org/wiki/Zen_of_Python#cite_note-7)  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than right now.[[b]](https://en.wikipedia.org/wiki/Zen_of_Python#cite_note-8)  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea – let's do more of those!"_  
[*PEP (Python Enhancement Proposal) 20 - the Zen of Python*](https://peps.python.org/pep-0020/) 


>_"We’ve heard computer science PhDs explain they were embarrassed to know Python 'because it’s a language for idiots.'"_, [Model View Culture](https://modelviewculture.com/pieces/c-is-manly-python-is-for-n00bs-how-false-stereotypes-turn-into-technical-truths)


>_"The major cause of complaints is C++ undoubted success. As someone remarked: There are only two kinds of programming languages: those people always bitch about and those nobody uses."_, [Bjarne Stroustrup](https://en.wikipedia.org/wiki/Bjarne_Stroustrup)

>_"If you want a fancier language, C++ is absolutely the worst one to choose. If you want real high-level, pick one that has true high-level features like garbage collection or a good system integration, rather than something that lacks both the sparseness and straightforwardness of C, and doesn't even have the high-level bindings to important concepts."_,[Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)


**OBJECTIVES**

* Briefly compare Python and C++
	* variable assignment
	* function declarations
* Cover Recursion
* Complexity Classes
---

## Resources to Get Started

If you do not know Python or C++, fear not! This text will not be covering *how* to code, I am assuming that you know *a priori* how to code in at least one of the two languages. This overview will be very brief, and is certainly not something to be used to learn how to code.

## Basic Differences Between the Two Languages
There are some key differences between the way that Python works and the way that C++ works. Python is an *interpreted* language, which means that it checks for failures as it goes, whereas C++ is a *compiled* language, which means that there is a compile step where variables and language are checked before the code is run. This has many effects on the language - this section will cover variable assignment and function declaration. 

### Variable Assignment
#### C++
C++ has what is known as a statically typed language - the types are declared explicitly to assign variables. To assign a variable, there needs to be a type in front i.e.
```cpp
int x = 10;
long double y = 1e6;
string z = "HELLO"
x = "I CAN'T DO THIS"; //This will break. The string you are trying to assign it to doesn't exist.
```
#### Python
In Python, however, variables can take any form that you would like. This isn't great for documentation purposes, but there are ways to document types without being as strict as C++. Similarly, in Python, you can "unpack" variables from iterable quantities, which is also shown below:
```python
x = 10
x = 1e6
x = "HELLO" #This code will work fine - python does not do typing like C++ does - which is one reason it's so flexible.
x, y, z = [1,2,3]
(w, x), (y, z) = [(0,1), (2,3)] #Here the extra parentheses are needed, as the list only has 2 items, and without the parentheses to evaluate the pairs separately, Python would expect 4 items in the list and throw an error.
```

## Functions

Functions in coding are similar to functions in math - they take an input and (sometimes) return an output. Imagine when you see a function that you are replacing the function call with its return value. Functions are one of the most useful things when coding - they allow someone to do something similar over and over again without having to rewrite nearly anything!

### C++
Similar to variables, functions *need* to have types in C++. This becomes very tricky when functions start returning complex values like datatypes or arrays without explicit sizes, but it's nice to know what a function will return with certainty (if a function does not return anything its type will be `void`). Similarly, functions in C++ can be *overloaded.* What this means is you can have the same function with a different signature, and C++ will know it's a different function. This is how you can get C++ to do the same thing to different data types, i.e.:

```cpp
void square(double &x){ //here a reference to x is being passed, so x will be changed from where you declared it
    x *= x;
}

double square(double x){
    return x*x;
}
int square(double x){
    return (int)(x*x); //Here the result is cast to be an integer, and even though the function input is the same, C++ will know it's a different function. 
}
```
### Python
Functions in Python are not constrained by many limitations. They need to be defined, and that is really all it is.

### Recursion
Recursion in coding is when a function calls itself. Recursive functions need 2 things to really work:
1. Basecase(s). 
   
   Basecases are where the result for some "base" value that the recursive function works down to is a concrete answer. An example of this would be the n=0 and n=1 case of the Fibonacci Sequence.

2. A shrinking size. 
   
   This one might be more "obvious," but it's the cause of many problems when dealing with recursion. 

### Documenting Functions
There are ways to document code in both [C++](https://developer.lsst.io/cpp/api-docs.html) and [Python](https://numpydoc.readthedocs.io/en/latest/format.html). These methods are very important, especially so with Python, since there isn't any type information built into the code! One of the main goals of this course will be to hammer in the necessity of documentation into your skulls!

## Common Errors

## Complexity Classes and Basic Recursive Analysis

>_"What is the most efficient way to sort a million 32-bit integers?"_, Eric Schmidt to Barack Obama, 2008
>
>_"I think the bubble sort would be the wrong way to go."_, Barack Obama.

## Exercises

### 1) Recursion

1. Write a simple function called `fact(n)` that calculates the Fibonacci numbers - one in C++ and one in Python - recursively. Is there a difference in the runtime between n=10 and n=30? ***HINT:** What is/are the base case(s) of the Fibonacci Sequence?*
	 
2. One of the major drawbacks to basic recursion is that values have to calculated repeatedly. For instance, in the Fibonacci sequence, $Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)= (Fibonacci(n-2) + Fibonacci(n-3)) + (Fibonacci(n-3) + Fibonacci(n-4))$ and so on. This wastes computational time! Is there a way that you can think of to speed this process up? Implement it in one language of your choice and compare the time of your new function with `fact(n)` from part 1 using the numbers provided. Timing can be done using [perf counter](https://docs.python.org/3/library/time.html#time.perf_counter). ***HINT:** It involves global variables.*
	 
3. Congratulations! You have now discovered [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming), an extremely powerful algorithmic tool for solving complex problems that have [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure).

### 2) Floating Point Accuracy

1. The following code block calculates $e^{-x}$ via its Taylor Series (using the factorial function you created in Problem 1!), however it is wildly inaccurate even for small integers. The reason is that this code is not good for maintaining the accuracy of a floating point number. Try and improve upon it, and compare it to the value returned by `exp(-x)` (which is well optimized for accuracy!). ***HINT:** Accuracy breaks down for really large numbers - maybe scaling down then scaling back up somehow would help? Similarly, try an iterative approach to calculating the sum, it's much easier for C++ to do $x^6*x$ than $x^7$.*

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
1. Given a pair of positive integers a and n, provide pseudo-code for a function `eff_exp(a, n)` that computes $a^n$ using only $\mathcal{O}(\log(n))$ multiplications. Prove that `eff_exp` $\in \mathcal{O}(\log(n))$. Assume that every operation (i.e. addition, multiplication) takes 1 "operation." ***HINT:* Use the Master Theorem**
	 
2. Consider the following code block that permutes an array A of size n (remembering that ranges in python are integer ranges from $[start, end)$ ):
```python
def permute(A):
    for i in range(n):
        Swap(A[i], A[random.randrange(0,n)])
    return A
```
Show that for any $n > 2$ all permutations are not equally probable. Devise your own permute function that makes sure every permutation is equally probable. ***HINT:* Something is equally probable if the permutations are evenly divisible with the number of outcomes**