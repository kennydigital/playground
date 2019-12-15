#Example, we establish two objects, add them to a list and iterate through the object using for loop

#Class defined
class Employee:

    #Constructor, with two variables
    def __init__(self, name, age):
        self.name=name
        self.age=age


list = []

sum = 0
emp_1 = Employee("Zebra", 1)
emp_2 = Employee("Kenneth", 10)
emp_3 = Employee("Melanie", 15)

list.append(emp_1)
list.append(emp_2)
list.append(emp_3)



#output
#Zebra
#Kenneth
#Melanie
for obj in list:
    print(obj.name)

#Output
#26
for obj in list:
    sum = obj.age + sum

print(sum)
