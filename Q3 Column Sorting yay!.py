# Q3. Column Sorting, yay!

# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]


def get_key(given_dict, sorting_key):
	return given_dict[sorting_key];

def f(dict_list, sorting_key):
	sorted_dict_list=sorted(dict_list, key=lambda given_dict: get_key(given_dict, sorting_key) );
	return sorted_dict_list



dict_list =[
	{"fruit": "orange", "color": "orange"},
	{"fruit": "apple", "color": "red"},
	{"fruit": "banana", "color": "yellow"},
	{"fruit": "blueberry", "color": "blue"}
]

sorting_key="color"

sorted_dict_list=f( dict_list , sorting_key );
print(sorted_dict_list)


# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University