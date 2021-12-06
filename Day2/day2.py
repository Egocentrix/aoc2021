import io

f = open("Day2/input.txt",'r')

pos = 0
depth = 0
aim = 0
for line in f.readlines():
    cmd, arg = line.split()

    if cmd == "forward":
        pos += int(arg)
        depth += aim * int(arg)
    elif cmd == "down":
        aim += int(arg)
    elif cmd == "up":
        aim -= int(arg)

print(pos)
print(depth)
print(pos * depth)
