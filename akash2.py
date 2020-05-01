# vairable & type of variable(String,Intger and floating point
# string and integer not print on same print command ( example -print(var1+var2)
var1 = "hello world" # string
var2 = 4 # integer
var3 = 35.5 # float
var4 = "hello"
print(var1)
print(type(var1))
print(type(var2))
print(type(var3))
# string and integer not print on same print command
#print(var1+var2)

# but float and integer and two string print one print statement
print(var2+var3)
print(var1+var4)

# TYPE CASTING (String change to integer)str(),int() & float()
var1 = "56 "
var2 = "45"
print(var1+var2)
print(int(var1)+int(var2))

# need to required string in muiltple times using * and for new line using /n(using for new line )
print(10*"hello world\n")
# how to print variable in muiltple times
print(10*str(int(var1)+int(var2)))

# example(how to add number in string using intger function
#print("enter your number")
#inpnum = input()
#print("enter number",int(inpnum)+10)

# project (How to add to number)

print("enter first number")
inpnum1 = input()
print("enter second number")
inpnum2 = input()
print("sum of number", int(inpnum1) + int(inpnum2))
print("div of number",int(inpnum1) / int(inpnum2))
print("mult of number",int(inpnum1) * int(inpnum2))
print("minus of number",int(inpnum1) - int(inpnum2))
print("percent of number",int(inpnum1) % int(inpnum2))


