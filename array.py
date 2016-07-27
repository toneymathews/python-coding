#python day 2, 3, 4 ,5 6,7 ,8&9 # Declare second integer, double, and String variables.

j = 0
e = 0.0
t = “”
# Read and save an integer, double, and String to your variables.
j = int(raw_input())
e = float(raw_input())
t = str(raw_input())
# Print the sum of both integer variables on a new line.
print i + j
# Print the sum of the double variables on a new line.
print d + e
print s + t

# Concatenate and print the String variables on a new line
# The ‘s’ variable above should be printed first.







import math

import sys

mealcost=float(raw_input())

tipp=float(raw_input())

taxp=float(raw_input())

tip=float(mealcost*tipp/100)

tax=float(mealcost*taxp/100)

total=int(math.floor(float(mealcost+tax+tip)))

print “The total meal cost is “ + str(total) + “ dollars.”







class Person:
def __init__(self,initialAge):
if initialAge < 0:
  self.initialAge = 0
  print “Age is not valid, setting age to 0.”
else:
  self.initialAge = initialAge
# Add some more code to run some checks on initialAge
def amIOld(self):
  if self.initialAge < 13:
    print “You are young.”
  elif self.initialAge < 18:
    print “You are a teenager.”
  else:
    print “You are old.”
# Do some computations in here and print out the correct statement to the console
def yearPasses(self):
  self.initialAge = self.initialAge + 1
# Increment the age of the person in here







#!/bin/python

import sys

N = int(raw_input().strip())
for i in range(1,11): 
  print str(N) +” x “ +str(i) +” = “+str(N*i)













# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(raw_input().strip())
S = “”
odd = “”
even = “”
for i in range(0,n):
  S = raw_input()
  for j in xrange(0,len(S),2):
    even = even + S[j]
  #print S[j]
#j = j + 2
  for k in xrange(1,len(S),2):
    odd = odd + S[k]
#print S[k]
#k = k + 1
  print even +” “+ odd
  odd = “”
  even = “”













#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(‘ ‘))
arr.reverse()
final =””
for i in range(0, n):
  final = final + str(arr[i]) +” “

print final







# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
i = 0
#print n
e = “”
arr = []
d = dict(raw_input().split() for _ in range(n))
#for keys,values in d.items():
# print keys +” “ +values
#print d
e = str(raw_input())
#while e:
# arr.append(e)
#print e
# e = str(raw_input())
#print e
#strs = [“” raw_input() while not _]
while e:
  if e in d:
  print e +”=”+d[e]
  else:
    print “Not found”
  e = str(raw_input())
  if not e:
    break







import math
n = int(raw_input())
m = math.factorial(n)
print str(m)
