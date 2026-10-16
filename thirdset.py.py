# lists

# fruits=["apple","mango","banana",12,14,45.10]
# print(fruits)
# print(type(fruits))

# slicing lists
# a=["Ironman","Thor","Captain America","Hulk"]
# print(a[1])

# slicing 2
# a=["Ironman","Thor","Captain America","Hulk"]
# print(a[0:5])
# print(a[1:])

# taking gap
# a=["Ironman","Thor","Captain America","Hulk"]
# print(a[::2])

# reverse list
# a=["Ironman","Thor","Captain America","Hulk"]
# print(a[::-1])

# discarding first value
# a=["Ironman","Thor","Captain America","Hulk"]
# print(a[-1:-4:-1])

# list iteration
# for loop
# a=["Hulk","Thor","Ironman","Captain America"]
# for i in a:
#     print(i)

# iteration using for loop with range and length func
# a=["Hulk","Thor","Ironman","Captain America"]
# for i in range(len(a)):
#     print(a[i])

# using while loop
# a=["Hulk","Thor","Ironman","Captain America"]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# using short hand for loop
# a=["Hulk","Thor","Ironman","Captain America"]
# [print (i) for i in a]

# # list func part 1
# a=["Thor","Hulk","Ironman","Captain America","Hulk"]
# print(a)
# # len func
# print("length: ",len(a))
# # check occurance
# print("count: ",a.count("Hulk"))
# # add to the list
# a.append("Spiderman")
# print("new list: ",a)
# # insert method
# a.insert(1,"vision")
# print("new list: ",a)
#
# # to remove from a list
# a.remove("Spiderman")
# print("new list: ",a)
#
# # remove from certain location
# print(a.pop(1))
# print("new list: ",a)

# list func part 2
# # copy a string
# a=["Thor","Hulk","Ironman","Captain America"]
# b=[]
# print(b)
# b=a.copy()
# print(b)

#access an element
# a=["Thor","Hulk","Ironman","Captain America"]
# print(a.index("Ironman"))

# to extend the list
# a=["Thor","Hulk","Ironman","Captain America"]
# c=["Vision","Spiderman"]
# a.extend(c)
# print(a)

# reverse list
# a=["Thor","Hulk","Ironman","Captain America"]
# print(a)
# a.reverse()
# print(a)

# sort the list
# a=["Thor","Hulk","Ironman","Captain America"]
# print(a)
# a.sort()
# print(a)

# d=[1,7,4,9,10]
# d.sort()
# print(d)

# clear all data from the list
# a=["Thor","Hulk","Ironman","Captain America"]
# a.clear()
# print(a)

# list comprehension
# l1=[30,40,50,60]
# l2=[]
# for i in l1:
#     if i>45:
#         l2.append(i)
#
# print(l1,"\n",l2)
#
# l3=[i for i in l1 if i>45]
# print(l3)

#problem solving
# A=["Ross","Rachel","Monica","Joe"]
# #swap first and forth element
# A[0],A[3]=A[3],A[0]
# print(A)

# A=["Ross","Rachel","Monica","Joe"]
# #add new val at 2nd position
# A.insert(1,"phoebe")
# print(A)

# A=["Ross","Rachel","Monica","Joe"]
# #delete val from 3rd position
# A.pop(2)
# print(A)

# B=[13,7,12,10]
# multiply all the numb in list
# mul=1
# for i in B:
#     mul=mul*i
# print(mul)

# B=[13,7,12,10]
# # find largest number
# largest=0
# for i in B:
#     if i>largest:
#         largest=i
# print(largest)

# another method
# B=[13,7,12,10]
# B.sort()
# print(B)
# print("largest: ",B[-1])
# print("smallest: ",B[0])












