# program for faulty calucator
# 45*3  = 555,56+9 =77,54/6 =4,125%25 =456

#num1 = int(input("enter the first number:-"))
#num2 = int(input("enter the second number:-"))
#opr = input("what operation you want to perform (example : +, -, *,) ")
#calculator = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "/": num1 / num2,}
#FaultyCalculator = {"+": 77, "*": 555, "/": 4}# (CREATE DIC FOR FAULTY VALUE)
#if (((num1 == 45 and num2 == 3) or (num1 == 3 and num2 == 45)) and opr == '*'):
 #   print(FaultyCalculator[opr])
#elif (((num1 == 56 and num2 == 9) or (num1 == 9 and num2 == 56))  and opr == '+'):
 #   print(FaultyCalculator[opr])
#elif (((num1 == 56 and num2 == 6) or (num1 == 6 and num2 == 56))  and opr == '/'):
 #   print(FaultyCalculator[opr])
#else:
 #   print(calculator[opr])


# example:---
no1 = int(input("enter 1st number:-"))
no2 = int(input("enter 2nd number:-"))
operation = input("eneter calculator operation permeter(example : % ,- ,+,/,)")
calculator = {"%":(no1/no2)*100,"-":no1-no2,"+":no1+no2,"/":no1/no2,} # diconeries
print(calculator[operation])
