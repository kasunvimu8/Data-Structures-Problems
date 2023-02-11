def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp
  return arr


def quick_sort(array, start, end):
  pivot = array[end]
  i=start
  j=end -1
  
  while i < (end -1):
    
    if(array[i] > pivot):
      
      while j != i:
        if (i == j):
          break
        
        if(array[j] <= pivot):
          swap(array, i, j)
          j=j-1
          break
        
        j=j-1
      
    if(i == j):
      swap(array, i+1, len(array) -1)
      quick_sort(array, start, i)
      quick_sort(array, i+2, end)
      break
        
    i=i+1

  return array
 
sorted_array = quick_sort([2, 7, 4, 3, 6, 1, 5, 4])
print(sorted_array)
