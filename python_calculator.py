def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    
        return x/y
    
a=int(input("Enter the first number-"))
b=int(input("Enter the second number-"))
print("Press 1 for addition")
print("Press 2 for subraction")
print("Press 3 for multiplication")
print("Press 4 for division")
choice=int(input("Enter your choice-"))
valid=0
if choice>0 and choice<5:
    if choice==1:
        answer=addition(a,b)
    elif choice==2:
        answer=subtraction(a,b)
    elif choice==3:
        answer=multiplication(a,b)
    else:
        if b!=0:
            answer=division(a,b)
        else:
            valid=1
            print("Division by zero is not possible!!!")
            
else:
    print("Enter valid choice!!")
if valid==0:
    
    print("Your answer is ", answer)
    
