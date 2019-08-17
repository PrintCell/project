s1 = 0
i1 = 0
while i1 <= 100:
    s1 += i1
    i1 += 1
print("从1加到100之和为：%d"%s1)


s = 0
for i in range(1,101):
    if i % 2 == 0:
        s += i
print("利用for循环加和的结果为%d"%s)