
# Method - 1
num = [5,6,7,2,3,1,1,7,8]

freq_map = dict() # 0r {}
for i in range(0,len(num)): # O(N)
  if num[i] in freq_map: # O(1) 
    freq_map[num[i]]+=1  # O(1)
  else:
    freq_map[num[i]] =1  # O(1)
print(freq_map)

# Time Complexity => O(N)
# Space Complexity => O(K)
# Space Complexity => O(N) => In worst case

# ------------ Method - 2 -----------------
hash_map = {} # or dict()
n = len(num)
for i in range(0, n): # O(N)
  hash_map[num[i]] = hash_map.get(num[i],0) + 1 # O(1)

print(hash_map)

# Time Complexity => O(N)
# Space Complexity => O(K)
# Space Complexity => O(N) => In worst case