"""
    练习:字符串比较1
    作者 : Sky_Interest
    简介:
"""
m = input("月份")
m = int(m)
if m == 12 or m == 1 or m == 2:
    print("冬季")
elif m == 3 or m == 4 or m == 5:
    print("春季")
elif m == 6 or m == 7 or m == 8:
    print("夏季")
elif m == 9 or m == 10 or m == 11:
    print("秋季")
else:
    print("输入错误")