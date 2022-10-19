# Description: This program will Write a codebreaker program that will use the key below to encode or decode a document.
# You will be given an encrypted infile.txt to decode.
# Key
    # A = !
    # E = @
    # I = #
    # O = $
    # U = %
    # a = ^
    # e = &
    # i = *
    # o = (
    # u = )
    # S = +
    # T = -
    # d = >
    # h = ;
    # k = <
    # n = :
    # r = ]
    # s = {
    # t = =
    # y = ]
    
# All other characters will remain the same. 

# Open infile.txt for reading. 
from email.policy import strict


file = open('infile.txt', 'r')

# Read infile.txt
file = file.read()

# Create a dictionary
key = {
    "A" : "!",
    "E" : "@",
    "I" : "#",
    "O" : "$",
    "U" : "%",
    "a" : "^",
    "e" : "&",
    "i" : "*",
    "o" : "(",
    "u" : ")",
    "S" : "+",
    "T" : "-",
    "d" : ">",
    "h" : ";",
    "k" : "<",
    "n" : ":",
    "r" : "]",
    "s" : "{",
    "t" : "=",
    "y" : "]"    
}

# Create a new string
new_string = "".join(key.get(char, char) for char in file)

# Print the new string
print(new_string)

# Decode the string

print(str.encode('utf-8'),'strict')
 