try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print("结果是 %s" % result)

except Exception as result:
    print("未知错误 %s" % result)
