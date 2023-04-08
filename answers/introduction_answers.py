from timeit import default_timer as timer
import matplotlib.pyplot as plt
import tqdm

def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)

def fast_fib(n):
    global global_store
    if n in global_store.keys():
        return global_store[n]
    
    if n == 1 or n == 0:
        return 1
    
    global_store[n] = fast_fib(n-1) + fast_fib(n-2)
    return global_store[n]
    
if __name__ == '__main__':
    global_store = {}
    orig_fib = []
    new_fib = []
    n=5e5
    range_to_iter = range(1, int(n))
    for n in tqdm.tqdm(range_to_iter):
        start = timer()
        # fib(n)
        end = timer()
        fast_fib(n)
        new_fib.append(timer() - end)
        orig_fib.append(end - start)

    # plt.plot(range(1,26), orig_fib)
    fig, ax = plt.subplots(1,2)
    ax[0].plot(range_to_iter, new_fib)
    ax[1].hist(new_fib, bins=10000, histtype='step')

    for i in range(2):
        ax[i].set_yscale('log')
        ax[i].set_xscale('log')
    plt.savefig('answer.png')
    