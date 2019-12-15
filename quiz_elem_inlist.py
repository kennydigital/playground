def checkIfMatch(elem):
    if len(elem) == 7:
        return True;
    else:
        return False;

def main():

    #Given a list
    listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'b', 'test', 'Ok']

    #elem in list
    #We learn about using 'in' and 'not in'
    if 'Hello' in listOfElems:
        print ("Yes we could find 'hello' in list", listOfElems)

    if 'time' not in listOfElems:
        print ("Yes we could not find 'time' in list", listOfElems)

    #We learn that 'count' helps us find how many elems found in given list
    #This would list 3, since it finds OK 3 times
    howMany = listOfElems.count('Ok')
    print(howMany)





    result = any(len(elem) == 5 for elem in listOfElems)
    if result:
        print("Yes, string element with size 5 found")


    result2 = any(checkIfMatch for elem in listOfElems)

    if result2:
        print("Yes, string element with size 5 found")

if __name__ == '__main__':
    main()
