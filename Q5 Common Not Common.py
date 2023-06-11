# Q5. Common, Not Common

# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]


def f(list_a, list_b):

	common = [ st for st in set(list_a) if st in set(list_b) ]

	not_common = [st for st in set(list_a) if st not in common ] + [st for st in set(list_b) if st not in common ]

	return common,not_common



mainStream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]

mustWatch = ["Full Metal Alchemist","Code Geass","DeathNote","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

common, not_common = f(mainStream, mustWatch)
print(common)
print(not_common)


# name - priyanshu agarwal
# reg no-12018473
# University - Lovely Professional University