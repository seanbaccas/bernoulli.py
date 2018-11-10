#n choose k function
import math


def nck(n,k):
    i = math.factorial(k)*math.factorial(n-k)
    j = math.factorial(n)
    return j/i

#recursively defined bernoulli function

def bernoulli(n):
    x = 0
    if n ==0:
        return 1
   # next we define the sum recursively, by starting with b0=1 and holding the 
   #sum in memory while next terms are calculated
    else:
        for k in range(n):
            x = x - nck(n,k)*bernoulli(k)/float(n-k+1)
    if abs(x) < 10**-14:
        return 0
    return x

