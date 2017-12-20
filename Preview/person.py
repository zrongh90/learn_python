class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    
    def lastName(self):
        return self.name.split(' ')[-1]

    def giveRaise(self, my_raise):
        self.pay *= (1 + my_raise)

    def __str__(self):
        return "{} => \n name:{} age:{} pay:{} job:{}".format(self.__class__.__name__, self.name, self.age, self.pay, self.job)

if __name__ == '__main__':
     bob = Person('Bob Smith', 42, 30000, 'software')
     sue = Person('Sue Jones', 45, 40000, 'hardware')
     print(bob.name, sue.pay)
     print(bob.lastName())
     sue.giveRaise(0.1)
     print(sue.pay)

