def cl():
    # nm = int(input("整数："))
    # while nm != 1:
    #     if nm % 2 == 0:
    #         nm = nm/2
    #     else:
    #         nm = 3 * nm + 1
    #     print(nm)
    try:
        nm = int(input("整数："))
        while nm != 1:
            if nm % 2 == 0:
                nm = nm/2
            else:
                nm = 3 * nm + 1
            print(nm)
    except ValueError:
        print("请输入一个整数！")
        cl()

cl()