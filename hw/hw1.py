import matplotlib.pyplot as plt
import time

def time_function(func, *args): #USE THIS FUNCTION TO TIME THINGS IF YOU WANT!!!!!
    """This is a function that makes it easy to time other functions. 
    If there is a function f(x,y,z) you would like to time, enter time_function(f,x,y,z) to time f(x,y,z)

    :param func: the function you want to time
    :type func: function
    :return: returns the time of the function along with its value
    :rtype: Tuple[float, Any]
    """

    start = time.time()
    value = func(*args)
    end = time.time()
    return end - start, value

## Problem 1a

def fib(n):
    pass

## Problem 1b
def fast_fib(n):
    pass



## Problem 2a

x = ["racecar", "12321", "amanaplanacanalpanama", "momo", "seventeen thousand leagues under the sea", "tu stultes es"]

def for_f(x):
    return True

def while_f(x):
    return True

## Problem 2b

data = [
    [
        ((0,0), (0,0), (6,6)), #t=0
        ((3,3), (6,6), (6,6)), #t=1
        ((12,12), (12,12), (6,6)), #t=2
        ((27,27), (18,18), (6,6)) #t=3
    ]
]

labels = ["x(t) = y(t) = 3t^2"]

times = [
    [0,1,2,3]
]

def visualize(data, labels, times):
    pass
    plt.savefig("trajectories.png")