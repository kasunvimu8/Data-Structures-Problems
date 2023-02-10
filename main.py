def swap(arr, index1, index2):
  temp = arr[index1]
  arr[index1] = arr[index2]
  arr[index2] = temp
  return arr


def quick_sort(array):
  pivot = array[len(array) -1]
  i=0
  while i < (len(array) -1):
    if(array[i] > pivot):
      swap(array, i , )
  return array


sorted_array = quick_sort([2, 7, 4, 3, 6, 1, 5, 4])
print(sorted_array)
