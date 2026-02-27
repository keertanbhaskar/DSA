# Basic Logic
def func(x,n):
  if n ==0:
    return
  print(x)
  func(x,n-1)

# print 1 to N using recursion
print("----Head Recursion 1 to N-------")
def num(n):
  if n == 0:
    return
  num(n-1)
  print(n)
num(5)

# Tail recursion 1 to N
print("----Tail Recursion 1 to N---------")
def num(X,N):
  if X > N:
    return
  print(X)
  num(X+1,N)
num(1,5)

# Tail Recursion (backtracking) N to 1
print("---Tail Recursion N to 1------")
def func(i,N):
  if i > N:
    return
  func(i+1,N)
  print(i)
func(1,5)

# Head-Recursion N to 1
print("----HeadRecursion N to 1-------")
def number(n):
  if n==0:
    return
  print(n)
  number(n-1)
number(5)
