import io

f = open("Day2/input.txt",'r')

pos = 0
depth = 0
for line in f.readlines():
    cmd, arg = line.split()

    if cmd == "forward":
        pos += int(arg)
    elif cmd == "down":
        depth += int(arg)
    elif cmd == "up":
        depth -= int(arg)

print(pos)
print(depth)
print(pos * depth)

