# Number of testcases
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    oddCount = 0
    evenCount = 0

    for i in range(n):
        if(arr[i] % 2 == 0):
            evenCount += 1
        else: 
            oddCount += 1
    
    if(oddCount > evenCount) :
        print(evenCount)
    else:
        print(oddCount)