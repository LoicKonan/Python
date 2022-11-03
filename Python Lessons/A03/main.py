# This program reads in a file to be decoded or encoded and then outputs the encoded or decoded text to a new file.
def decode(fIn, fOut): # defining "decode" function
  with open(fIn, "r") as fileIn:
    fileOut = open(fOut, "w") # assigning fileOut to write file
    for line in fileIn: # for each line in read file...
      for ch in line: # for each character in each line...
        # replace encoded characters with 'true' characters
        if ch == '!':
          fileOut.write('A');
        elif ch == '@':
          fileOut.write('E');
        elif ch == '#':
          fileOut.write('I');
        elif ch == '$':
          fileOut.write('O');
        elif ch == '%':
          fileOut.write('U');
        elif ch == '^':
          fileOut.write('a');
        elif ch == '&':
          fileOut.write('e');
        elif ch == '*':
          fileOut.write('i');
        elif ch == '(':
          fileOut.write('o');
        elif ch == ')':
          fileOut.write('u');
        elif ch == '+':
          fileOut.write('S');
        elif ch == '-':
          fileOut.write('T');
        elif ch == '>':
          fileOut.write('d');
        elif ch == ';':
          fileOut.write('h');
        elif ch == '<':
          fileOut.write('k');
        elif ch == ':':
          fileOut.write('n');
        elif ch == ']':
          fileOut.write('r');
        elif ch == '{':
          fileOut.write('s');
        elif ch == '=':
          fileOut.write('t');
        elif ch == '[':
          fileOut.write('y');
        else:
          fileOut.write(ch);
  fileOut.close() # close writing file

def encode(fIn, fOut): # defining encode function
  with open(fIn, "r") as fileIn:
    fileOut = open(fOut, "w") # assigning fileOut as writing file
    for line in fileIn: # for each line in read file...
      for ch in line: # for each character in each line...
        # replace 'true' characters with encoded counterparts
        if ch == 'A':
          fileOut.write('!');
        elif ch == 'E':
          fileOut.write('@');
        elif ch == 'I':
          fileOut.write('#');
        elif ch == 'O':
          fileOut.write('$');
        elif ch == 'U':
          fileOut.write('%');
        elif ch == 'a':
          fileOut.write('^');
        elif ch == 'e':
          fileOut.write('&');
        elif ch == 'i':
          fileOut.write('*');
        elif ch == 'o':
          fileOut.write('(');
        elif ch == 'u':
          fileOut.write(')');
        elif ch == 'S':
          fileOut.write('+');
        elif ch == 'T':
          fileOut.write('-');
        elif ch == 'd':
          fileOut.write('>');
        elif ch == 'h':
          fileOut.write(';');
        elif ch == 'k':
          fileOut.write('<');
        elif ch == 'n':
          fileOut.write(':');
        elif ch == 'r':
          fileOut.write(']');
        elif ch == 's':
          fileOut.write('{');
        elif ch == 't':
          fileOut.write('=');
        elif ch == 'y':
          fileOut.write('[');
        else:
          fileOut.write(ch);
  fileOut.close() #close writing file

read_file = input("Name of file to read? ")
writefile = input("Name of file to write? ")
answer = input("Would you like to encode or decode your file? ")
while answer not in ["decode", "encode"]: # loop validation for function call
  answer = input("Would you like to encode or decode your file? ")
if answer == "encode": # calling for encode function
  encode(read_file, writefile);
else: # calling for decode function
  decode(read_file, writefile);