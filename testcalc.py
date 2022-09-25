import math
def kperm(n,k):
    nfact = math.factorial(n)
    nminuskfact = math.factorial(n-k)
    return nfact/nminuskfact

def nchoosek(n,k):
    kfact = math.factorial(k)
    ans = kperm(n,k) / kfact
    return(ans)

def bernoulitrials(n, k, p):
    ans = 0
    i=k
    for i in range(n):
        ans = ans + (nchoosek(n,i) * p**i * (1-p)**(n-i))
    return ans

print(nchoosek(4,3))
print(nchoosek(5,4))
print(nchoosek(6,4))
print(nchoosek(7,4))
