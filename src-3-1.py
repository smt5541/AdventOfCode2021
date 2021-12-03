def aoc_3_1(filename):
    length = 0
    zero_bits = []
    one_bits = []
    gamma_rate = ''
    epsilon_rate = ''
    with open(filename) as file:
        for line in file.readlines():
            if length == 0:
                for char in line:
                    if (char != '\n'):
                        length+=1
                        zero_bits.append(0)
                        one_bits.append(0)             
            for i in range(length):
                if line[i] == '0':
                    zero_bits[i]+=1
                else:
                    one_bits[i]+=1
        for i in range(length):
            if zero_bits[i] > one_bits[i]:
                gamma_rate+='0'
                epsilon_rate+='1'
            else:
                gamma_rate+='1'
                epsilon_rate+='0'
    print(int(gamma_rate, 2)*int(epsilon_rate, 2))
                
