# Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]


def f(my_list):    
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j

        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return my_list



my_list = [5,416,54,21,6135,15,741]
sorted_list = f(my_list)
print(sorted_list)




# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University