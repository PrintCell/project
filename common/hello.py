import turtle as t
import random as r


def sj1():  # 随机出五角星的大小及五角星的位置，大小设为(10,30),随机多边形的边数
    x = r.randint(-400, 350)
    y = r.randint(50, 250)
    star = r.randint(10, 20)
    bi = r.randint(3, 6)
    return x, y, star, bi


def sj2():  # 随机出所画图的的颜色
    a = r.random()
    b = r.random()
    c = r.random()
    return a, b, c


def drawstar():  # 画五角星的函数
    # for i in range(15):
    x, y, z, bi = sj1()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color((sj2()))
    t.begin_fill()
    for s in range(5):
        t.fd(z)
        t.right(144)
    t.end_fill()


def draw520():  # 写吐槽字的函数
    s = '这平台有bug啊！！！这真的不是代码的错！'
    for i in range(len(s)):
        a, b, c = sj2()
        e = s[i]
        t.color((a, b, c))
        t.penup()
        t.goto(-400 + 40 * i, -150)
        t.pendown()
        t.write(e, font=('times', 30, 'bold'))


def drawsanjiao():
    x, y, z, bi = sj1()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color((sj2()))
    t.begin_fill()
    if bi == 3:
        t.circle(z, steps=3)
    elif bi == 4:
        t.circle(z, steps=4)
    elif bi == 5:
        t.circle(z, steps=5)
    else:
        t.circle(z, steps=6)
    t.end_fill()


t.speed(0)
t.setup(1000, 600)
sj1()
sj2()
t.bgcolor((1, 1, 1))
for i in range(15):
    a = r.randint(1, 2)
    if a == 1:
        drawstar()
    else:
        drawsanjiao()
draw520()
t.hideturtle()
t.done()
