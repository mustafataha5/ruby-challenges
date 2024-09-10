


def missing_number(arr) : 
    try: 
    
        arr = sorted(arr)
        miss = arr[0]          
        for i in range(0,len(arr)):
           # print(arr[i],'   ',miss)
            if arr[i]!= miss :
                 return miss 
            miss = miss+1
        
        return None
    
    except Exception as e:
        print("Error:",repr(e))     
        
print(missing_number([2,5,4,3,7]))        