#To create a empty dictionary 
# my_dict={}
#To create dictionary with integer keys
# my_dict={1:'abc',2:'xyz'}

#dictionary with mixed keys
my_dict={'name':'satish','age':27,'address':'Kasukabe'}
print(my_dict['name'])
print(my_dict.get('address'))
print(my_dict.get('degree'))

#dict add or modify the element
my_dict['name']='Abhinav'
my_dict['degree']='M.Tech'
print(my_dict)