def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
      return False
  return True

array = [3,6,1,7,8,9]
arrList = is_sorted(array)
print(arrList)

# time complexity => O(N)
# Space complexity = > O(1) 