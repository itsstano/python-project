def add(A,B):
 #This function is used for adding two numbers
 return A+B
def subtract(A,B):
 #This function is used for subtracting two numbers
  return A-B
def multiply(A,B):
 #This function is used for multiplying two numbers
 return A*B
def divide(A,B):
 #This function is used for dividing two numbers
 return A/B
#input from the user
print("please select the operation")
print('a.Add')
print('b.Subtract')
print('c.Multiply')
print('d.Divide')

choice=input('please enter choice(a/b/c/d):')

num=int(input('enter first number'))
num1=int(input("enter second number"))

if choice=='a':
 print(num, '+' ,num1,'=',add(num,num1))
elif choice=='b':
 print(num,'-',num1,'=',subtract(num,num1))
elif choice=='c':
 print(num,'*',num1,'=',multiply(num,num1));
elif choice=='d':
 print(num,'/',num1,'=',divide(num,num1))
else:
 print('this is an invalid option')