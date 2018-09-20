def add (num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def sub(num1,num2):
    return(num1-num2)

def main():
    
    validInput = False
    
    while not validInput:
    
      try:
       num1 = int(input("Enter First no : "))
       num2 = int(input("Enter Second no : "))
       operation= int(input("what do you do with this no 1.sub 2.add 3.mul "))
       validinput = True
      except:
         print("invaild input Try again")
         
    if(operation == 2): 
       print(add(num1,num2))
       
    elif(operation == 1):
      print(sub(num1,num2))
     
    elif(operation == 3):
      print(mul(num1,num2))
    else:
     print("I don't understand")
       
main()
             
