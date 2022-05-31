#!/usr/bin/python3
import sys

filename = sys.argv[1]
nums = []
with open(filename, 'r') as f:
    for line in f:
        nums.append(int(line.rstrip()))

average = round(sum(nums) / len(nums))
count = 0
for num in nums:
    count += abs(average - num)
print(count)
