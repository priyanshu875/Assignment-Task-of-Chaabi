def selection_sort(lst):
    # Traverse through all array elements
    for i in range(len(lst)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst

my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print(sorted_list)
