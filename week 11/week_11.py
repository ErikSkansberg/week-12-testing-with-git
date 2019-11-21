#testing things in py 
def PrintOutput(string):
  print("OUTPUT "+str(string))
def LoadFile(filename):
    Fin = open(filename,'r')
    Line = []
    for line in Fin:
        Line.append(''.join(line))
    PrintOutput(Line)
def UpdateString(str1,str2,num):
    word1 = list(str1)
    word1[num] = str2
    print(word1)
