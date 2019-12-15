#Sample OUTPUT
#Your list contains:  ['Snart', 'Math', 'Labs']
#Element not found in list. Error msg :  'Art' is not in list
#0 Snart
#1 Math
#2 Labs


#Let's create a simple list
courses = ['Snart', 'Math', 'Labs']


#Let's print out the list
#Note: Here's a quick way of using print while passing (string, variable) for print
#statement
print('Your list contains: ', courses)

#Let's find 'Art' in the list
#Remember, we put this in a try catch because when value is not found in index
#it will throw ValueError
try:
    courses.index("Art")
    print('Found Art')
except ValueError as e:
    print('Element not found in list. Error msg : ', e)

#Random fun -- print value and index of the list
#Leverage enumerate which returns two
for idx,name in enumerate(courses):
    print (idx,name)
