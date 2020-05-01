# create a dic and take input from user and retrun the menaing
# of  words from  the dic.

#d1={"ok":"all correct","gamble":"bet","early":"beforetime","easy":"simple"}
#print("Enter any of this word \"ok, bet, early, easy\"")
#print(d1[input()])

d2 = {"Love":"a strong feeling somebody","feeling":"a belief",
      "emotion":"a strong feeling","belle":"beautiful"}
d2.update({"true":"sacha"})# updated the dic.
print("Enter any of this  words")
i1 = input()
print(d2[i1])

#dict1 = { "list" : "It is a collection which is ordered and changeable",
 #         "tuple" : "A tuple is a collection which is ordered and unchangeable",
#        "set" : "A set is a collection which is unordered and unindexed",
 #         "dictionary" : "It is a collection which is unordered, changeable and indexed"}
#print("enter the words")
#print(dict1[input()])

#d1={"Hi":"Salut","Good Morning":"Bonjour","Good Evening":"Bonsoir","Bye":"Au Revoir"}
#print("Enter a English word")
#i1=input ()
#print(d1[i1])