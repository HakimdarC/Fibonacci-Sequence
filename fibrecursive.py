
def fib(n):

    if n==1:
        return 1
    if n==2:
        return 1

    else:
        return fib(n-1) + fib(n-2)
n = int(input("Give the number of fibonnacci terms: "))

for n in range(1,n+1):
    print(n,":",fib(n))

