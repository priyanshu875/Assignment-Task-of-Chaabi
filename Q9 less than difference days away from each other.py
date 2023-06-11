
# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.


from datetime import datetime

def check_days_difference(from_date, to_date, difference):
	calculated_difference=( datetime.strptime(from_date,'%y-%m-%d') - datetime.strptime(to_date,'%y-%m-%d') ).days
	
	if(calculated_difference < difference):
		return True;
	return False




from_date='23-06-09'
to_date='23-06-01'
difference=11

if( check_days_difference(from_date, to_date, difference) ):
	print(True)
else:
	print(False)



# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University