# function for factors calculation
def factor(a):

    # myArray which will be used to store the factors
    myArray = []

    # loop for the numbers between 1 and passed integer
    for i in range(1, a + 1):

        # if the passed integer is divisible by "i" then i is a factor
        if a % i == 0:

           #append i to the myArray
           myArray.append(i)

    # returning myArray
    return myArray

if __name__=="__main__":
    
    print("Enter a positive number  or enter the letter e to end the program: ")
    
    # This try block will make will run as long as the input enter a valid number. ie not the character 'E' or 'e'
    try:
               
        # this while loop will only execute if we have a valid number.
        while True:
            
            # printing the text to the console for number
            i = int(input())
            
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
            
    # this except block will run when the user enter the E or 'e'. and end the program.
    except ValueError:
        print("You should enter a number instead, anyway bye Felicia lol !!!")