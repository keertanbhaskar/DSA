# Selection Sort

def selection_Sort(num):
  n = len(num)
  for i in range(0,n):
    min_index = i
    for j in range(i+1,n):
      if num[j] < num[min_index]:
        min_index = j
    num[i],num[min_index] = num[min_index],num[i]
  return num

num = [2,6,9,1,4,8,3]
selectionSort = selection_Sort(num)
print(selectionSort)