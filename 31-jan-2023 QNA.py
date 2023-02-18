#    Python Practice Questions with solutions 

# Date: 31/Jan./2023

# 1) write a program to concatenate given to lists
#     list_1 = [1,2,3,4]
#     list_2 = [5,6,7,8]

# 2) write a program to slice a given list 10.0 to 0j
#     a = [1, 'krishna', 10.0, 0j, (4+2j) ]

# 3) write a program to convert case of  given string to uppercase
#     a = "abcdefghijklmnopqrstuvwxyz"

# 4) write a program to convert a given string's case to lowercase but without using lower() method.
# Email ="NnkriShnakumar714@gmail.com"

# 5) write a program to remove both sides spaces from the given string.
# a = "        NnkriShnakumar714@gmail.com     "

# 6) write 3 programs to get the mentioned string result.
# c = "krishna"
# d = "kumar"
# result = "krishnakumar"

# 7) write a program to get the result output.
# c = "krishna       "
# d = "      kumar"
# result = "krishnakumar"



# Solution:

# 1)
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
# a=list_1.extend(list_2)
print(list_1 + list_2)
# print(a)

# 2)
a = [1, 'krishna', 10.0, 0j, (4+2j) ]
print(a[2:4])
print(a[-3:-1])
print(a[2:-1])
print(a[-3:4])

# 3)
a = "abcdefghijklmnopqrstuvwxyz"
print(a.upper())

# 4)
Email ="NnkriShnakumar714@gmail.com"
print(Email.casefold())

# 5)
a = "        NnkriShnakumar714@gmail.com     "
print(a.strip())

# 6)
c = "krishna"
d = "Kumar"
# result = "krishnakumar"

# program 1:

print(c + d)

# program 2:

result=''.join([c,d])
print(result)

# program 3:

print(c,d,sep='')

# 7)
c = "krishna       "
d = "      kumar"
# result = "krishnakumar"

# method 1:

c = "krishna       "
d = "      kumar"
result = c.strip() + d.strip()
print(result)

# method 2:

c = "krishna       "
d = "      kumar"
result = c.replace(" ", "") + d.replace(" ", "")
print(result)


