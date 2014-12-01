#! /usr/bin/env python

class Grammanalyzer():
  def __init__(self):
    self.encoding = []
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
  
  def test_print(self):
    print self.encoding

def main():
  an = Grammanalyzer()
  print "loading file"
  an.load_file("templates/3.txt")
  an.test_print()

main()
