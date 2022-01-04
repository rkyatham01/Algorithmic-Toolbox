
def Fibonacci(n):
    firstone = 1
    secondone = 0
    output = 0
    sum = 1
    for i in range(2, n+1):
        output = firstone + secondone
        secondone = firstone
        firstone = output
        sum = sum + output
    print(sum % 10)

n = int(input())

if n == 0:
    print(0)
    exit()
else:
    Fibonacci(n)

