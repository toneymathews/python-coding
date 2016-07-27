#occurance of largest interger in an array
#!/bin/python3

import sys
occurance = 0
max = 0
n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
for i in range(0,n):
    if max < height[i]:
        max = height[i]
for i in range(0,n):
    if max == height[i]:
        occurance = occurance + 1
print (occurance)
        
    
