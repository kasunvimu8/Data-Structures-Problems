def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp
  return arr


def quick_sort(array, start, end):
  pivot = array[end]
  i=start
  j=end -1
  
  #Returnning point of the quick sort stack
  if end <= start:
    return
  
  while True:
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
      swap(array, i, end)
      quick_sort(array, start, i-1)
      quick_sort(array, i+1, end)
      break
        
    i=i+1

  return array
 
input = [2, 7, 56, 89, 34, 9, 3, 5, 12, 6, 4]
sorted_array = quick_sort(input, 0, len(input) -1)
print(sorted_array)
