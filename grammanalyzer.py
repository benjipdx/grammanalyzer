#! /usr/bin/env python

class StringStack():
  string = ""
  def push(self, string):
    self.string+=string
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
 
  def get_buff(self):
    try:
      nextchar = self.buffer[0]
      self.buffer = self.buffer[1:] #remove first charA
      return nextchar
    except IndexError:
      return None

  def get_rule(self, terminal):
    """takes terminal as input and finds matching rule for it"""
    #self.encoding is a list of lists
    for i in self.encoding:
      #['S','aSa','#']
      #i is a list of each line of file
      #need to find the right rule
      for j in i:
        if(j[0] == terminal):
          return j
        else:
          return None

  def sim(self):
    """simulate stuffs"""

    #    To parse a string you will need to maintain a stack and an input buffer. Begin by pushing the
    #    start variable onto the stack. Then repeat the following until you empty the input buffer.

    done = False
    while(not done):
      buffchar = self.get_buff()
      popped = self.stack.pop()
      #    1. Pop an element from the stack.

      if(not popped and buffchar):
        #no more stack buf still have buffchars
        #    4. If the stack is empty and the input buffer is not, reject the string.
        done = True
        return 1 #reject

      elif(not popped and not buffchar):
        done = True
        return 0
      #    5. If both the stack and the input buffer are empty, accept the string.

      if(popped.islower() == False):
      #    2. If the popped element is a variable, look at the next character in the input and use that to
      #    determine which rule to apply. Then push the right hand side of that rule onto the stack. If
      #    no rule matches the next input reject the string.
        next = self.stack.peek()
        rule = get_rule(next) #get next rule
        if(not rule):
          #no rule matches
          done = True
          return 1 #one for reject
        else:
          #found a rule
          self.stack.push(rule)

      elif(popped.islower() == True):
      #    3. If the popped element is a terminal, make sure it matches the next character in the input and
      #    remove both. If it does not match reject the string.
        if(popped == buffchar):
          #remove both
          #already popped, just need to remove buffchar, but it is as well
          continue
        
        elif(popped != buffchar):
          done = True
          return 1 #reject string


def main():
  an = Grammanalyzer()
  an.load_file("templates/1.txt")
  an.tp()
  input="aa#bb"
  an.input_test_string(input)
  returned = an.sim()
  if(returned == 0):
    print("String %s in Grammar" % input)
  else:
    print("String %s is NOT in Grammar" % input)
  

main()
