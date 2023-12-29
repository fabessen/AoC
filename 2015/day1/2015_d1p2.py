#https://adventofcode.com/2015/day/1#part2

count    = 0
noiter   = 0
basement = 0
with open("./aoc/2015/d1/2015_d1p1.txt") as file:
    data = file.read()

for chrtr in data:
    noiter += 1

    if chrtr == "(":
        count += 1
    elif chrtr == ")":
        count -= 1

    if basement == 0:
        if count == -1:
            basement = noiter

print(str(count) + " " + str(basement))
#lösung 138 :)
