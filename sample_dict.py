
#Dicts can be represented like this
#stuff = {'name': 'kenneth', 'age': 38, 'gender': 'male'}

#Dics can also be represented like this
stuff = {
    'name': 'kenneth',
    'age': 38,
    'gender': 'male'
}
#output {'name': 'kenneth', 'age': 38, 'gender': 'male'}
#print(stuff)



for key,value in stuff.items():
    print("{} {}".format(key,value))

#output male
print(stuff['gender'])

#delete the dictionary item, gender
del stuff['gender']
print(stuff)

#del is similar to pop, will remove item age but will return it first

value = stuff.pop('age')

#output 38
print(value)

#output {'name': 'kenneth'}
print (stuff)
