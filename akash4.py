# lists-----

grocery = ("tea","shop","jeera","vim","coffee",56,67)
print(grocery)
print(grocery[1])

# number lists

number1 = [1,3,4,6,8]
print(number1)
print(number1[4])
# sort and reverse function-change the oringinal list

number2 = [1,5,4,6,2]
number2.sort()
number2.reverse()
print(number2)
#slicing---slicing create new list but old list not change
print(number2[0:5])
print(number2[:5])
print(number2[:])
print(number2[1:4])

# extened function---
print(number2[::2])
print(number2[::-1])

# when add some item in the list---used append function
number2 = [1,5,4,6,2]
number2.append(8)
print(number2)
# insert function--number add after two no.in list
number2.insert(2,9)
print(number2)

# remove function--remove 5 in list
number2.remove(5)
print(number2)

# pop function---remove last no in list
number2.pop()
print(number2)


