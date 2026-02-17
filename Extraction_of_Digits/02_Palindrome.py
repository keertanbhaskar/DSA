# ------Check Palindrome--------
n = 1221
num = n
result = 0
while num > 0:
  last_digit = num % 10
  result = (result * 10) + last_digit
  num = num // 10

if n == result:
  print("The given number",n," is a Palindrome")
  
else:
  print("The given number",n," is Not a Palindrome")

# -----Time complexity is => O(log10(N))
# -----Space complexity is  => O(1)
