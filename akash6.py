# dictoneries--nothing to key value pair

d1 ={}
print(type(d1))
d2 ={"Ram":"dal","Sita":"rice","love":"wheat"
     ,"Akash":{"b":"bread","l":"aloo","d":"egg"}}
#print(d2)
#print(d2["Ram"])
#print(d2["Akash"])
#print(d2["Akash"]["l"])

# how to add another item in list

#d2["kush"] = "burger"
#d2["pru"] = "sandwich"
#print(d2)

# how to remove item in lists
#del d2["kush"]
#print(d2)

#  function in dic---copy,update ,get,
#d3 = d2
#d3 = d2.copy()#used for any fucntion is not delet in dic used copy fucntion
#del d3["pru"]
d2.update({"leena":"gobi"})
print(d2.keys())
print(d2.items())
print(d2)