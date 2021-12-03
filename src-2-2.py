def aoc_2_2(filename):
    horiz = 0
    depth = 0
    aim = 0
    with open(filename) as file:
        for line in file.readlines():
            cmd = line.split()
            num = int(cmd[1])
            if cmd[0] == "forward":
                horiz+=num
                depth+=aim*num
            elif cmd[0] == "down":
                aim+=num
            elif cmd[0] == "up":
                aim-=num
        print(horiz*depth)
