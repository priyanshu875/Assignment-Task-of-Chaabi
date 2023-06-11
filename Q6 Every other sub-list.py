# Q6. Every other sub-list

# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

def f(given_list, st_ind, end_ind):
	sub_list=[]
	for i in range(st_ind, end_ind+1, 2):
		sub_list.append( given_list[i] );

	return sub_list



my_list=[2,3,5,7,11,13,17,19,23,29,31,37,41]
st_ind=2
end_ind=9

sub_list=f(my_list, st_ind, end_ind)
print(sub_list)

# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University