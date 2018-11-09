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
    #else:
    #    x = -nchoosek(n,n-1)*bernoulli(n-1)/float(2)    #this is final term in the sum
    #return x
    else:
        for k in range(n):
            x = x - nck(n,k)*bernoulli(k)/float(n-k+1)
    return x
#k = []
#for i in range(10):
#    k = k + [bernoulli(2*i)]
#print k
    
