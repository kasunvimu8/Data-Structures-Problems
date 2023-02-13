def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp
  return arr

# start : start element index
# start : last element index
def get_partition_index(arr, start, end):
  pivot = arr[end]
  i = start
  for j in range(start, end):
    
    if arr[j] <= pivot :
      swap(arr, i, j)
      i=i+1
  
  swap(arr, i, end)
  return i

def quick_sort(arr, start, end):
  if start < end:
    partition_index = get_partition_index(arr, start, end)
    quick_sort(arr, start, partition_index-1)
    quick_sort(arr, partition_index+1, end)
    
  return arr

def quick_sort_algorithm(arr):
  return quick_sort(arr, 0, len(input) -1)

input = [2, 54, 4, 9, 79, 56, 89, 34, 9, 3, 5, 12, 6, 4]
sorted_array = quick_sort_algorithm(input)
print(sorted_array)
