def find_minimal_damage_count(n, jumps, attacks):
    damageCount = 0
    # if traps length equals to jumps len
    if(n == jumps):
        return damageCount
    
    for i in range(n):
        damageCount += attacks[i]
        # add bonus damage to init damage
        attacks[i] += i + 1

    attacks.sort()
    attacks.reverse()

    for i in range(jumps):
        damageCount -= attacks[i]
        damageCount += n - i

    return damageCount


# Number of testcases
t = int(input())

for i in range(t):
    lens = input().split(" ")
    n = int(lens[0])
    jumps = int(lens[1])
    attacks = list(map(int, input().split(" ")))
    print(str(find_minimal_damage_count(n, jumps, attacks)))
