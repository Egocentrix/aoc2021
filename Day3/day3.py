import io
import numpy as np 

# Load bits into array
f = open("Day3/input.txt",'r')
report = [ list(i) for i in f.readlines()]
bits = np.array(report) [:,:-1].astype(int)

# Part 1
gamma = sum(bits,0) > len(bits)/2
epsilon = np.invert(gamma)

def bits2num(bits):
    bitvalue = [2**i for i in range(11,-1,-1)]
    return sum(bitvalue * bits)

power = bits2num(gamma) * bits2num(epsilon)
print("Power consumption: ", power)
