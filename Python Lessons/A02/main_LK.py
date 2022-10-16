##############################################################################################
#  
#      Author:           Loic Konan
#      Email:            loickonan.lk@gmail.com
#      Label:            "Experienced Programmer". I am not experienced at all lol.
#      Title:            Program 3
#      Course:           CMPS 1023, Dr. Johnson
#      Semester:         Fall 2022
#      Description:
#                        This program ask the user to enter at least 5 numbers including
#                        floating point numbers. The program has a sentinel number
#                        to indicate that the user is done entering numbers. 
#                        The program will print the average of the numbers entered 
#                        excluding the highest and lowest numbers.
#  
#
#      Usage:
#             main.py          : driver program
#  
#  
##############################################################################################

# Print the program description
print('''##############################################################################################
#  
#      Author:           Loic Konan
#      Email:            loickonan.lk@gmail.com
#      Label:            "Experienced Programmer". I am not experienced at all lol.
#      Title:            Program 3
#      Course:           CMPS 1023, Dr. Johnson
#      Semester:         Fall 2022
#      Description:
#                        This program ask the user to enter at least 5 numbers including
#                        floating point numbers. The program has a sentinel number
#                        to indicate that the user is done entering numbers. 
#                        The program will print the average of the numbers entered 
#                        excluding the highest and lowest numbers.
#  
#
#      Usage:
#             main.py          : driver program
#  
#  
##############################################################################################''')

# Declare and Initialize Variables
counter = 0
total = 0.0
number = 0.0
average = 0.0

# Variables for the highest and lowest numbers
max = 0.0
min = 10.0


print("Enter the scores for each judge. Enter a -1 when finished.\n")

# While loop runs until -1 is entered
while number != -1:
    # Prompt the user to enter a number
    number = float(input("Enter a number: "))
    
    # Make sure the number is between 0 and 10 including floating point numbers.
    if number >= 0.0 and number <= 10.0:
        
        # find the highest number
        if number > max:
            max = number
        
        # find the lowest number    
        if number < min:
            min = number
            
        # Summation of all numbers    
        total += number
        
        # Increment the counter variable.
        counter += 1

    # If the number is not between 0 and 10, print an error message.
    elif number != -1:
        print("Score out of range. Try again.\n")

    # If the user has not entered enough scores, don't break out of the loop.
    elif counter < 5:
        print("You must enter at least 5 scores.")
        number = 0

# Print number of scores entered. 
print("Number of scores entered: ", counter)

# Calculate the Total of the numbers entered by the user, excluding the highest and lowest values.
total = total - max - min
print("total: ", total)

# Calculate average, excluding the highest and lowest values.
average = total / (counter - 2)      

# print the average round up 
print("Final Averaged Score: ", round(average, 1))