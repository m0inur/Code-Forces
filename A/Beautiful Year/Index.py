def is_distinct_year(year):
    return year[0] != year[1] and year[0] != year[2] and year[0] != year[3] and year[1] != year[0] and year[1] != year[2] and year[1] != year[3] and year[2] != year[0] and year[2] != year[1] and year[2] != year[3] and year[3] != year[0] and year[3] != year[1] and year[3] != year[2]

year = int(input())
i = year + 1
while True:
    if is_distinct_year(str(i)) == True:
        print(i)
        break
    i += 1