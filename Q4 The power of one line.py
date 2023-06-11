# Q4. The power of one line -
# Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
# key becomes value. The function's body shouldn't have more than one statement.
# f({
# "key1": "value1",
# "key2": "value2",
# "key3": "value3",
# "key4": "value4",
# "key5": "value5"
# }) should return
# {
# "value1": "key1",
# "value2": "key2",
# "value3": "key3",
# "value4": "key4",
# "value5": "key5"
# }


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


# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University
