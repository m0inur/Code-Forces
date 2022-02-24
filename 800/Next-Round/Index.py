# Number of testcases
lens = input().split(" ")
n = int(lens[0])
k = int(lens[1])
scores = list(map(int, input().split(" ")))

kthScore = scores[k - 1]
passingCount = 0

for i in range(n):
    # if current score if not positive
    if scores[i] < 1: continue
    if scores[i] >= kthScore:
        passingCount += 1
    else:
        break

print(passingCount)