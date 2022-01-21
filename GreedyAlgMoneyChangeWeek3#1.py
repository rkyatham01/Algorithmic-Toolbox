def MoneyChange(n,penny,nickel,dime):
    minnumbcoins = 0
    if n == 0:
        print(0)
    while n >= dime:
        n = n - 10
        minnumbcoins = minnumbcoins + 1
        if n == 0:
            print(minnumbcoins)
    while n >= nickel:
        n = n - 5
        minnumbcoins = minnumbcoins + 1
        if n == 0:
            print(minnumbcoins)
    while n >= penny:
        n = n - 1
        minnumbcoins = minnumbcoins + 1
        if n == 0:
            print(minnumbcoins)

n = int(input()) #takes the Input
penny = 1
nickel = 5
dime = 10 #denominations
MoneyChange(n,penny,nickel,dime)