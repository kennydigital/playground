#Given a list
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
#                  0       1    2     3       4      5       6    7     8      9
#Write a program that will find 'Ok' in indexes 1, 3, 9 in a given list


#TIP #1
print ('Length of list ', len(listOfElems))
#n=5
#while n >= 0 :
#  print(listOfElems[n])
#  n = n-1

#TIP #2 index(elem,start,end)
#       elem - searching for
#       start - if given, start searchign from this index
#       end - if given, stop searching from this index
#
#print(listOfElems.index("Hello",0))



def getIndexPositions(listOfElems, elem):
    listOfPos=[]
    indexPos=0

    while True:
        try:
            indexPos =listOfElems.index(elem,indexPos)
            listOfPos.append(indexPos)
            indexPos= indexPos + 1
        except ValueError as e:
            break
    return listOfPos

print('Index of ok', getIndexPositions(listOfElems, 'Ok'))
