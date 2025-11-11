#Wrting the set 
s={1,2,3,1,2,4}
#printing the set
print(s)
#----------------------------------------
#printing the type of set
print(type(s))
#----------------------------------------
#Adding the single element
s.add(5)
print (s)
#----------------------------------------
# using update() method we can add many elemnets
s.update([6,7,8,3])
print(s)
#----------------------------------------
#adding the list and set
s.update([6,7,8,3],{9,10})
print(s)
#----------------------------------------
s.discard(4)
print(s)
#----------------------------------------
s.pop()
print(s)
#----------------------------------------
# s.clear()
# print(s)
set1 = {1, 2, 3, 4, 5, 6}
set2 = {6, 7, 8, 9, 10}

print(set1 | set2)     
# union operator

print(set1.union(set2))

#for intersection 
print(set1 & set2)
print(set1.intersection(set2))

# for difference
print(set1 - set2)
print(set1.difference(set2))
#--------------------------------------
#Symmetric difference
print(set1^set2)
print(set1.symmetric_difference(set2))

#Subset
x={"e","a","b","c","d"}
y={"c","d"}
print("set  x is subset of y ?",x.issubset(y))
print("set  y is subset of x ?",y.issubset(x))

set3 = frozenset([1, 2, 3, 4, 5])
set4 = frozenset([6, 7, 8, 9, 10])
# set3.add(5)


