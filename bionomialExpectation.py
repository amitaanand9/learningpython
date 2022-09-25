import math
def kperm(n,k):
    nfact = math.factorial(n)
    nminuskfact = math.factorial(n-k)
    return nfact/nminuskfact

def nchoosek(n,k):
    kfact = math.factorial(k)
    ans = kperm(n,k) / kfact
    return(ans)

k = 1

expectation = 0
while k<=48:
    expectation = expectation + ( nchoosek(48, k) * k**2 * (1/3)**k * (2/3)**(48-k) )
    k = k + 1

print(expectation)
variance = 0
i=1
while i <=48:
    variance = variance + (( nchoosek(48, i) * k * (1/3)**i * (2/3)**(48-i) ) * (i-16)**2 )
    i = i + 1

print(variance)