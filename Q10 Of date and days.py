
# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

from datetime import datetime, timedelta

def of_date_and_days(date, n):

	resultant_date=( (datetime.strptime(date, '%y-%m-%d') ) - timedelta(n) ).strftime('%y-%m-%d')
	return resultant_date


given_date='23-06-10'
n=1

previous_date = of_date_and_days( given_date, n)

print(previous_date)



# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University