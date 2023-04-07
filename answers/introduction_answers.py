from timeit import default_timer as timer

def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1) + fact(n-2)

def fast_fact(n):
    global global_store
    if n in global_store.keys():
        return global_store[n]
    
    if n == 1 or n == 0:
        return 1
    
    global_store[n] = fast_fact(n-1) + fast_fact(n-2)
    return global_store[n]
    
if __name__ == '__main__':
    global_store = {}
    n1 = 10
    n2 = 30
    
    print("factorial of 10:")
    start = timer()
    fact(10)
    end = timer()
    print(end - start)
    
    start = timer()
    fast_fact(10)
    end = timer()
    print(end - start)
    
    print("factorial of", n2)
    start = timer()
    fact(n2)
    end = timer()
    print(end - start)
    
    start = timer()
    fast_fact(n2)
    end = timer()
    print(end - start)