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
    return np.sum(bitvalue * bits)

power = bits2num(gamma) * bits2num(epsilon)
print("Power consumption: ", power)

# Part 2
def ox_criterion(v):
    return sum(v) >= len(v)/2

def co2_criterion(v):
    return sum(v) < len(v)/2

def filter_criterion(bits, criterion):
    subset = bits
    for pos in range(12):
        subset = subset[subset[:,pos] == criterion(subset[:,pos])]
        if len(subset) == 1:
            break
    return subset

ox_rating = bits2num(filter_criterion(bits, ox_criterion))
co2_rating = bits2num(filter_criterion(bits, co2_criterion))

ls_rating = ox_rating * co2_rating
print("Life support rating: ", ls_rating)