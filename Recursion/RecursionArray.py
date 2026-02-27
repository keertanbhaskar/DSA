# Reverse array using Recursion

# array = [5,7,3,2,6,1,5,9]

def Array(array):
  if len(array) ==0:
    return []
  return [array[-1]]+Array(array[:-1])

print("Reversing using Slicing")
print(Array([5,7,3,2,6,1,5,9]))


# using pointers
arr = [5,7,3,2,6,1,5,9]
def reverse_arr(arr,left,right):
  if left >= right:
    return 
  arr[left],arr[right] = arr[right],arr[left]
  reverse_arr(arr,left+1,right-1)

print("\nReversing using pointers")
# reverse_arr(arr, 0, len(arr)-1)  for whole array reversing

# for middle values reversing
reverse_arr(arr,2,5)
print(arr)