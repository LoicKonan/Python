# import tkinter as tk
# window = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()
# label_a = tk.Label(master=frame_a, text="Frame A")
# label_a.pack()
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
# frame_a.pack()
# frame_b.pack()
# window.mainloop()


# name = input("what is your name? ")
# age = input("what is your age? ")

# print ("Hello " + name + " You are : " + age + " years old")


# coordinates = (4,5) # Good for coordinates. data that can't be change
# print(coordinates[1])


# Functions
# def cube(number):
#     return pow(number,3) 

# result = cube(4)

# print(result)


# if statement
# is_male = True
# is_tall = True


# if is_male and  is_tall:
#     print("you are a male and Tall ")
    
# elif is_male:
#     print("You are gay")
    
# else: 
#     print("YOu crazy")


# dictionaries


# i = 1
# while i < 3:
#     print("I love u")
#     i+=1
    
# print("\n\nLoop is done")


# friends = ["Jim", "Karen", "Kevin"]


# for index in range(5):
#     if index == 0:
#         print(index)
    
    
# input_file = open("input1.txt", "a")
    
# input_file.write("what")
# input_file.close()


# Classes and object

# class student():
#     def __init__(self, name, major, gpa, age , is_on_probation):
#       self.name = name
#       self.age = age
#       self.gpa = gpa
#       self.major = major
#       self.is_on_probation = is_on_probation



# student1 = student("Loic", "CS", 3.99, 27, False)
# student2 = student("koffic", "History", 3.92, 27, False)

# print(student2)


# mydict = {
#   'key1' : 'value1',
#   'key2' : 'value2',
#   'key3' : 'value3',
#   'key4' : 'value4',
#   'key5' : 'value5',
#   }

# for k,v in mydict.items():
#   print(k)
#   print(v)
  

import sys 
  
class Order:
    def __init__(self, cart =[], customer = None):
      if not isinstance(cart,list):
        print("Cart should be a list")
        sys.exit(0)       
        
      self.cart = list(cart)
      self.customer = customer
                        
      
def some_function(**kwargs):
  pass



def add_nums(*args):
  sum = 0
  for x in args:
    sum += x
    
    return sum
  
# kwargs = keyword arguments
# args - arguments = kwargs

if __name__ == '__main__':
  
  nums = [2,3,4,3,5,6,7]
  
  fruits = ["apple", "banana", "cherry","kiwi", "mango"]
  
  newlist = [x for x in fruits if "a" in x]
  
  
  print(nums[:4])
  print(nums[::-1])
  
  for i in range(0,100,18,):
    print(i)
  
  o1 = Order()
  
  some_function(fname='Joe', lname='Smith', age = 20, bday = 'unkown')
  
  print(add_nums(1,2,3,4,8,9))
  
  
  
  