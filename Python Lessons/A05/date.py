# This program determines whether your birthdate is magic or not. Input from the user about their birthdate is read and the product of the month and day is calculated. If the answer is equal to the year provided, your birthdate is magic, if not then it is not magic.

#Introduces program
print ("Jahkeel Warner")
print ("CMPS 1023")
print ("This program determines whether your birthdate is magic or not. Input from the user about their birthdate is read and the product of the month and day is calculated. If the answer is equal to the year provided, your birthdate is magic, if not then it is not magic.")

#User prompt
Month = 0
while Month > 12 or Month < 1:
  Month = int (input("Please enter month of birth.   "))

Day = 0
while Day > 31 or Day < 1:
  Day = int (input ("Please enter day of birth.     "))

Year = -1
while Year > 99 or Year < 0:
  Year = int (input ("Please enter year of birth.    "))

#Establishes and stores date format  
date = [Month, Day, Year]
Bday = "Your birthdate is {0}/{1}/{2}".format(date[0], date[1], date[2])
DOB = "{0}/{1}/{2}".format(date[0], date[1], date[2])
print(Bday)

#Calculates and establishes results with rationale
if Month * Day == Year:
  print (DOB + " is MAGIC! because " + str(Month) + " * " + str(Day) + " = " + str(Year) + ".")
else:
  print (DOB + " is NOT MAGIC! because " + str(Month) + " * " + str(Day) + " ≠  " + str(Year) + ".")
