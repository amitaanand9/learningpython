import math
def kperm(n,k):
    nfact = math.factorial(n)
    nminuskfact = math.factorial(n-k)
    return nfact/nminuskfact

def nchoosek(n,k):
    kfact = math.factorial(k)
    ans = kperm(n,k) / kfact
    return(ans)

#print(nchoosek(75,5)*15)
#answer = math.factorial(20) / ((math.factorial(3)-1) * (math.factorial(10)-1) * (math.factorial(7)-1))
print(nchoosek(3,0))