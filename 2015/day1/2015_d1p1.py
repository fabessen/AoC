count = 0
with open("2015_d1p1.txt") as file:
    data = file.read()

for chrtr in data:
    if chrtr == "(":
        count += 1
    elif chrtr == ")":
        count -= 1

print(count)
#lösung 138 :)
