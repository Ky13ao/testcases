#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numbersOfSwaps = 0
for i in range(0,n):
  nOSwaps = 0
  for j in range(0,n-1):
    if a[j]>a[j+1]:
      a[j], a[j+1] = a[j+1], a[j]
      nOSwaps += 1
  if nOSwaps==0:
    break
  numbersOfSwaps += nOSwaps
print('Array is sorted in %d swaps.' %numbersOfSwaps)
print('First Element:',a[0])
print('Last Element:',a[n-1])