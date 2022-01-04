#Function that is called
def FibonacciNumberForAToN(a,n): #now use the n to perform and find the answer on it
    firstone = FibonacciNumberForA(a)
    a = a + 1
    secondone = FibonacciNumberForA(a)
    output = 0
    sum = 1
    for i in range(a, n+1):
        output = firstone + secondone
        secondone = firstone
        firstone = output
        sum = sum + output
    print(output % 10)

def FibonacciNumberForA(a):  # now use the n to perform and find the answer on it
    firstone = 1
    secondone = 0
    output = 0
    sum = 1
    for i in range(2, a + 1):
        output = firstone + secondone
        secondone = firstone
        firstone = output
        sum = sum + output


a,n = [int(x) for x in input().split()]

if n == 0:
    print(0)
if n == 1:
    print(1)
else:
    FibonacciNumberForA(a,n)

