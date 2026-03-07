# Finding 2nd largest element without using sorting
arr = [10, 5, 20, 8, 15, 89,77]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)