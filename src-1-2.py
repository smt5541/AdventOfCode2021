def aoc_day_1_2(filename):
    increaseCount = 0
    prevSum = -1
    rollNums = []
    with open(filename) as file:
        for line in file.readlines():
            newNum = int(line)
            rollNums.append(newNum)
            if len(rollNums) == 3:
                newSum = 0
                for num in rollNums:
                    newSum+=num
                if prevSum >= 0 and newSum > prevSum:
                    increaseCount+=1
                rollNums.pop(0)
                prevSum = newSum
    print(increaseCount)
