# Remove Duplicates from sorted Array[In Place].
# Method = BruteForce method
def Remove_dup(nums):
  n = len(nums)
  freq_map = {}
  for i in range(0,n):
    freq_map[nums[i]] = 0
  j=0
  for keys in freq_map:
    nums[j] = keys
    j+=1
  return j

num = [1,1,1,2,3,4,4,7,9,9,9,10]
nums = Remove_dup(num)
print(num)
# Time Complexity = O(2N) ~ O(N)
# Space Complexity = O(N)



# Method = Optimal Solution
def remove_dup(nums):
  n = len(nums)
  if n == 1:
    return 1
  i = 0
  j = i + 1
  while j < n:
    if nums[j] != nums[i]:
      i+=1
      nums[i]= nums[j]
    j += 1
  return i+1

Array_val = [1,1,1,2,3,4,4,7,9,9,9,10]
RemoveDuplicates = remove_dup(Array_val)
print(Array_val[:RemoveDuplicates])
print(RemoveDuplicates)
# Time Complexity = O(N)
# Space Complexity = O(1)