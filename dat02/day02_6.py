"""
    学习python的“第二天”
    作者: Sky_Interest
    日期: 23.9.7
"""
# 输出
print("哼哼哼啊啊啊啊啊", 114514, False)

# 输出类型转换
a = 11.3
print(type(a))
print(int(a))
print((type(int(a))))
"""
<class 'float'>
11
<class 'int'>
"""

#
print(True or False)

# 除法运算的结果一定是float型
print(40 / 4)
print(41 / 4)

# print(40 / 0)
# 除数一旦为0则报错

# 银行系统(分隔字符)
money = 114514191980
mon_ey = 114_514_1919_80

print(money) # 114514191980
print(mon_ey) # 114514191980

# 字符串相连(相同类型)
print("Sky" * 3)

# 报错
# print("Sky" / 3)
# 报错
# print("Sky" + 1)
# 报错
# print("Sky" + 1.0)
# 报错
# print("Sky" + True)

print("Sky" + " Interest")

# 位运算符
a = 10
b = 6

# Python中是没有++和--的运算符的
# print(++a) a
# 三目运算符  条件表达式 ?  a:b

# 报错: Python中没有三目运算符
# print(a >= b ? "大于等于":"小于")
a1 = 10
b2 = 6
if a1 >= b2:
    print("大于等于")
else:
    print("小于")

# 运算字符优先级
print(2 + 15 / 3 - 7.5 * 2 // 3)
"""
    2 + 15 / 3 - 7.5 * 2 // 3
    2 + 5.0 - 15.0 // 3
    2 + 5.0 - 5.0
    2.0
"""
# print((2 + 15 / 2) - 7.5 * (2 // 3))