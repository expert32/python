def add (num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def sub(num1,num2):
    return(num1-num2)

def main():
    num1 = int(input("Enter First no : "))
    num2 = int(input("Enter Second no : "))

    operation= input("what do you do with this no sub add mul ")

    if(operation == "add"):
       print(add(num1,num2))
       
    elif(operation == "sub"):
     print(sub(num1,num2))
     
    elif(operation == "mul"):
     print(mul(num1,num2))
    
    
main()
             
