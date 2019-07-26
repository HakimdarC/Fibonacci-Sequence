from functools import lru_cache
@lru_cache(maxsize = 1000)
def fib(n):
    if n<1:
        raise ValueError("Type non negative integer")
    if type(n) != int:
        raise TypeError("Type non negative integer")

    if n==1:
        return 1
    if n==2:
        return 1

    else:
        return fib(n-1) + fib(n-2)
n = int(input("Give the number of fibonnacci terms: "))

for n in range(1,n+1):
    print(n,":",fib(n))

