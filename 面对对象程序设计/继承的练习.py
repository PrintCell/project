class Person:
    name = "人"
    age = "有大有小"

    @staticmethod
    def eat():
        print("人要词东西")


class Man(Person):
    sexy = "男的"

    @staticmethod
    def toliet1():
        print("男生要去男厕所")


class Woman(Person):
    sexy = "女的"

    @staticmethod
    def toliet2():
        print("女生要去女厕所")


xiaoming = Man()
xiaomei = Woman()

print(xiaoming.sexy)
print(xiaoming.name)
print(xiaoming.age)
print(xiaoming.toliet1())

print(xiaomei.sexy)
print(xiaomei.age)
print(xiaomei.name)
print(xiaomei.eat())