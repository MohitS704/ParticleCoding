---
title: Documentation
filename: documentation
chapternum: '1'
numbersections: true
---

> "There is nothing in the programming field more despicable than an undocumented program." - [Edward Yourdon](https://en.wikipedia.org/wiki/Edward_Yourdon)

> "Voluminous documentation is part of the problem, not part of the solution." - [Tom DeMarco](https://en.wikipedia.org/wiki/Tom_DeMarco)

> "Manuals just slow you down and make you feel stupid. The directions are too slow, too detailed, and use too much abstract, arcane or academic language, like 'boot up' instead of turn on the red switch in the back." - [Neil Fiore](https://www.ericksoncongress.com/neil-fiore-phd/)

## Objectives

* Why is documentation important?
  * From a software perspective
  * From a physics perspective
* Learn about how to document code
  * Not _everything_ needs to be documented
  * docstrings
    * styles
* Writing good code that should speak for itself

***

## WARNING

A lot of this chapter is filled with my opinions on this subject, based off of personal experience along with the experience of those that I know. (__Once again, if you have different opinions, _tell me!_ I am nothing resembling an expert on this topic__) Documentation, and the amount of effort that you put into documenting things, is entirely subjective. However, the general consensus is that you should at least document _something_.

## Why is Documentation Important?

When code is undocumented, it can often be difficult to understand. This makes it difficult to parse for anyone in the future looking at code - __including yourself!__ I know that many people have created a program to do something - maybe something that calculates a physical value - and when they come back to it after some time, they end up with no clue what they were thinking! This kind of blase attitude towards documentation is fine for small and self-understood scripts, but becomes much more of an issue when dealing with larger programs, and _especially_ with things like packages.

### From a Software Perspective

The average piece of professionally written software has between [1 and 25 bugs per 1000 lines of code](https://stackoverflow.com/a/56043694) in professional industry - imagine the number of bugs that you or I have for individually written programs! This means that in order for code to maintain its usefulness, it has to be constantly maintained. In order for it to be constantly maintained and updated, it should be easy for someone to understand when coming back to it.

Not only does this make it easier for a person to understand code, but it also means that the code will be better written to not include unnecessary redundancies! For example, let's say there is some code that defines a function to store mass values on lines 4-10, and a new function is being written that needs to access that mass function on line 500 5 months after the mass function was written. Without any comments, someone might simply _re-write_ the mass function needlessly, forgetting the earlier function exists! This is, of course, an extreme example, but the point still stands, comments and documentation help smoothen the development process.

### From a Physics Perspective

Let's look at some code together from [JHUGen](https://spin.pha.jhu.edu/), a Monte Carlo simulator for particle physics, and try to parse the physical meaning out of it after deleting the comments. The code is in Fortran, but the block is simple enough. This is the first time `qqq` and `decayMass` are accessed after their initialization, and the other variables are all imported from the parameters in other files.

```fortran
elseif( scheme.eq.4) then
  if ( M_Zprime.ne.-1 ) then 
    decayMass = M_Zprime
  else
    decayMass = M_Z
  end if
  if(0.25d0*(sHat) < decayMass**2) then
    qqq = 0
  else
    qqq = sqrt(0.25d0*(sHat) - decayMass**2)
  endif
  qqq0=sqrt(0.25d0*(M_Reso**2) - decayMass**2)
  GetBWPropagator =  1d0/( (sHat-M_Reso**2)**2 + (M_Reso*Ga_Reso*qqq/qqq0)**2 )
```

Well, knowing the context surrounding JHUGen, the decayMass is the two decay products of the Higgs (or Higgs subsitute) being simulated, and `M_ZPrime`/`M_Z` are some sort of decay products. Well what is `sHat`? Is it a particularly crude way of describing what happened at the toilet, or is it something genuinely physics related? It turns out that not _only_ is this variable funnily named, it also describes a genuine physics item in detail! The variable `sHat` is _supposed_ to represent $\hat{s}$, which is the square of a particle reconstructed mass - and is a good name motivated by nomenclature! However, let's look at the same code block without removing the comments.

Okay, one can assume that can be parsed from anyone who uses a particle physics generator, the target audience of the software. However, scheme numbering is not exclusive to particle physics - what does scheme 4 mean? How is it different from scheme 1,2 or 3? Let's now look at the code with just a few one line comments scattered throughout:

```fortran
elseif( scheme.eq.4) then !alternate running width
  if ( M_Zprime.ne.-1 ) then !if you're using ZPrime then it will consider the ZPrime mass
    decayMass = M_Zprime
  else
    decayMass = M_Z !if you're doing Z-ZPrime stuff this scheme won't work anyways so the point is moot
  end if
  if(0.25d0*(sHat) < decayMass**2) then !sHat is the mass squared!
    qqq = 0
  else
    qqq = sqrt(0.25d0*(sHat) - decayMass**2)
  endif
  qqq0=sqrt(0.25d0*(M_Reso**2) - decayMass**2)
  GetBWPropagator =  1d0/( (sHat-M_Reso**2)**2 + (M_Reso*Ga_Reso*qqq/qqq0)**2 ) !new style running width
```

This paints a much clearer picture - `sHat` is explained explicitly, as is the decay mass. Similarly, it is now known that scheme 4 is the alternate running width scheme, and that `GetBWPropagator` is the propagator for the new style running width propagator! The addition of just 4 one line comments has added a whole new dimension of context and clarity to this code block - there is a lot less thinking required to understand this code - and a lot less guessing that has to happen.

Here lies the importance of code in scientific circles - making sure that the decisions that are made are motivated by scientific phenomena - and being able to explain those decisions properly.

## How is code documented?

There are two really useful types of comments in Python at least - and this text only really covers Python. These two types are _inline comments_ and _docstrings_. Both serve important purposes and complement each other's existence. One is usually more used to inline comments, as they don't have as much structure.

Inline comments are the kind seen in the example above - they serve to clarify certain lines/blocks of code for clarity. They are as dense or as sparse as you'd like, and serve to improve clarity for code that is written.

Docstrings are specially designed comments that go in functions to describe what they are and what they do. A nice description of docstrings is shown in [PEP 257](https://peps.python.org/pep-0257/), as defined by Python back in 2001. Since then, there are now a multitude of docstring styles in Python:

* [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
* [NumPy](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google](https://google.github.io/styleguide/pyguide.html)
* There are a few others that I might not be mentioning - but you get the idea.

The basic structure of a docstring contains the following:

* A brief description of what the function does
* A list of the input parameters
  * This could include the expected input types of the function. Since Python does not have explicit types, this is useful!
* What the function returns
* Any errors that the function manually raises

## Exercises

### 1) Parsing Code

1. This function doesn't have any comments, is named badly, has variable names that only make sense if you know the context surrounding the function, and re-assigns variables over and over again! Try and parse what the function does, and make a docstring for the following function in either the NumPy, Sphinx, or Google style. Similarly, suggest a useful name for the function.

```python
import numpy as np
def do_something(a, arr, arr2=[], fact=False):
    arr = np.array(arr)
    arr = arr.astype(float)
    signs = np.sign(arr)
    arr = np.abs(arr)

    if (a == 0) or (np.sum(arr) == 0):
        return np.zeros(arr.shape)
    
    arr = signs*arr*a/np.sum(arr)
    arr[~np.isfinite(arr)] = 0
    if any(arr2):
        if fact:
            return arr, arr2, a/np.sum(arr)
        
        return arr, arr2
    
    elif fact:
        return arr, a/np.sum(arr)
    
    return arr
```