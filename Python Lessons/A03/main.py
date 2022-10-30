# Gillian Achord
# CMPS 1023 - Program 4
# This program will decode or encode text in a provided file.

#This function prints a heading.
def heading():
  print("Gillian Achord")
  print("CMPS 1023 - Program 4")
  print("This program will decode or encode") 
  print("text in a provided file.")

#This function scrambles a message.
def encode (fIn, fOut):
  fileIn = open(fIn, "r")
  fileOut = open(fOut, "w")
  for line in fileIn:
    for ch in line:
      if ch == 'A':
        fileOut.write('!')
      elif ch == 'E':
        fileOut.write('@')
      elif ch == 'I':
        fileOut.write('#')
      elif ch == 'O':
        fileOut.write('$')
      elif ch == 'U':
        fileOut.write("%")
      elif ch == 'a':
        fileOut.write('^')
      elif ch == 'e':
        fileOut.write('&')
      elif ch == 'i':
        fileOut.write('*')
      elif ch == 'o':
        fileOut.write('(')
      elif ch == 'u':
        fileOut.write(')')
      elif ch == 'S':
        fileOut.write('+')
      elif ch == 'T':
        fileOut.write('-')
      elif ch == 'd':
        fileOut.write('>')
      elif ch == 'h':
        fileOut.write(';')
      elif ch == 'k':
        fileOut.write('<')
      elif ch == 'n':
        fileOut.write(':')
      elif ch == 'r':
        fileOut.write(']')
      elif ch == 's':
        fileOut.write('}')
      elif ch == 't':
        fileOut.write('=')
      elif ch == 'y':
        fileOut.write('[')
      else:
        fileOut.write(ch)
      
  fileIn.close()
  fileOut.close()

#This function unscrambles a message.
def decode (fIn, fOut):
  fileIn = open(fIn, "r")
  fileOut = open(fOut, "w")
  for line in fileIn:
    for ch in line:
      if ch == '!':
        fileOut.write('A')
      elif ch == '@':
        fileOut.write('E')
      elif ch == '#':
        fileOut.write('I')
      elif ch == '$':
        fileOut.write('O')
      elif ch == '%':
        fileOut.write('U')
      elif ch == '^':
        fileOut.write('a')
      elif ch == '&':
        fileOut.write('e')
      elif ch == '*':
        fileOut.write('i')
      elif ch == '(':
        fileOut.write('o')
      elif ch == ')':
        fileOut.write('u')
      elif ch == '+':
        fileOut.write('s')
      elif ch == '-':
        fileOut.write('T')
      elif ch == '>':
        fileOut.write('d')
      elif ch == ';':
        fileOut.write('h')
      elif ch == '>':
        fileOut.write('k')
      elif ch == ':':
        fileOut.write('n')
      elif ch == ']':
        fileOut.write('r')
      elif ch == '}':
        fileOut.write('s')
      elif ch == '=':
        fileOut.write('t')
      elif ch == '[':
        fileOut.write('y')
      else:
        fileOut.write(ch)
      
  fileIn.close()
  fileOut.close()




# main
heading()
readfile = input("What is the name of your file?\n")
writefile = input("What would like to name the new file?\n")
answer = input("Would you like to encode or decode your file?(Please enter e or d)\n")

#This if statement will tell the user if their input is not vaild
if answer != "e" or answer != "E" or answer != "d" or answer != "D":
  print(answer, "is not a vaild choice, please try again.")
 

while answer == "e" or answer == "E" or answer == "d" or answer =="D":
  #This if statement allows the user to choose to scramble or unscramble their message.
  if answer == "e" or answer == "E":
    encode(readfile,writefile)
  else:
    decode(readfile,writefile)
  
  
