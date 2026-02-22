n = [5,3,2,2,1,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

# Brute-Force Method
print("---------- bruteForce method-----------")
for num in m:
  count = 0
  for x in n:
    if x == num:
      count += 1
  print(count)

#optimal solution
print("--------- Optimal Solution ----------")
hash_list = [0] * 11
for num in n:
  hash_list[num] += 1
for num in m:
  if num <1 or num > 10:
    print(0)
  else:
    print(hash_list[num])

print("-----------using dictionary------------") 
# create frequency dictionary
freq = {}
for number in n:
  freq[number] = freq.get(number,0) + 1

# create result dictionary for m
result = {} 
for number in m:
  result[number] = freq.get(number,0)
print(result)