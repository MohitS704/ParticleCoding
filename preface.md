---
title: "Preface"
filename: "preface"
chapternum: "p"
geometry: margin=30mm
---

>_"Physics, which is one of the oldest academic disciplines, has had plenty of time to figure out a way to visit the year 4515 and see if humans are still around or have been taken over by a race of intelligent spiders, is broken into multiple branches including particle physics and astrophysics, neither of which has led to the construction of a time-traveling device so who gives a shit."_, [_The Onion Book of Known Knowledge_](https://mathijs.info/files/ebooks/onion.pdf), 2012.

This course is intended to provide insight into how to manipulate large quantities of data similar to a particle physicist, and how to use the tools to do so. Now, as a PhD student who has yet to even pass his Graduate Board Oral Exam (GBO), you may think, "Is this schmuck even qualified to type these words??" I guess not really - but we all start somewhere. (Pro Tip: If you think I'm wholly unqualified to be writing this, you are probably right. _Please_ help me out by either suggesting material to add or revise, or write some stuff up to help me out!) Over the course of my PhD I hope to continue to update this text with sections about things that I _wish_ I had when I was learning to conduct analyses. This also involves pointing you to the people who can tell you about processes/packages better than I ever could - the developers themselves!

The educational goals will be to cover the following (and this will be updated as time goes on):

* An (_extremely_) brief introduction to
  * Python
  * C++
  * Algorithmic Analysis
* CERN ROOT
  * Pythonic methods of interfacing with CERN ROOT
  * Bypassing ROOT entirely (in most cases)
* Speed
  * Vectorization
  * Good Practices

## Guiding Philosophy

The guiding philosphy of this course is the same as the motto of the acclaimed satire publication, The Onion; _Tu Stultes Es_, or "You are Dumb." (Referenced in [Section 1 of the Argument](https://www.supremecourt.gov/DocketPDF/22/22-293/242292/20221003125252896_35295545_1-22.10.03%20-%20Novak-Parma%20-%20Onion%20Amicus%20Brief.pdf) of an Amicus Curae Brief to the Supreme Court of the United States).

__This is not to mean that _you_, my dear reader, are dumb. You are not!__. It instead means that you should always _assume_ the worst understanding possible for any person reading your code, or in the machine that is processing your code. The specifity requirements of algorithms are often ridiculed in videos like [this](https://www.youtube.com/watch?v=Ct-lOOUqmyY), but they are very [useful](http://static.zerorobotics.mit.edu/docs/team-activities/ProgrammingPeanutButterAndJelly.pdf) tools to teach that programs need to be very specific and easy to understand!

As scientists, code often needs to be shared, and oftentimes people who try to read and understand code lack the context that the developers had - good code should be written so that "even a caveman could do it." This is so that people who lack the background knowledge of the code can understand what can is done.

Going back to the guiding philosphy, this means that code will be approached as something that can and should be deconstructed down to its basic components, with a plethora of comments and programming styles that favor readability and ease-of-access over marginal gains in performance (of course, a decline in readability is inevitable with operations like vectorization, but that is a trade-off that you should be more than willing to make due to the performance difference). I've found that this approach to coding has netted the most benefits, as people can come back to code and continue working immediately, rather than spend hours trying to remember exactly what was done.

## Usefulness to Physicists

I hope to be as helpful as possible when writing this text - but at the end of the day - this whole text can only really be a primer. Individual groups use specific proprietary software, collaborations like CMS and ATLAS have their own environments, and I could not possible hope to cover nearly all of that. I can barely manage as is! However, if there are students who do not have strong backgrounds in programming, texts like this can be invaluable to get them to pick up skills that they otherwise would not have as quickly!

Similarly, Python is a dominant force in scientific computing, and it gets very painful sometimes to see people still using Python 2, writing code that is essentially not human-readable, or writing code that is needlessly _slow_! Similarly, for those of you who are not in particle or astrophysics, it's sometimes not necessary to utilize large-scale data analyses, and sometimes not necessary to learn them at all. But, you should still learn! The ability to analyze large quantities of data properly and efficiently also gives you the ability to analyze small quantities of data properly and efficiently!

## Usefulness to Non-Physicists

Physicists handle large amounts of data, and if you are interested in learning about how to analyze large amounts of data, this may be the place for you! The same techniques and tools used by people in physics have been used by many people (there were [actuaries](https://www.casact.org/abstract/root-data-analysis-and-data-mining-tool-cern) who _wanted_ to use ROOT!). I think this text can be very helpful to anyone looking for an introduction to analyzing data.

## The Importance of Documentation

There is a reputation among physicists that they write bad code! "Physicist code," it's called - from those of us who seem "enlightened" by studying computer science in some capacity beforehand. To be completely honest, physicists actually don't write code that's bad, it's just hard to understand! What would truly improve the code that physicists write would be good documentation. I've encountered _entire_ packages that are immensely complex, with the only documentation being a few inline comments smattered here and there - it isn't sustainable!! I'm a bit of a stickler for good documentation, and so maybe that's why I'm bothering to write this text.

That being said, if you, the esteemed reader, find anything wrong with my grammar, spelling, or have recommendations for material **please** tell me! Bring up an issue on the Github or email me at [msrivas6@jhu.edu](mailto:msrivas6@jh.edu).
