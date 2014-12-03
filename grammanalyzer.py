#! /usr/bin/env python
import sys

class StringStack():
  string = ""
  def push(self, char):
    if(len(char) > 0):
      length = len(char)
      for i in xrange(length):
        self.string+=char[(length-1)-i]
    else:
      self.string+=char
    return

  def pop(self):
    try:
      temp = self.string[-1]
      self.string = self.string[:-1]#remove last element, top of stack
      return temp
    except IndexError:
      return None

  def peek(self):
    try:
      return self.string[-1]
    except IndexError:
      return None

class Grammanalyzer():
  def __init__(self):
    self.encoding = []
    self.stack = StringStack()
    self.buffer = ""
    return

  def load_file(self, filename):
    #no error checking, if you hand me a invalid file, program blows up
    file = open(filename,'rt')
    contents = file.read()
    contents = contents.rstrip('\n').split('\n')
    for i in contents:
      #each i is the string of the whole line withot newlines
      line = i.split('->') #now we have separated by -> ['S','aSa|#']
      rules = line[1].split('|') #now we have rules ['aSa','#']
      final_line = [line[0]]+rules
      self.encoding+=[final_line]

  def tp(self): #testprint function
    print self.encoding
    print self.buffer

  def input_test_string(self, teststring):
    self.buffer = teststring
 
  def pop_buff(self):
    try:
      nextchar = self.buffer[0]
      self.buffer = self.buffer[1:] #remove first charA
      return nextchar
    except IndexError:
      return None

  def peek_buff(self):
    try:
      nextchar = self.buffer[0]
      return nextchar
    except IndexError:
      return None

  def get_rule(self, character):
    """takes terminal as input and finds matching rule for it"""
    #self.encoding is a list of lists
    for i in self.encoding:
      #['S','aSa','#']
      #i is a list of each line of file
      #need to find the right rule
      result = None
      for j in i:
        #print(j,i)
        if(j[0] == character):
          result = j
          return result
      return result #catching case if we dont find anything


  def sim(self):
    """simulate stuffs"""

    #    To parse a string you will need to maintain a stack and an input buffer. Begin by pushing the
    #    TODO start variable onto the stack. Then repeat the following until you empty the input buffer.

    #push start variable onto stack
    self.stack.push(self.encoding[0][0]) 

    done = False
    while(not done):
      #run the simulator

      print("before", self.buffer, self.stack.string)
      #import pdb;pdb.set_trace()

      buffpeek = self.peek_buff()
      stackpeek = self.stack.peek() #not getting anything, getting none

      print("after", self.buffer,buffpeek,stackpeek,self.stack.string)

      #    1. Pop an element from the stack.

      if(not stackpeek and buffpeek):
        print "1"
        #no more stack buf still have buffpeeks
        #    4. If the stack is empty and the input buffer is not, reject the string.
        done = True
        return 1 #reject

      elif(not stackpeek and not buffpeek):
        print "2"
        done = True
        return 0
      #    5. If both the stack and the input buffer are empty, accept the string.

      elif((stackpeek.islower() == False) and stackpeek != '#'):
        print "3"
      #    2. If the stackpeek element is a variable, look at the next character in the input and use that to
      #    determine which rule to apply. Then push the right hand side of that rule onto the stack. If
      #    no rule matches the next input reject the string.
        rule = self.get_rule(buffpeek) #get next rule TODO this is broked
        if(not rule):
          #no rule matches
          done = True
          return 1 #one for reject
        elif(rule[0] == buffpeek):
          #found a rule
          self.stack.pop()
          self.stack.push(rule)

      elif((stackpeek.islower() == True) or stackpeek == "#"):
        print "4"
      #    3. If the stackpeek element is a terminal, make sure it matches the next character in the input and
      #    remove both. If it does not match reject the string.
        if(stackpeek == buffpeek):
          #remove both
          self.stack.pop()
          self.pop_buff()

        elif(stackpeek != buffpeek):
          done = True
          return 1 #reject string


def main():
  #usage: ./grammanalyzer.py templates/3.txt abababa
  an = Grammanalyzer()
  an.load_file(sys.argv[1])
  an.tp()
  input=str(sys.argv[2])
  an.input_test_string(input)
  returned = an.sim()
  if(returned == 0):
    print("String %s in Grammar" % input)
  else:
    print("String %s is NOT in Grammar" % input)
    return 1
  

main()
