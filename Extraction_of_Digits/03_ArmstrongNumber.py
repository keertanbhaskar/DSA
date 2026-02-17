n = 153
num = n
nod = len(str(n))
total = 0
while num :
  ls = num %10
  total = (total) + (ls ** nod)
  num = num // 10

print(total)
if total == n:
  print("Armstrong Number")
else:
  print("Not an Armstrong Number")