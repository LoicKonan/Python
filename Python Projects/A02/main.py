class Cars:
    # Construct for our class.
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost
        
    # Methods that will display Cars Brand
    def showBrand(self):
              return self.brand
          
    # Methods that will display Cars Cost
    def showCost(self):
              return self.cost

# Creating 2 objects cars.
c1 = Cars("Honda",21000)
c2 = Cars("BMW", 35000)

# Displaying the result on the screen with the right spacing.
print("brand: ", c1.showBrand(),"       price: ",c1.showCost())
print("brand: ", c2.showBrand(),"         price: ",c2.showCost())