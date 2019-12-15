#Remember tuple ()  is similar to list []
#But you cannot change the length or substitue elements

#Example Lists
#list of elements with same type
listOfElems1=['1', '2', '3']
print(listOfElems1)

#list of elements with different type
listOfElems2=['1', 2, '3', 'cat']
print(listOfElems2)

#['1', '2', '3', ['1', 2, '3', 'cat']]
listOfElems1.append(listOfElems2)
print(listOfElems1)

#['1', '2', '3', ['1', 2, '3', 'cat'], '1', 2, '3', 'cat']
listOfElems1.extend(listOfElems2)
print(listOfElems1)

language = ['P', 'y', 't', 'h', 'o', 'n']
print(language[:1])


#Examples with tuples
tupleOfElems=(1,2,3)
print(tupleOfElems)

#Packing a tuple
#(3, 4.6, 'dog')
my_tuple = 3, 4.6, "dog"
print(my_tuple)

#Unpacking a tuple, must match same amount of variables or will fial
a, b, c = my_tuple
print(b)
