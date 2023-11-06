# Simple example of parsing
# Bartosz Sawicki, 2014-03-13

from scanner import *
from myParser import *
from preprocesor import *


f = open('cir30.net', "r")
input_string = f.read()


print (input_string)



preproc = preprocesor(input_string)
input_string = preproc.conv
print (input_string)
scanner = Scanner(input_string)
#print (scanner.tokens)

parser = myParser(scanner)
parser.start()

f.close()
  
