courses=['science', 'art', 'history', 'math']
addMore = ['physics', 'sociology']
#Print the courses list
#output ['science', 'art', 'history', 'math']
print(courses)

#This will add additional list items to end of list
courses.extend(addMore)
print(courses)

#Print the courses list sorted
#ouput ['art', 'history', 'math', 'science']
sorted_courses = sorted(courses)
print(sorted_courses)

#Print the index location of art in the list
#output 1
print(courses.index('art'))

#Evaluate if there is a fart in the list
#output the else statement
if 'fart' in courses:
    print("Found fart in course list")
else:
    print("Couldn't find fart in course list")


#Print every item in the list
for item in courses:
    print(item)
