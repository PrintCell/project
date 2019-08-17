has_ticket = True
knife_length = 30
if has_ticket is True :
    print("可以进入车站进行安检")
    if knife_length <= 20:
        print("安检通过，允许进入车站")
    else:
        print("安检不通过，你的刀有%d"%knife_length)
else:
    print("没票不允许进入车站")