# 第一题
print("Hello", 123, True)
# 第二题
print(int(12.3))
print(int(12.99))
# 第三题
print(True or False)
# 第四题: 除法运算的结果一定是float型
print(12 / 6)  # 2.0
print(10 / 6)  # 1.6666666666666667
# 报错
# print(10 / 0)
# 银行系统
money = 111_0010_10101_0000
print(money)
print(money * 3)
# *
print("jack" * 3)
# 报错
# print("jack" / 3)
# +
# 报错
# print("jack" + 1)
# 报错
# print("jack" + 1.0)
# 报错
# print("jack" + True)
print("jack" + " lucy")
# 位运算符
a = 10
b = 6
# Python中是没有++和--的运算符的
# print(++a)
# 三目运算符  条件表达式 ?  a:b
# 报错: Python中没有三目运算符
# print(a >= b ? "大于等于":"小于")

# 练习1
c = 10
# c = c + 2
c += 2
print(c)
# 练习2
a = 10
b = 6
if a >= b:
    print("大于等于")
else:
    print("小于")
# 练习3
print(1 + 10 / 2 - 5.5 * 2 // 3)
"""
    1 + 10/2 - 5.5 * 2 // 3
    1 + 5.0 - 11.0 // 3
    1 + 5.0 - 3
    3.0
"""
print((1 + 10 / 2) - 5.5 * (2 // 3))
