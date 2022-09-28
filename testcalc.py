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

sum=0
for k in range(1, 250):
    sum = sum + 0.02* k


print(250 * 249 *248*246*247 * 0.02**5)
print(0.98**245)

