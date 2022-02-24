def can_open_all_doors(map):
    hasRedDoorKey = False
    hasGreenDoorKey = False
    hasBlueDoorKey = False

    for i in range(len(map)):
        if(map[i] == 'R' and hasRedDoorKey == False):
            return "NO"
        elif(map[i] == 'G' and hasGreenDoorKey == False):
            return "NO"
        elif(map[i] == 'B' and hasBlueDoorKey == False):
            return "NO"
        elif(map[i] == 'r'): hasRedDoorKey = True
        elif(map[i] == 'g'): hasGreenDoorKey = True
        elif(map[i] == 'b'): hasBlueDoorKey = True

    return "YES"
# Number of testcases
t = int(input())

for i in range(t):
    map = input()
    print(can_open_all_doors(map))