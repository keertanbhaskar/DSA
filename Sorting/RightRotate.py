# Right rotate an array by one place
nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
nums[:] = [nums[-1]] + nums[0:n-1]
print(nums)
# Time complexity = O(N)
# Space Complexity = O(1)

# Method = 2
nums[:] = [nums[n-1]] + nums[0:n-1]
print(nums)

# Using For loop
temp = nums[n-1]
for i in range(n-2,-1,-1):
  nums[i+1] = nums[i]
nums[0] = temp
print(nums)
# Time complexity => O(N)
# Space complexity =>  O(1)