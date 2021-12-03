def aoc_3_2(filename):
    numbers_o2 = []
    numbers_co2 = []
    length = 0
    with open(filename) as file:
        for line in file.readlines():
            if length == 0:
                for char in line:
                    if (char != '\n'):
                        length+=1
            numbers_o2.append(line)
            numbers_co2.append(line)
    for i in range(length):
        zeros_o2 = 0
        ones_o2 = 0
        zeros_co2 = 0
        ones_co2 = 0
        for num in numbers_o2:
            if num[i] == '0':
                zeros_o2+=1
            else:
                ones_o2+=1
        for num in numbers_co2:
            if num[i] == '0':
                zeros_co2+=1
            else:
                ones_co2+=1
        o2_remove = []
        for num in numbers_o2:
            if zeros_o2 > ones_o2:
                if num[i] != '0' and len(numbers_o2)-len(o2_remove)>1:
                    o2_remove.append(num)
            else:
                if num[i] != '1' and len(numbers_o2)-len(o2_remove)>1:
                    o2_remove.append(num)
        for num in o2_remove:
            numbers_o2.remove(num)
        co2_remove = []
        for num in numbers_co2:
            if zeros_co2 > ones_co2:
                if num[i] != '1' and len(numbers_co2)-len(co2_remove)>1:
                    co2_remove.append(num)
            else:
                if num[i] != '0' and len(numbers_co2)-len(co2_remove)>1:
                    co2_remove.append(num)        
        for num in co2_remove:
            numbers_co2.remove(num)
    print(int(numbers_o2[0], 2)*int(numbers_co2[0], 2))
