# loop --used for when print many item in list

#list1 = ["akash","kash","kush","kashi"]
#for item in list1:
 #   print(item)

# when list replace in tuple

#list1 = ("akash","kash","kush","kashi")
#for item in list1:
 #   print(item)

#list in list
#list1 = [["akash",2],["kash",3],["kush",5],["kashi",8]]
#for item in list1:
 #   print(item)# print item list in list

#list1 = [["akash",2],["kash",3],["kush",5],["kashi",8]]
#for item,lollypop in list1:
    #print(item,lollypop)
 #   print(item, "and lollypop is" ,lollypop)

# how to change lists in diconeries   ----
#list1 = [["akash",2],["kash",3],["kush",5],["kashi",8]]
#dic1 = dict(list1)
#print(dic1)
#for item,lollypop in dic1.items():
   # print(item, "and lollypop is" ,lollypop)

# when print only item in lists ---

#list1 = [["akash",2],["kash",3],
 #      ["kush",5],["kashi",8]]
#dic1 = dict(list1)
#for item, in dic1:
 #   print(item)

# example  (quiez)---

list2 = ["A",6,"B",56,"C",23,"D",45]
for number in list2:
    if str(number).isnumeric() and number>6:
     print(number)

 # example 2

list2 = ["cat","401","4297","medicine","key","2","6","4","9","21"]
for item in list2:
    if item.isnumeric():
        if int(item)>6:
            print(item)
# example 3(using dic.)
Dict1 = {"a": 1,"b":7, "c":8}
for item, val in Dict1.items():
    if val>6 and val.isnumeric:
        print(val)






