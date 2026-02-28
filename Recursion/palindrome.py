# Fibonacci Problem solving Recursion

def fun(num):
  if num <=1:
    return num
  return fun(num-1)+fun(num-2)

print(fun(5))

# Time complexity => O(2^n)
# Space complexity => O(2^n)
