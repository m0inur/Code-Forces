# https://codeforces.com/problemset/problem/136/A

n = int(input())
presents = list(map(int, input().split(" ")))
ans = ""

for i in range(n):
    index = presents.index(i + 1) + 1
    ans += str(index) + " "

print(ans)