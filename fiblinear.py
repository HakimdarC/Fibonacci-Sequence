import time
def fib_lin(x):
    a, b = 0, 1
    for i in range(x+1):
        a, b = b, a + b
    return a
x= int(input("Give the number of fibonnacci terms: "))

for x in range(1,x+1):
    start=time.time()
    print(x,":",fib_lin(x))
stop=time.time()
print("total time taken to this program is {} sec".format(stop-start))
