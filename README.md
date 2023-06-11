# Assignment-Task-of-Chaabi

**Q1. Get your basics right** - Implement selection sort algorithm in python. The function accepts a
list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135]

```
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

```
<hr/>
**Q2. Dictionary, what?**
Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs
E.g.
f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]) should return
{
"abc.jpg": "image",
"xyz.xls": "spreadsheet",
"Text.csv": "unknown",
"123": "unknown"
}

```
def f(extension_and_type, file_list):
    tmp_ext = [pair.split(',') for pair in extension_and_type.split(';')]
    ext_dict = {pair[0]: pair[1] for pair in tmp_ext}

    type_pairs = {}

    for file in file_list:
        ext = file.split('.')[-1]
        file_type = ext_dict.get(ext)
        type_pairs[file] = file_type

    return type_pairs


extension_and_type = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv", "123"]

type_pairs = f(extension_and_type, file_list)
print(type_pairs)

```
<hr/>
**Q3. Column Sorting, yay!**

Given a list of dicts, write a program to sort the list according to a key given in input.
E.g.
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")
Should Output
[
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"}
]

```
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
```

<hr/>
**Q4. The power of one line -**
Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
key becomes value. The function's body shouldn't have more than one statement.
f({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}) should return
{
"value1": "key1",
"value2": "key2",
"value3": "key3",
"value4": "key4",
"value5": "key5"
}

```
def f(given_dict):
    return {value:key for key, value in given_dict.items()}



curr_dict={
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

new_curr_dict=f( curr_dict )
print(new_curr_dict)
```

<hr/>
**Q5. Common, Not Common**

Given 2 lists in input. Write a program to return the elements, which are common to both
lists(set intersection) and those which are not common(set symmetric difference) between the
lists.
Input:
Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death
Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
On Titan"]
f(mainstream, must_watch) should return:
["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
"One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

```
def f(list_a, list_b):

	common = [ st for st in set(list_a) if st in set(list_b) ]

	not_common = [st for st in set(list_a) if st not in common ] + [st for st in set(list_b) if st not in common ]

	return common,not_common



mainStream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]

mustWatch = ["Full Metal Alchemist","Code Geass","DeathNote","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

common, not_common = f(mainStream, mustWatch)
print(common)
print(not_common)
```

<hr/>
**Q6. Every other sub-list**

Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
contain every second element.
E.g.
Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
Return [5, 11, 17, 23]

```
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
```

<hr/>
**Q7. Calculate the factorial of a number using lambda function.**

```
getFactorial=lambda n:1 if n==0 else n*getFactorial(n-1)


num=5
calculated_factorial = getFactorial(num)
print(calculated_factorial)
```
<hr/>
**Q8. Some neat tricks up her sleeve:**

Looking at the below code, write down the final values of A0, A1, ...An

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

A1 = range(10)

A2 = sorted([i for i in A1 if i in A0])

A3 = sorted([A0[s] for s in A0])

A4 = [i for i in A1 if i in A3]

A5 = {i:i*i for i in A1}

A6 = [[i,i*i] for i in A1]

A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])

A8 = map(lambda x: x*2, [1,2,3,4])

A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"])

```
A0: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1: range(0,10)
A2: []
A3: [1, 2, 3, 4, 5]
A4: [1, 2, 3, 4, 5]
A5: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6: [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
A7: 21
A8: [2, 4, 6, 8]
A9: ["want", "learn", "python"]

```
<hr/>

**Q9.**
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days away from each other, else
returns False.

```
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

```
<hr/>
**Q10. Of date and days**
Write a func that takes 2 args:
date - string representing a date in the form of 'yy-mm-dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16-12-10', 11) should return '16-11-29'

```
from datetime import datetime, timedelta

def of_date_and_days(date, n):

	resultant_date=( (datetime.strptime(date, '%y-%m-%d') ) - timedelta(n) ).strftime('%y-%m-%d')
	return resultant_date


given_date='23-06-10'
n=1

previous_date = of_date_and_days( given_date, n)

print(previous_date)
```
<hr/>

**Q.11 Find output of following:**

def f(x,l=[]):
	for i in range(x):
		l.append(i*i)
	print(l)



f(2) 
f(3,[3,2,1])
f(3)

```
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]
```
