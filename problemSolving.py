
# covert dictionary into json
# import json
# Student_data= {"name": "David","age":13,"marks":87}
# print(type(Student_data))
# data= json.dumps(Student_data)
# print(data)
# print(type(data))

# access value of age
# import json
# Student_data= """{"name": "David","age":13,"marks":87}"""
# data=json.loads(Student_data)
# print(data["age"])

# # pretty print given json data
# import json
# Student_data={"name":"David","age":13,"marks":87}
# data=json.dumps(Student_data,indent=4,separators=(",","="))
# print(data)

# sort following json keys and write them into a file
# import json
# Student_data={"name":"David","age":13,"marks":87}
# f=open("demo.json","w")
# data=json.dumps(Student_data,indent=4,sort_keys=True)
# f.write(data)
# print("data added to file")

# access the nested key "marks" from the data

# Student_data = {"name": "David", "age": 13, "marks": 87}
# print(Student_data["marks"])

# multiply student data
# mul=1
# B=[13,7,12,10]
# for i in B:
#     mul*=i
#
# print(mul)

# # find largest number
# B=[13,7,12,10]
# B.sort()
# print(B)
# print("largest value: ",B[-1])
# print("smallest valuee: ",B[0])

# marks=[85,90,76]
# marks.append(95)
# print(marks)

# B=[13,7,12,10]
# B.extend([34,54])
# print( B)


# B=[13,7,12,10]
# B.insert(1,99)
# print(B)

# B=[13,7,12,10]
# B.remove(12)
# print( B)
#
# B=[13,7,12,10]
# B.pop(1)
# print(B)

