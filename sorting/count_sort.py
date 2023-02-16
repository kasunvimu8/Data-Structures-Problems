def counting_sort(arr, max):
    output = [0 for i in range(len(arr))]

    # initialize a count array
    count_array = [0 for i in range(max)]

    # counting the occurances of inout array
    for j in range(len(arr)):
        count_array[arr[j]] += 1

    # cumalating the occurances in count array
    for k in range(1, max):
        count_array[k] += count_array[k-1]

    # assigning the values
    for l in range(len(arr)):
        val = arr[l]
        index = count_array[val] - 1
        output[index] = val
        count_array[val] -= 1

    return output