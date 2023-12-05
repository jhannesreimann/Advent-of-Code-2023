sum = 0

for line in open("day01/input"):
    numberList = [int(i) for i in line if i.isdigit()]
    string = ''.join(str(numberList[0]) + str(numberList[-1]))
    sum += int(string)

print(sum)