
name = 'Michael Jackson'
# indexes
# M = 0 = -15
# i = 1 = -14
# c = 2 = -13
# h = 3 = -12
# a = 4 = -11
# e = 5 = -10
# l = 6 = -9
# ' ' = 7 = -8
# J = 8 = -7
# a = 9 = -6
# c = 10 = -5
# k = 11 = -4
# s = 12 = -3
# o = 13 = -2
# n = 14 = -1

# name[0:4] = Mich
# name[8:12] = Jack
# name[::2] = McalJcsn -> jumps of 2
# name[0:5:2] = Mca -> the second position is for slicing
print(len(name))
#len command to get de length of the string
statement =  name + ' is the best'
print(len(3 * name))

# \n ->  new line
# \t -> tab
# \\ -> \

# Strings methods
A = 'Thriller is the sixth studio album'
B = A.upper() # THRILLER IS THE SIXTH STUDIO ALBUM
C = A.replace('sixth','fourth') # Thriller is the fourth studio album
D = A.find('er') # 6 -> first index of the sequence ( -1 if is not theredata)
print(D)

print("0123456".find('1'))

var = '01234567'
print(var[::2])