
def GCD(a,b):
    if b == 0:
        LeastCommonMultiple(a)
    x = a % b #finds the remainder and stores it in x
    a = b
    b = x #sets
    GCD(a,b)


def LeastCommonMultiple(a):
    print(c // a)


a,b = [int(x) for x in input().split()]
c = a * b #keeps it in c
GCD(a,b)
