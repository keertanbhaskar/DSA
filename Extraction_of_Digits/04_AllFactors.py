# brute force
n = 10
num = 10
for i in range(1,num+1): # O(N)
  if num % i == 0:
    print(i,end=" ")
    i += 1
# Time Complexity => O(N)
# Space Complexity => O(1)

# ------------another way------------------
print("\n")
result = []
for i in range(1,num+1):
  if num % i == 0:
    result.append(i)
print(result)
  
# TC => O(N)
# SC => O(K)  =>k would be the total number of factors


# ---------- better solution ----------

result = []
for i in range(1,(num//2)+1):
  if num % i == 0:
    result.append(i)
result.append(num)
print(result)

# tc -> O( N/2) == O(N)  sc=> O(K)

# -------optimal solution------
from math import *
result = [] #O(K)
for i in range(1,int(sqrt(num))+1): # O(√N)
  if num % i==0:
    result.append(i)
    if num // i != i:
      result.append(num // i)

result.sort() # O(N logN)
print(result)

# 1.Time complexity => O(√N)+O(N logN)
# 2.Space Complexity => O(K)