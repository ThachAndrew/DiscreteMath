#prints logical truth tables
#input format example: p q * r t * = 
#possible improvements: allow for bigger proposition names
from sys import stdin
import re
import itertools

#create stack
input = stdin.read().split()

#filter out operators from stack
operators = {"+","=","->","<=","*","!","~","False","True"} 
propositions = set(input) - (operators)

#Another way to filter out operators
#Filter out operators, and put in separate set
#propositions = set()
#for token in input:
#  if not (re.search(r"[+=-><=*~!]+", token)):
#    propositions.add(token);  

#print first line in table: declared propositions y expression 
for variable in sorted(propositions):
  print ('%-7s' % variable, end = '')
print (*input)

#print results of expression
for row in itertools.product((False, True), repeat = len(propositions)):
  for booleanValue in row: 
    print('%-7s' % booleanValue, end = '')
  #perform calculation here
  truthTableRow = dict(zip(sorted(propositions), row))
  buffer = list() #create stack
  for token in input:
    if (token == "True"):
      buffer.append(True)
    elif(token == "False"):
      buffer.append(False)
    elif token not in operators: #push truth value of proposition
      buffer.append(truthTableRow[token])
    else:
      if (token == "="): #test for equality
        x = buffer.pop()
        y = buffer.pop()
        buffer.append(x == y)
      elif (token == "+"):  #test for or
        x = buffer.pop()
        y = buffer.pop()
        buffer.append(x or y)
      elif (token == "*"):  #test for and
        x = buffer.pop()
        y = buffer.pop()
        buffer.append(x and y)
      elif (token == "->" or token == "<="):  #test for implication
        y = buffer.pop()
        x = buffer.pop()
        buffer.append((not x) or y)
      elif (token == "~" or token == "!"):  #test for not
        x = buffer.pop()
        buffer.append(not x)

  print(buffer.pop()) #print result
    
  
  


  #print('')  #patch: prints newline for some reason


#print("Printing Pop: ")
#print(input.pop())

#####DEBUG#####
#for row in itertools.product((False, True), repeat = len(propositions)):
#  print(row)
#####DEBUG#####
#print("Propositions are: \n")
#print(propositions)

