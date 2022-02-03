FirstInputScanned = int(input())
#First input Scanned
SecondInputScanned = [int(b) for b in input().split()]
#takes the second input scanned

productoftwoHighest = 0

SecondInputScanned.sort()

x = SecondInputScanned[FirstInputScanned - 1]
y = SecondInputScanned[FirstInputScanned - 2]

print(x * y)
