


def game():
    import random


    player = input("请输入你要出的：")
    computer = random.choice(("石头", "剪刀", "布"))

    if player != computer:
        if player == "剪刀":
            if computer == "布":
                print("电脑出的是%s" % computer)
                print("玩家赢")
            else:
                print("电脑出的是%s" % computer)
                print("电脑赢")
        if player == "布":
            if computer == "石头":
                print("电脑出的是%s" % computer)
                print("玩家赢")
            else:
                print("电脑出的是%s" % computer)
                print("电脑赢")
    else:
        print("你和电脑出的一样，请重新出一个")
        game()

