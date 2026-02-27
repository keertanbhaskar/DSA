# Palindrome of string  using loop
def palindrome(s):
  n= len(s)
  left = 0
  right = len(s)-1
  while left <right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

print(palindrome("nitin"))
print(palindrome("keertana"))

# Time complexity => O(N)
# Space complexity => O(1)

# ------- Using Recursion -------
print("\nUsing Recursion")
def Palindrome(s,left,right):
  if left >= right:
    return True
  if s[left] != s[right]:
    return False
  return Palindrome(s,left+1,right-1)
s = "madam"
print(Palindrome(s, 0, len(s)-1))