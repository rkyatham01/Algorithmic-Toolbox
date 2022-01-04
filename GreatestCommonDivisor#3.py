def GCD(a,b):
    if b == 0:
        done(a)
    x = a % b #finds the remainder and stores it in x
    a = b
    b = x #sets
    GCD(a,b)

def done(a):
    print(a)


a,b = [int(x) for x in input().split()]
GCD(a,b)
