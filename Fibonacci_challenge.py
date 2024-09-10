



def Fibonacci():
    try: 
        num1= 0 
        num2 = 1
        n = int(input("Enter How many number of Fibonacci challenge :"))
        if(n<=0):
            raise Exception("Sorry, no numbers below zero") 
        
        if(n>=1):
            print(num1)
          
            for i in range(1,n):
                print(num2)
                temp = num2 
                num2 = num2+num1 
                num1 = temp
             
    
    
    except Exception as e: 
        print("Error:", repr(e))    
        
        
Fibonacci()        