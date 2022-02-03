#Function that is called
def FibonacciNumber(n): #now use the n to perform and find the answer on it

    for i in range(2,n):
        Arr[i] = ((Arr[i-1] + Arr[i-2]) % 10) #stores the last digit in each array point
    print(Arr[n-1])

n = int(input())
if n == 0:
    print(0)
else:
    n = n + 1
    Arr = [0] * n #creates an empty Array
    Arr[0] = 0
    Arr[1] = 1
    FibonacciNumber(n)
