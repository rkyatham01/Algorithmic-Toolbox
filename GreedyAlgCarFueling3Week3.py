def CarFueling(d,m,n,Arr):
    currentnumberrefills = 0
    currentRefill = 0
    index = 0
    currentdistance = 0
    while currentdistance <= d: #goes as long as it doesn't go past d
        while m - Arr[index] >= 0 and currentdistance <= d:
            index = index + 1
        currentdistance = Arr[index]
        m = m + Arr[index]
        currentnumberrefills = currentnumberrefills + 1

d = int(input()) #distance between cities
m = int(input()) #at most m miles on a full tank
n = int(input()) #total # of stops available

Arr = list(map(int, input().split())) #converts to list after mapping the inputs
CarFueling(d,m,n,Arr)
