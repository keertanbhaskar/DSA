def bubbleSort(nums):
  n = len(nums)
  for i in range(n-2,-1,-1):
    swapped = False
    for j in range(0,i+1):
      if nums[j] > nums[j+1]:
        nums[j],nums[j+1] = nums[j+1],nums[j]
        swapped = True
    if swapped == False:
      break
  return nums
    

nums = [5,8,1,6,9,2,4]
bubblesort = bubbleSort(nums)
print(bubblesort)

# time complexity => O(N^2)
# space complexity => O(1)
# time complexity best case => O(N)

