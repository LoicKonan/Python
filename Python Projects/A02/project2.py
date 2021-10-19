# try:
#     num = int(input("Enter positive number : "))

#     while not(input() == 'e'):

#         counter = 0

#         comma = ""

#         top = []

#         sum = 0

#         for i in range(1, (num+1)):

#             if(num % i == 0):
#                 a = b = c = 0
#                 a = b   
#                 b = c   
#                 c = i
                
#                 counter = counter + 1
#                 print(comma, i, end ='')
#                 comma = ","

#             if(counter < 4):

#                 top.append(i)
#                 sum += i

#         print("\nTotal number of factor are : ", counter)

#         print('Top 3 :', a, '', b, '', c )

#         avg = float(a+b+c)/3

#         print("Average is : ", avg)
        
# except ValueError:
#     print("You a character so bye Felicia lol !!!")





# function for factors calculation
def factor(a):

    # list which will be used to store the factors
    list = []

    # loop for the numbers between 1 and passed integer
    for i in range(1, a + 1):

        # if the passed integer is divisible by "i" then i is a factor
        if a % i == 0:

           #append i to the list
           list.append(i)

    # return list
    return list

if __name__=="__main__":

    # printing the text to the console for number
    i = int(input("Enter positive number : "))
    
    try:
        while not(input() == 'e'):
            
            # calling the factor method
            factors = factor(i)

            # printing the factors
            print("factors are "+ str(factors))

            # printing the number of factors
            print(" The number "+ str(i)+" has "+ str(len(factors)) + " factors")

            # check if the factors are having atleast 3
            if len(factors) >= 3:

                # print the top 3 factors
                print(" Top 3 Factors are "+ str(factors[-1]) +","+ str(factors[-2]) +","+ str(factors[-3]))

                # print the average 3 factors
                print("average of top 3 factors "+ str((factors[-1] + factors[-2] + factors[-3]) / 3))

            # else print that number of factors are less than 3
            else:
                print("number of factors are less than 3 ")
            
    except ValueError:
        print("You Entered a character so bye Felicia lol !!!")