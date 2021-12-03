def aoc_2_1(filename):
    horiz = 0
    depth = 0
    with open(filename) as file:
        for line in file.readlines():
            cmd = line.split()
            num = int(cmd[1])
            if cmd[0] == "forward":
                horiz+=num
            elif cmd[0] == "down":
                depth+=num
            elif cmd[0] == "up":
                depth-=num
        print(horiz*depth)
