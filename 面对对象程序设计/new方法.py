class Musicplayer:

    instance = None
    flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            print("程序初始化")
        return cls.instance

    def __init__(self):
        if self.flag:
            return
        print("程序运行了")
        self.flag = True



play1 = Musicplayer()
print(play1)
play2 = Musicplayer()
print(play2)

