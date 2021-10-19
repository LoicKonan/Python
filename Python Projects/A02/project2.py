def factor(a):  
    list =[]
    
    for i in range(1, a + 1):   
        
        if a % i == 0:
            
            list.append(i)
            
            return list
        
if __name__ == '__main__':
    
    print('Please enter a number: ')
    
    i = int(input())
    
    factors = factor(i)
    
    print('factors are' + str(factors))
    
    print('The number ' + str(i) + ' has' + str(len(factors)) + ' factors')
    
    if len(factors) > 3:       
        print('Top 3 factors are' + str((factors[-1])) + "" + str((factors[-2])) + "" + str((factors[-3])))
        
        print('Average of Top 3 factors' + str((factors[-1] + factors[-2] + factors[-3]) / 3))
    else:
        print('number of factors are less than 3')