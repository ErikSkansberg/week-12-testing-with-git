#testing things in py 
def PrintOutput(string):
  print("OUTPUT "+str(string))
def LoadFile(filename):
    Fin = open(filename,'r')
    Line = []
    for line in Fin:
        Line.append(''.join(line))
    Fin.close()
    PrintOutput(Line)
def UpdateString(str1,str2,num):
    word1 = list(str1)
    word1[num] = str2
    print("".join(word1))
def FindWordCount(looking,fin):
    count = 0

    with open((file), 'r') as file:
        for row in file:
            for word in row.split():
                if word == n:
                    count = count + 1
    return PrintOutput(count)
def ScoreFinder(a,b,c):
    count = 0
    C = c
    A = [x.upper() for x in a]
    c = c.upper()
    for i in A:
        if i == c:
            print("OUTPUT", C, "scored", b[A.index(c)])
            count = 1

    if count == 0:
        print("OUTPUT Could not find Player")
def Union(a,b):
    list = []
    total = a + b
    for i in total:
        if i not in list:
            list.append(i)
    return PrintOutput(list)
def Intersection(a,b):
    List = []
    c = a + b
    d = [c[i] for i in range(len(c)) if c[i] in c[:i]]

    for i in d:
        if i not in C:
            C.append(i)
    C.reverse()
    
    return PrintOutput(C)
def NotIn(a,b):
    mylist = []
    for i in a:
        if i not in b:
            mylist.append(i)
    return PrintOutput(mylist)

