# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }


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



# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University