---
title: "Introduction"
filename: "introduction"
chapternum: "0"
numbersections: true
---

# Introduction {#introchap}

>"Beautiful is better than ugly.  
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
Namespaces are one honking great idea – let's do more of those!"  
[_PEP (Python Enhancement Proposal) 20 - the Zen of Python_](https://peps.python.org/pep-0020/)


>"We’ve heard computer science PhDs explain they were embarrassed to know Python 'because it’s a language for idiots.'", [Model View Culture](https://modelviewculture.com/pieces/c-is-manly-python-is-for-n00bs-how-false-stereotypes-turn-into-technical-truths)


>"The major cause of complaints is C++ undoubted success. As someone remarked: There are only two kinds of programming languages: those people always bitch about and those nobody uses.", [Bjarne Stroustrup](https://en.wikipedia.org/wiki/Bjarne_Stroustrup)


>"If you want a fancier language, C++ is absolutely the worst one to choose. If you want real high-level, pick one that has true high-level features like garbage collection or a good system integration, rather than something that lacks both the sparseness and straightforwardness of C, and doesn't even have the high-level bindings to important concepts.",[Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)

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

Computational complexity classes are a sets of computational problems of "[related resource-based complexity](https://en.wikipedia.org/wiki/Complexity_class)." This is a fancy way of saying that problems within the same complexity class take approximately the same time/memory asympototically. This is the basis of large tenets of theoretical computer science, and much work has been done on the subject over the years, with the most famous being the famous [P=NP](https://www.explainxkcd.com/wiki/index.php/287:_NP-Complete) problem, which asks whether the two complexity classes can be reduced to one another.

![A representation of the relationships between several important complexity classes - courtesy of Wikipedia](https://en.wikipedia.org/wiki/Complexity_class#/media/File:Complexity_subsets_pspace.svg)

### Time Complexity

![Graphs of functions commonly used in the analysis of algorithms, showing the number of operations N as the result of input size n for each function - courtesy of Wikipedia](https://en.wikipedia.org/wiki/Time_complexity#/media/File:Comparison_computational_complexity.svg)

Of course, we will not be discussing these classes in great detail - this is essentially a data science text after all! However, what we will be discussing is _time_ complexity - as speed should always be a major factor when thinking about how to write code. Time complexity describes the amount of computer time it takes to run an algorithm - with each "operation" taken to be a _basic_ computational operation (such as addition, subtraction, list indexing, etc.). Other operations like insertion and deletion are not basic operations, and in fact often have runtimes that are nontrivial.

Since running times can vary wildly by input-size, it is often commonplace to consider the worst-case runtime of a function or an algorithm. Similarly, it's also standard practice to look at asympotic behavior of a given algorithm - this means looking at large input sizes n - such that the difference between something taking 2n time and 16n time isn't really that large of a difference when dealing with large input sizes when compared with something like $\log(n)$ or $n^2$ time. Placing an upper bound on a given algorithm is given by something called ["Big-O"](https://en.wikipedia.org/wiki/Big_O_notation) notation, which is formally defined as such:

$$ f(n) \in \mathcal{O}\left(g(n)\right) \implies \left|f(n)\right| \leq c \cdot g(n) \forall n \geq n_0 \in \mathbb{R} $$

This is a very formal way of stating that if you can find a function that is greater than or equal to your runtime (your algorthm's time complexity function "function") for all values of n greater than a some number times any finite constant c, then your function is in $\mathcal{O}(g(n))$.

There's a similar notation known as ["Little-o"](https://en.wikipedia.org/wiki/Big_O_notation#Related_asymptotic_notations) notation - which is for when something is _strictly_ less than a given function - and the definition changes slightly:

$$ f(n) \in \mathcal{o}\left(g(n)\right) \implies \left|f(n)\right| \leq c \cdot g(n) \forall n \geq n_0 \in \mathbb{R}, c > 0 $$
There is also a definition for Little-o that involves limits that may be more useful at times:

$$  f(n) \in \mathcal{o}\left(g(n)\right) \implies \lim_{n\rightarrow\infty} \frac{f(n)}{g(n)} = 0 $$

The difference here is that while Big-O has to be true for at least some constant c, Little-o must hold for every possible positive constant. Little-o then makes a stronger statement about the time complexity - every function $\in \mathcal{o}\left(g(n)\right)$ is also $\in \mathcal{O}\left(g(n)\right)$, however the other way around is not necessarily true (think squares and rectangles!). 

#### Examples

* Is $n^2 \in \mathcal{O}\left(n^2\right)$?
$
\begin{aligned}
  |n^2| &\overset{?}{\leq} c \cdot n^2\\
  1 &\leq c \text{ for some choice of c } \geq 1\\
  &\therefore n^2 \in \mathcal{O}\left(n^2\right)
\end{aligned}
$
* Is $\log(n) \in \mathcal{o}\left(n^\epsilon\right)$, where $\epsilon$ is any real number > 0?
$
\begin{aligned}
  \lim_{n\rightarrow\infty}\frac{\log(n)}{n^\epsilon} &= 0 \forall \epsilon > 0 \implies \log(n) \in \mathcal{o}(n^\epsilon) \forall \epsilon > 0\\
  L.H.S.: &\lim_{n\rightarrow\infty}\frac{\log(n)}{n^\epsilon}\\
  &= \lim_{n\rightarrow\infty} \frac{\epsilon\log(n^\frac{1}{\epsilon})}{n^\epsilon}\\
  &< \lim_{n\rightarrow\infty} \frac{\epsilon n^\frac{1}{\epsilon}}{n^\epsilon}\\
  &= \lim_{n\rightarrow\infty} \frac{\epsilon}{n^{\epsilon - \frac{1}{\epsilon}}} = 0\\
  &\therefore \log(n) \in \mathcal{o}\left(n^\epsilon\right) \forall \epsilon > 0
\end{aligned}
$

There exist other time complexity bounds like Big-Omega, little-Omega, and Big-Theta - but Big/Little-O is arguably the most useful, since it simple provides and upper bound on the runtime

## Exercises

### 1) Recursion

1. Write a simple function called `fact(n)` that calculates the Fibonacci numbers - one in C++ and one in Python - recursively. Is there a difference in the runtime between n=20 and n=50? ***HINT:** What is/are the base case(s) of the Fibonacci Sequence?*
   
2. One of the major drawbacks to basic recursion is that values have to calculated repeatedly. For instance, in the Fibonacci sequence, $Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)= (Fibonacci(n-2) + Fibonacci(n-3)) + (Fibonacci(n-3) + Fibonacci(n-4))$ and so on. This wastes computational time! Is there a way that you can think of to speed this process up? Implement it and compare the time of your new function with `fact(n)` from part 1. ***HINT:** It involves storing values.*
   
3. Congratulations! You have now discovered [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming), an extremely powerful algorithmic tool for solving complex problems that have [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure).

### 2) Floating Point Accuracy

1. The following code block calculates $e^{-x}$ via its Taylor Series (using the factorial function you created in Problem 1!), however it is wildly inaccurate even for small integers. The reason is that this code is not good for maintaining the accuracy of a floating point number. Try and improve upon it, and compare it to the value returned by `exp(-x)` (which is well optimized for accuracy!). Afterwards, implement the C++ code below in Python, and notice how the same problem does _not_ occur 
**_HINT:_ Accuracy breaks down for really large numbers - maybe scaling down then scaling back up somehow would help? Similarly, try an iterative approach to calculating the sum, it's much easier for C++ to do $x^6*x$ than $x^7$.**

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
Show that for any $n > 2$ all permutations are not equally probable.