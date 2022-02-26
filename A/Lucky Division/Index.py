# A. Lucky Division
# time limit per test 2 seconds
# memory limit per test 256 megabytes
# input standard input
# output standard output
# Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

# Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.

# Input
# The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.

# Output
# In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).

# Examples

# input
# 47

# output
# YES

# input
# 16

# output
# YES

# input
# 78

# output
# NO
# Note
# Note that all lucky numbers are almost lucky as any number is evenly divisible by itself.

# In the first sample 47 is a lucky number. In the second sample 16 is divisible by 4.

def is_num_lucky(num):
    numList = list(str(num))
    if '0' in numList or '1' in numList or '2' in numList or '3' in numList or '5' in numList or '6' in numList or '8' in numList or '9' in numList:
        return False
    return True

num = int(input())
numList = list(str(num))

# if the number is not lucky
if is_num_lucky(num) == False:
    isPrinted = False

    for i in range(num):
        if is_num_lucky(i) == True:
            if num % i == 0:
                isPrinted = True
                print("YES")
                break

    if isPrinted == False:
        print("NO")
else:
    # print("it is a lucky number")
    print("YES")