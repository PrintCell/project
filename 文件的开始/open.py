# 文件打开之后就是创建一个对象，利用面向对象的思想进行操作
# 下面的text_1就是一个对象
text_1 = open("hello.txt", "r", encoding="utf-8")
text_2 = open("world.txt", "w", encoding="utf-8")
while True:
    file = text_1.readline()
    text_2.write(file)
    if len(file) == 0:
        break

text_1.close()
text_2.close()
