def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp
  return arr

# # Wrong Implementation
# def quick_sort(array, start, end):
#   pivot = array[end]
#   i=start
#   j=end -1
  
#   #Returning point of the quick sort stack
#   if end <= start:
#     return
  
#   while True:
#     if(array[i] > pivot):
      
#       while j != i:
#         if (i == j):
#           break
        
#         if(array[j] <= pivot):
#           swap(array, i, j)
#           j=j-1
#           break
        
#         j=j-1
      
#     if(i == j):
#       swap(array, i, end)
#       quick_sort(array, start, i-1)
#       quick_sort(array, i+1, end)
#       break
        
#     i=i+1

#   return array

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
