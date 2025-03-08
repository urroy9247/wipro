def selection_sort(array):
    length = len(array)
    for i in range(length-1):
        index_of_min = i
        for j in range(i+1,length):
            if array[j] < array[index_of_min]:
                index_of_min = j
        array[i] , array[index_of_min] = array[index_of_min],array[i]
    return array
array = [15,78,35,26,9,45,3]  
print("sorted array is:", selection_sort(array))