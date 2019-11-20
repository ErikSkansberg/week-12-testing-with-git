#testing things in py 
def PrintOutput(string):
  print("OUTPUT "+str(string))
def LoadFile(filename):
    Fin = open(filename,'r')
    Line = []
    for line in Fin:
        Line.append(''.join(line))
    print(Line)