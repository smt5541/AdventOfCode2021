def aoc_day_1_1(filename):
    increaseCount = 0
    prevNum = -1
    with open(filename) as file:
        for line in file.readlines():
            newNum = int(line)
            if prevNum >= 0 and newNum > prevNum:
                increaseCount+=1
            prevNum = newNum
    print(increaseCount)
