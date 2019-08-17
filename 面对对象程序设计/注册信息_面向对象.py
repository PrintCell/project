class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s现在的体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美", 50)
xiaomei.run()
xiaomei.eat()
print(xiaomei)