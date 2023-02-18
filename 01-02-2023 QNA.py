# 1)w.a.p to  concatenate given list 
# list_1 = [1,2,3,4]
# list_2 = [a,b,c,d]

# Note: solve it using two method

# 2)w.a.p to add string "krishna" in an empty  list.
# (Try with the method)

# 3)w.a.p to reverse a list = ['a' ,'b' , 'c' ,'d']

# 4) w.a.p to extend a empty list using another list=['alpha','beta','gama'] ===> convert into symbols..

# solutions:

# 1)
list_1 = [1,2,3,4]
list_2 = ['a','b','c','d']

# method :1
print(list_1 + list_2)

# method :2
list_1.extend(list_2)
print(list_1)

# 2)

a = 'krishna'
l= []

# method :1
list_3=list(a) + list(l)
print(list_3)

# method :2
l.append(a)
print(l)

# 3)

list = ['a' ,'c' , 'b' ,'d']

# method :1
list.reverse()
print(list)

# method :2
print(list[::-1])

# method :3
list.sort(reverse=True)
print(list)

# 4)
# Note: "alpha" in Greek: \u03B1 (Unicode code point: 945)
# "beta" in Greek: \u03B2 (Unicode code point: 946)
# "gamma" in Greek: \u03B3 (Unicode code point: 947)

list = ['\u03B1','\u03B2','\u03B3']
empty = []

# method :1
empty.extend(list)
print(empty)

# method :2
Result = list + empty
print(Result)
