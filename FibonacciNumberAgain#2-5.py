#Function that is called
def Period(a,n,Arr): #now use the n to perform and find the answer on it
    b = 1
    for i in range(2,a+1):
        Arr.append((Arr[i-1] + Arr[i-2]) % n)
        if Arr[i-1] == 0 and Arr[i] == 1:
            Fibonacci(a,b,n)
            break
        b = b + 1

def PeriodNormal(a,n,Arr):
    for i in range(2, a+1):
        Arr.append(Arr[i - 1] + Arr[i - 2])
    print(Arr[a] % n)

def Fibonacci(a,b,n):
    c = a % b #c is the remainder of a and n
    Arr2 = []  # creates an empty Array
    Arr2.append(0)
    Arr2.append(1)
    for i in range(2,c+1):
        Arr2.append(Arr2[i-1] + Arr2[i-2])
    print(Arr2[c] % n)

a,n = [int(x) for x in input().split()]
if a == 0:
    print(0)
else:
    Arr = []
    Arr.append(0)
    Arr.append(1)
    if (a > n^2):
        Period(a,n,Arr)
    else:
        PeriodNormal(a,n,Arr)


