print("_____________________calculator___________________")
a = int (input('First Number : '))
b = int (input('Second Number : '))
opr = input (" Enter an operator '+' , '-' , '*' , '/' : " )
if opr == '+' :
           print(a+b)
elif opr == '-' :
           print(a-b)
elif opr == '*' :
           print(a*b)
elif opr == '/' :
           print(a/b)
else :
           print("error")