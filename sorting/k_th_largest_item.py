def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp
  return arr

def assign_better_pivot (arr):
  first = arr[0]
  last = arr[len(arr)-1]
  middle = arr[(len(arr)-1) // 2]
  
  min_value = min(first, middle, last)
  max_value = max(first, middle, last)
  mid_index = 0
  
  for i in [0, (len(arr)-1) // 2, len(arr)-1]:
    if(arr[i] <= max_value and arr[i] >= min_value):
      mid_index = i
  
  swap(arr, mid_index, len(arr)-1)

def get_partition_index(arr, start, end):
  assign_better_pivot(arr)
  pivot = arr[end]
  i = start
  for j in range(start, end):
    
    if arr[j] <= pivot :
      swap(arr, i, j)
      i=i+1
  
  swap(arr, i, end)
  return i

def quick_sort(arr, start, end, k):
  if start < end:
    partition_index = get_partition_index(arr, start, end)
    
    if (k < partition_index) :
      quick_sort(arr, start, partition_index-1, k)
    
    if (k > partition_index) :
      quick_sort(arr, partition_index+1, end, k)
    
    if(k == partition_index) :
      return arr
    
  return arr

def get_largest_k_element(arr, k):
  if k > len(arr) or k <= 0:
    return
  
  quick_sort(arr, 0, len(input) -1, len(input) - k)
  return arr[len(input) -1 - k]
