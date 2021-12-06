import io
import numpy as np

f = io.open("Day1/input.txt", 'r')
values = np.array([int(i) for i in f.readlines()])

# Part 1
number_increasing = sum(np.diff(values) > 0)

print(number_increasing)

# Part 2
sliding_sum = values[0:-2] + values[1:-1] + values[2:]

number_increasing = sum(np.diff(sliding_sum) > 0)
print(number_increasing)