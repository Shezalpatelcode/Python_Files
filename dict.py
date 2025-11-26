#To create a empty dictionary 
# my_dict={}
#To create dictionary with integer keys
# my_dict={1:'abc',2:'xyz'}

# #dictionary with mixed keys
# my_dict={'name':'satish','age':27,'address':'Kasukabe'}
# print(my_dict['name'])
# print(my_dict.get('address'))
# print(my_dict.get('degree'))

# #dict add or modify the element
# my_dict['name']='Abhinav'
# my_dict['degree']='M.Tech'
# print(my_dict)

# #Dict Delete or Remove Element
# print(my_dict.pop('age'))
# print(my_dict)
# print(my_dict.popitem())
# print(my_dict)
squares={2:4,3:9,4:16,5:25}

del squares[2]
print(squares)
# del squares
# print(squares)->return a new dictionary with the keys from seq and value]
subjects={}.fromkeys(['math','eng','hindi'],0)
print(subjects)

print(subjects.items())
print(subjects.keys())
print(subjects.values())


print("---------------------------------------")
d={'a':1,'b':2,'c':3,'d':4}
# print(dir(d))
for pair in d.items():
    print(pair)
print("---------------------------------------")
new_dict={k:v for k,v in d.items() if v>2}
print(new_dict)
print("---------------------------------------")
d={k+'c':v*2 for k,v in d.items() if v>2}
print(d)
print("---------------------------------------")

print("---------------------------------------")
kmnklmk
print("---------------------------------------")
kjnjk
print("---------------------------------------")