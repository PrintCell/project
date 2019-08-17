def cut_paper():
    str_1 = "我喜欢你\t \n 有机会吗 有机？ 有机不会"
    new_list = str_1.split()
    print(new_list)
    str_2 = ""
    for son_list1 in new_list:
        str_2 += son_list1
    print(str_2)
    print(str_2.count("有机"))
cut_paper()