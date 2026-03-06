'''
# ---------- conditions --------
1) Pick a Pivot
  -It can be the 1st element
  -It can be the last element
  -It can be the middle element
  -It can be any random element

2) Put pivot at its correct Position/index

'''
# choosing 1st element as pivot
def partition(nums, low, high):
  pivot = nums[low]
  i = low
  j=high
  while i < j:
    while nums[i] <= pivot and i<= high-1:
      i+=1
    while nums[j] >pivot and j >= low + 1:
      j -= 1
    if i < j:
      nums[i],nums[j] = nums[j],nums[i]
  nums[low],nums[j] = nums[j],nums[low]
  return j

def quickSort(nums,low,high):
  if low < high:
    p_index = partition(nums,low,high)
    quickSort(nums,low,p_index-1)
    quickSort(nums,p_index+1,high)

nums = [4,1,6,8,3,9,5]
quicksort = quickSort(nums,0,len(nums)-1)
print(nums)


# Time Complexity => O(N logN) => bestCase and average case
# Time Complexity => worstCase => O(N^2) Example = [5,5,5,5,5,5,5,5] => if all elements same in list
# Space Complexity = O(1)


