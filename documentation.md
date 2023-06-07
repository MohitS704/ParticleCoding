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

A lot of this chapter is filled with my opinions on this subject, based off of personal experience along with the experience of those that I know. Documentation, and the amount of effort that you put into documenting things, is entirely subjective. However, the general consensus is that you should at least document _something_.

## Why is Documentation Important?

When code is undocumented, it can often be difficult to understand. This makes it difficult to parse for anyone in the future looking at code - __including yourself!__ I know that many people have created a program to do something - maybe something that calculates a physical value - and when they come back to it after some time, they end up with no clue what they were thinking! This kind of blase attitude towards documentation is fine for small and self-understood scripts, but becomes much more of an issue when dealing with larger programs, and _especially_ with things like packages.

### From a Software Perspective

Code is something that has to be continuously understood 
