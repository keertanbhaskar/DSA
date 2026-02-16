# -------Logic ------------
num = 1024 // 10
print(num)

# ---- Count of Digits------
count = 0
number = int(input("Enter the number: "))
while number > 0:
  number = number // 10
  count += 1
print(count)
# ------------time complexity : O(log10(N))
# ------------Space Complexity : O(1)



# ---- Using Math Module----------
from math import *
def countDigits(number1):
  return int(log10(number1) + 1)

logNumber = countDigits(64383976335)
print("Length of number is: " , logNumber)
# ------------time complexity : O(1)
# ------------Space Complexity : O(1)



