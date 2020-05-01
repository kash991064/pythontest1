# string slicing
# string-String is a combiantion of charecter

mystr1 =("life is an open road enjoy everymovement")
print(len(mystr1))
print(mystr1)
print(mystr1[0:40])

#print(mystr1[78])(Not print result becoz 78 charecter not persent
print(mystr1[0:78])
#slicing
print(mystr1[::])
print(mystr1[0:40:1])
print(mystr1[::1])
print(mystr1[0:])
print(mystr1[:5])

# how to miss cherecter in string example miss two char.
print(mystr1[::2])
# how to use - in string
print(mystr1[-4])
print(mystr1[-4:-6])
print(mystr1[:-7])
print(mystr1[::-1])
print(mystr1[::-3])
# some spicale string charecter
print(mystr1.isalnum())
print(mystr1.endswith("everymovement"))# becoz string end with everymovement
# how to conut char in string
print(mystr1.count("m"))# m is two time in string

# captalize starting chaer in string
print(mystr1.capitalize())
# how to found char in string
print(mystr1.find("an"))

# upper and lower case convert in string
print(mystr1.lower())
print(mystr1.upper())
print(mystr1.isupper())
# repalce char
print(mystr1.replace("is","are"))



