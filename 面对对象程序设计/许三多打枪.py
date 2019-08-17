class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet = 0

    # 每运行一次函数，子弹数更新为30
    def add_bullet(self, count):
        self.bullet += count

    def __str__(self):
        return "型号：%s,剩余子弹：%d" % (self.model, self.bullet)

    def shoot(self):

        print("突突突")
        self.bullet -= 3
        print("%s 剩余%d发子弹" % (self.model, self.bullet))


class Soider:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def __str__(self):
        return "姓名：%s\n武器：%s" % (self.name, self.gun)

        # 三连
    def fire(self):
        if self.gun is None:
            print("我没有枪")
            return

        if gun.bullet == 0:
            print("枪里没有子弹，上子弹先")
            gun.add_bullet(30)
        print("许三多扣了一下扳机")
        gun.shoot()


xusanduo = Soider("许三多")
#xusanduo.gun = "ak_47"
gun = Gun("ak_47")
print(xusanduo)
enemy = 5
while enemy != 0:
    xusanduo.fire()
    enemy -= 1

print(gun)
# 上子弹
# gun.add_bullet(90)
# print(gun)