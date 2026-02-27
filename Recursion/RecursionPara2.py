# Sum of 1 to N(parameterized way)
def func(sum,i,n):
  if i>n:
    print(sum)
    return
  func(sum+i,i+1,n)

func(0,1,10) 
# Time complexity => O(N)
# Space Complexity => O(N) => stack space created


# ------ Functional Recursion ------
def functional(n):
  if n<=1:
    return n
  return n + functional(n-1)
print(functional(0))

# Factorial Problem
def fact(num):
  if num == 0 or num == 1: #f(0) => 1 and f(1) => 1
    return 1
  return num*fact(num-1)
print(fact(5))
# Time complexity => O(N)
# Space Complexity => O(N)