################################### 
#########   Class Car  ############ 
################################### 
class Car:
    
    # This is the Constructor for the Car class.
    # where we define the efficiency and the initial fuel level to 0.
    def __init__(self, efficiency, tanksize):
        
        # initial fuel level is 0.
        self.__fuelLevel = 0
       
        # The efficiency is specified here.
        self.__efficiency = efficiency
        
        # Variable for the tank size.
        self.__tankSize = tanksize
            
            
    # This method will returns current fuel level.
    def getGasLevel(self):
        return self.__fuelLevel
    
    # This method will adds gas to the tank 
    # and returns how many gallons added.
    def addGas(self, level):

        # if the fuel in the tank size is already equal to the
        # size of the tank size then print tank is full and return 0.
        if self.__fuelLevel == self.__tankSize:
            print("\t    Tank is already full")
            return 0
        
        # else if the the fuel in the tank + the added fuel is 
        # greater than the tank size then return and print 
        # the amount of fuel that was added.
        elif self.__fuelLevel + level > self.__tankSize:
            print("\t    Gas Added: ", self.__tankSize - self.__fuelLevel)
            self.__fuelLevel = self.__tankSize
            return self.__tankSize - self.__fuelLevel
       
       # else it is not full so just print the amount of fuel
       # added and return the level.
        else:
            print("\t    Gas Added: ", level)
            self.__fuelLevel += level
            return level
    
    # This Method will determine the amount of gallons required
    # to travel a given distance. 
    def drive(self, distance):
       
        # calculate gallons required to travel the given distance
        gallonsRequired = distance / self.__efficiency
        
        # Here if the if the fuel if the fuel we 
        # is to small to make the trip then print not enough fuel.
        if self.__fuelLevel - gallonsRequired < 0:
            print("\t    Car does not have enough gas to drive: ", distance)
        
        # else if we have enough fuel print the distance and amount 
        # of fuel left.
        else:
            # Reduce the consumed gallon
            self.__fuelLevel -= gallonsRequired
            milesToDrive = self.__fuelLevel * self.__efficiency
            print("\t    You drove ", distance, " miles. You can drive another ", milesToDrive, "on this gas")


#########################################
#     This method will Open             #
#     the  LogFuel.txt and add          #
#     whatever info the user will add.  #
#########################################

def logMessage(message):
    # Open the file in append mode
    f = open("LogFuel.txt", "a")
    
    # write the message
    f.write(message + "\n")
    
    # Calose the file
    f.close()
  

#############################################
#     This method will Dsiplay              #
#     the menu and get the user choice      #
#############################################

def getMenuChoice():
    print("""\n\n\t    ###########################################
            #                                         #
            #              Welcome To                 #
            #               Eby Anet                  #
            #             CAR DASHBOARD               #
            #                                         #
            #       [1] -- See Current Fuel Level     #
            #       [2] -- Drive                      #
            #       [3] -- Add Gas                    #
            #       [4] -- Exit                       #
            #                                         #
            ###########################################""")
    return int(input("\t    Enter your choice (1-4): "))
  
########################
#                      #
#  The Main Driver.    #
#                      #
########################

if __name__ == "__main__":
        
    # Initialize the different variables that we will use.
    efficiency = 0
    tanksize   = 0
    fileName   = "FuelEffic.txt"
    
    # Open the file in read mode and 
    # read tanksize and efficiency from the FuelEffic.txt file
    # and just grab the numbers by just slpliting them by the ':' 
    # and removing any space.
    with open(fileName, 'r') as f:
        first_line = f.readline().rstrip('\n').strip().split(':')
        second_line = f.readline().rstrip('\n').strip().split(':')
        
        # After slpliting it into 2 part now just grab the number. 
        # since it should be element 1 of the array not element 0.
        efficiency = int(first_line[1])
        tanksize = int(second_line[1])
        
        print("\n\n\t   ##############################  Example  #############################\n")

        # Create an object call myHybrid from our class call Car.
        myHybrid = Car(efficiency, tanksize) # 20 miles per gallon
        # Here we adding 25 gas in the tank.
        myHybrid.addGas(25)
       
        # Drive 100 miles
        myHybrid.drive(100) 
        
        # Print fuel remaining
        print("\t    Fuel level: ", myHybrid.getGasLevel()) 
       
        # Add 9 gallons
        myHybrid.addGas(9) 
        
        # Print fuel remaining
        print("\t    Fuel level: ", myHybrid.getGasLevel())
        print("\n\t   #####################################################################")
        
        
    # Now using The Menu choice for the user, using a while loop
    # and if statement to validate the input.
    choice = 0
    while choice != 4:
        # get user choice
        choice = getMenuChoice()
       
        # if the choice is 1 then we just print the Current Fuel Level.
        if choice == 1:
            logMessage("User Input: 1 -- See Current Fuel Level")
            
            # Print fuel remaining
            print("\t    Fuel level: ", myHybrid.getGasLevel()) 
            logMessage("Fuel level shown: " + str(myHybrid.getGasLevel()))
        
        # if the user choice is 2 then We print the Drive.
        elif choice == 2:
            logMessage("User Input: 2 -- Drive")
            miles = int(input("\t    How many miles to Drive: "))
            logMessage("Miles to Drive: " + str(miles))
            
            # Drive the car
            myHybrid.drive(miles) 
        
        # if the user choice is 3 then we add gas to the tank.
        elif choice == 3:
            logMessage("User Input: 3 -- Add Gas")
            gasToFill = int(input("\t    How much gas to Add: "))
            logMessage("Gas to Fill: " + str(gasToFill))
            addedGas = myHybrid.addGas(gasToFill)
            logMessage("Gas Added: " + str(addedGas))
        
        # if the user choice is 4 then we Exit.
        elif choice == 4:
            logMessage("User Input: 4 -- Exit")
            print("\t    Good Bye \n\t    Au revoir\n\t    see you soon!!!")
            
        # Here if the user choice is invalid then we print invalid choice.
        else:
            logMessage("User Input: " + str(choice) +" - Invalid choice")
            print("\t    Invalid choice!")