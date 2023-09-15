---
title: Visualization
filename: visualization
chapternum: '3'
numbersections: true
---

> "Mankind invented a system to cope with the fact that we are so intrinsically lousy at manipulating numbers. It's called the graph." - [Charlie Munger](https://en.wikipedia.org/wiki/Charlie_Munger)

> "...You might think that, data presentation being almost the primary reason for ROOT's existence, it might be good at it. Well, for some reason the default plot style is unfeasibly ugly (grey background?!) and difficult to fix. In fact to fix it you have to go via several global ROOT objects. Gah." - [Andy Buckley](https://www.ppe.gla.ac.uk/~abuckley/)

## Objectives

* Briefly introduce matplotlib
* Talk about histogramming
  * How does one scale a histogram?
* Talk even more about histogramming
* _Emphasize_ histograms even more

***

## WARNING

___Use the supplementary notebook for this chapter.___ Much of this chapter deals with plotting, and the notebook is a good way to showcase code!

## Producing Plots Pythonically

Much of science is nothing without pretty plots! These satisfying pieces of data are able to show distributions in a nice way that our brains can comprehend. Showing a plots like below is a much better way of showing the range over a bunch of different samples than writing the range and standard deviations in a table.

![A histogram showing the maximum and minimum values for a distribution for a bunch of samples. Errors shown are the standard deviation](media/histogram_example.png)

Luckily, (unlike CERN ROOT), it is very easy to plot in Python. It's as simple as:

```python
import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3]
y = [1,2,3]
plt.plot(x,y)
```

This chapter does not intend to discuess the actual intricacies of plotting things - that is the job of documentation! I highly recommend using that documentation to your benefit, as well as the supplementary Jupyter Notebook that is provided. Anything I tell you in text form will be thrown away and forgotten near immediately - through no fault of your own!


## Exercises

### 1) Integrals of histograms

1. Write a function named `integrate_hist(counts, bins)` that takes in a numpy histogram of counts and bins, and returns the integral of that histogram.
2. Write a function named `scale_hist(scaleto, counts, bins)` that takes in a numpy histogram of counts and bins, and returns a scaled version of the histogram with an area of `scaleto`.
