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

If you do not know Python or C++, fear not! This text will not be covering *how* to code, I am assuming that you know *a priori* how to code in at least one of the two languages.


## Complexity Classes

>_"What is the most efficient way to sort a million 32-bit integers?"_, Eric Schmidt to Barack Obama, 2008
>
>_"I think the bubble sort would be the wrong way to go."_, Barack Obama.

## Exercises

### 1) Recursion

1. Write a simple function called `fact(n)` that calculates the Fibonacci numbers - one in C++ and one in Python - recursively. Is there a difference in the runtime between n=20 and n=50? ***HINT:** What is/are the base case(s) of the Fibonacci Sequence?*
	 
2. One of the major drawbacks to basic recursion is that values have to calculated repeatedly. For instance, in the Fibonacci sequence, $Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)= (Fibonacci(n-2) + Fibonacci(n-3)) + (Fibonacci(n-3) + Fibonacci(n-4))$ and so on. This wastes computational time! Is there a way that you can think of to speed this process up? Implement it and compare the time of your new function with `fact(n)` from part 1. ***HINT:** It involves storing values.*
	 
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
1. Given a pair of positive integers a and n, provide pseudo-code for a function `eff_exp(a, n)` that computes $a^n$ using only $\mathcal{O}(\log(n))$ multiplications. Prove that `eff_exp` $\in \mathcal{O}(\log(n))$. Assume that every operation (i.e. addition, multiplication) takes 1 "operation."
	 
2. Consider the following code block that permutes an array A of size n (remembering that ranges in python are integer ranges from $[start, end)$ ):
```python
def permute(A):
    for i in range(n):
        Swap(A[i], A[random.randrange(0,n)])
    return A
```
Show that for any $n > 2$ all permutations are not equally probable. Devise your own permute function that makes sure every permutation is equally probable. ***HINT:* Something is equally probable if the permutations are evenly divisible with the number of outcomes**