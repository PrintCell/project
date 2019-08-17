
def add_num(num):
    if num == 1:
        return 1
    else:
        temp = add_num(num - 1)
        return num + temp


print(add_num(100))
