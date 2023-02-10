
# Program prompts user for input of partygoers and pizza. The number of pizzas is multiplied by 8 
# to get the total number of slices between all pizzas. 
# Next, the program calculates how many slices each person will get as well as the remaining slices. 

# User input prompt
people = int(input("How many people are partying? "))
pizza = int(input("How many pizzas did you order? "))

# Math
slices = pizza * 8
totalslices = slices // people
remainder = slices % people

# Print result
print("For " + str(people) + " people and " + str(pizza) + " pizzas, each person will get " + str(totalslices) + " slices and you will have " + str(remainder) + " slice(s) left over.")