#Example showing how we will use setter, deleter

#Class defined
class Employee:

    #Constructor, with two variables
    def __init__(self, first, last):
        self.first=first
        self.last=last
    #    self.email= first + '.' + last + '@email.com'


    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    @fullname.setter
    def fullname(self, name):
        #Will split the input separated by space into first = ?? and last = ??
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


    # The @property, will allow email like a method but accessible like attribute
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)



#Based on this input
emp_1 = Employee("Kenneth", "Cornelius")
emp_1.first="Melanie"
emp_1.fullname="Jackson Cornelius"





#See output below
print(emp_1.first)
print(emp_1.last)

# I can call it like an attribute when applying the @property. if you pull this
# off then would have to call this emp1.email()
print(emp_1.email)

#i can call my fullname function like an attribute due to @property
print(emp_1.fullname)

#Sample of calling deleter method
del emp_1.fullname





#Output
#Jackson
#Cornelius
#Jackson Cornelius@email.com
#Jackson Cornelius
