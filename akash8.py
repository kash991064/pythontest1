#set---is a collection of data

#s1 = set()
#print(type(s1))

#s_from_list =set([1,2,3,4])
#print(s_from_list)
#print(type(s_from_list))

# or

#list1 = (110,232,363,414,525)
#list_set1 = set(list1)
#print(list_set1)

# how to add elements in set--(set add only unique value)
s1 = set()
s1.add(1)
s1.add(23)
print(s1)

# another example
s1 = set()
s1.add(1)
s1.add(23)
s2 = s1.union({23,45,66,77})
print(s1,s2)

# intersction


s1 = set()
s1.add(1)
s2 = s1.intersection({1,45,66,77})
print(s1,s2)


