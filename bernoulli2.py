import math

def gcd(x, y): 
    while(y):
        x, y = y, x % y 
    return x 
  
def fradd(A,B):
    X = [A[0]*B[1] + B[0]*A[1], A[1]*B[1]]
    X = [X[0]/gcd(X[0],X[1]) , X[1]/gcd(X[0],X[1])]
    return X

#print fradd([5,7], [11,13])

def frmult(A,B):
    X = [A[0]*B[0],A[1]*B[1]]
    X = [X[0]/gcd(X[0],X[1]) , X[1]/gcd(X[0],X[1])]
    return X

def frsub(A,B):
    return fradd(A,[-B[0],B[1]])

def frdiv(A,B):
    return frmult(A,[B[1],B[0]])

def nck(n,k):
    i = math.factorial(k)*math.factorial(n-k)
    j = math.factorial(n)
    return j/i

#recursively defined bernoulli function

def setup(n,d):
	x = [0,1]
	if n in d:
		return d[n]
	else:
		
		for k in range(n):
			y = [nck(n,k)*setup(k,d)[0], (n-k+1)*setup(k,d)[1]]
			y =  [y[0]/gcd(y[0],y[1]) , y[1]/gcd(y[0],y[1])]

			x = frsub(x, y)
			#print (x, 'first')
			x  = [x[0]/gcd(x[0],x[1]) , x[1]/gcd(x[0],x[1])]
			x = [int(x[0]), int(x[1])]
			#print(x,'second')
		ans = x
		d[n] = ans
		return ans



def bernoulli(n):
	d = {0:[1,1], 1:[-1,2]}
	if n %2 == 1 and n > 2:
		return [0,1]
	return setup(n,d)

#for i in range(100):
#	print(bernoulli(i))
