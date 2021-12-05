'''
Logs the message to LogFuel.txt File
'''
def logMessage(message):
    # Open the file in append mode
    f = open("LogFuel.txt", "a")
    
    # write the message
    f.write(message + "\n")
    
    # Calose the file
    f.close()
  

'''
Object-Oriented Programming
Class: Car
'''
class Car:
    # A car has a certain fuel efficiency (measured in miles/gallon)
    # and a certain amount of fuel in the gas tank.
    def __init__(self, efficiency, tanksize):
        
        # The efficiency is specified in the constructor,
        # and the initial fuel level is 0.
        self.__fuelLevel = 0
       
        # measured in miles/gallon
        self.__efficiency = efficiency
        self.__tankSize = tanksize
            
    # returns current fuel level
    def getGasLevel(self):
        return self.__fuelLevel
    
    # adds gas to the tank and returns how many gallons added
    def addGas(self, level):
    
        # if the added fuel exceeds the tank size,
        # have the full tank gas
        if self.__fuelLevel == self.__tankSize:
            print("Tank is already full")
            return 0
        
        elif self.__fuelLevel + level > self.__tankSize:
            print("Gas Added: ", self.__tankSize - self.__fuelLevel)
            self.__fuelLevel = self.__tankSize
            return self.__tankSize - self.__fuelLevel
       
        else:
            print("Gas Added: ", level)
            self.__fuelLevel += level
            return level
    
    def drive(self, distance):
       
        # calculate gallons required to travel the given distance
        gallonsRequired = distance / self.__efficiency
        if self.__fuelLevel - gallonsRequired < 0:
            print("Car does not have enough gas to drive: ", distance)
        
        else:
            # Reduce the consumed gallon
            self.__fuelLevel -= gallonsRequired
            milesToDrive = self.__fuelLevel * self.__efficiency
            print("You drove ", distance, " miles. You can drive another ", milesToDrive, "on this gas")


#Prints the menu and get user choice
def getMenuChoice():
    print("**** MENU ****")
    print("1. See Current Fuel Level")
    print("2. Drive")
    print("3. Add Gas")
    print("4. Exit")
    return int(input("Enter your choice (1-4): "))
  
if __name__ == "__main__":
        
    # read tanksize and efficiency from text file
    efficiency = 0
    tanksize = 0
    fileName = "FuelEffic.txt"
    
    # Open the file in read mode
    with open(fileName, 'r') as f:
        first_line = f.readline().rstrip('\n').strip().split(':')
        second_line = f.readline().rstrip('\n').strip().split(':')
        
        efficiency = int(first_line[1])
        tanksize = int(second_line[1])
        
        myHybrid = Car(efficiency, tanksize) # 20 miles per gallon
        myHybrid.addGas(25)
       
        myHybrid.drive(100) # Drive 100 miles
        print("Fuel level: ", myHybrid.getGasLevel()) # Print fuel remaining
       
        myHybrid.addGas(9) # Add 9 gallons
        print("Fuel level: ", myHybrid.getGasLevel()) # Print fuel remaining
        
    # Run the menu
    choice = 0
    while choice != 4:
        # get user choice
        choice = getMenuChoice()
       
        # See Cureent Fuel
        if choice == 1:
            logMessage("User Input: 1 - See Current Fuel Level")
            print("Fuel level: ", myHybrid.getGasLevel()) # Print fuel remaining
            logMessage("Fuel level shown: " + str(myHybrid.getGasLevel()))
        
        elif choice == 2:
            logMessage("User Input: 2 – Drive")
            miles = int(input("How many miles to Drive: "))
            logMessage("Miles to Drive: " + str(miles))
            myHybrid.drive(miles) # Drive the car
        
        elif choice == 3:
            logMessage("User Input: 3 – Add Gas")
            gasToFill = int(input("How much gas to Add: "))
            logMessage("Gas to Fill: " + str(gasToFill))
            addedGas = myHybrid.addGas(gasToFill)
            logMessage("Gas Added: " + str(addedGas))
        
        elif choice == 4:
            logMessage("User Input: 4 – Exit")
            print("Good Bye, see you soon!")
        else:
            logMessage("User Input: " + str(choice) +" - Invalid choice")
            print("Invalid choice!")