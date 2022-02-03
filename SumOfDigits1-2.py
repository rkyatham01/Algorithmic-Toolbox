def sumOfDigts(input1, input2):
    return input1 + input2

if __name__ == '__main__':
    x, y = map(int, input().split())  # splits the inputs
    # into seperate characters as a integer [1,2]
    print(sumOfDigts(x, y))
