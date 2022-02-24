n = int(input())
str = input()
prevChar = str[0]
removeCount = 0

for i in range(1, n):
    if str[i] == prevChar:
        removeCount += 1
    else:
        prevChar = str[i]

print(removeCount)