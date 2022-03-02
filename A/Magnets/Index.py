# https://codeforces.com/problemset/problem/344/A

n = int(input())
last = input()[1]
groups = 1

for i in range(n-1):
    magnets = input()
    if magnets[0] == last:
        last = magnets[1]
        groups += 1

print(groups)