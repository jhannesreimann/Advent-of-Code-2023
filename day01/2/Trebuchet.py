sum = 0
d = { "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e" }

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

for line in open("day01/input"):
    line = replace_all(line, d)
    numberList = [int(i) for i in line if i.isdigit()]
    string = str(numberList[0]) + str(numberList[-1])
    sum += int(string)

print(sum)