class Heros:
    def __init__(self, new_hero):
        self.name = new_hero
        print("使用的英雄人物是：%s" % self.name)

    def jineng(self):
        print("%s 快乐起来" % self.name)

    def __del__(self):
        print("啊！%s挂了" % self.name)

    def __str__(self):
        return "%s你个坑货" % self.name


hero_1 = Heros("亚索")
hero_1.jineng()
print(hero_1)
del hero_1
hero_2 = Heros("盖伦")
hero_2.jineng()
print(hero_2)