def MaximumValueOfLoot(a,b,Arr):
    if b == 0:
        print(0)
    knapsack = 0
    Capacity = 0
    sum = 0
    for x in range(0,a):
        var = Arr[x][1]
        if(var <= b):
            b = b - var #decreases the whole item itself
            knapsack = knapsack + Arr[x][0]
        else:
           restover = b #rest of the b needed for full capacity
           sum = Arr[x][0] / Arr[x][1]
           sum = sum * restover
           knapsack = knapsack + sum
           break
    print(knapsack)


a,b = [int(x) for x in input().split()]
Arr = []
if b == 0:
    print(0)

for x in range(0,a): #a is the length of the tuple
    inputs = [int(y) for y in input().split()]
    Arr.append(inputs)
Arr.sort(key=lambda y: y[0]/y[1])
Arr = Arr[::-1] #reverses the Array
#sorts the tuple by the division index
MaximumValueOfLoot(a,b,Arr) #MaximumValueOfLoot(a,b,Arr)

