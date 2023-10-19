"""
    复习前面所学的所有    作者: Jack
    日期: 23.9.7的知识

"""
# 变量
a = 10
b = 20
c, d = 30, 40
# 输出
print(a)
print(d)
# 多个变量的输出
print(a, b, c, d)
# 常量
PI = 3.1315
print(PI)
PI = 4
print(PI)
# 定义一个半径的变量和PI的常量，计算圆形的面积？
r = 4
PI = 3.1415
area = PI * r ** 2
print("半径是:",r,"圆形的面积是:",area)
# 数据类型
name = "李莲花"
age = 31
salary = 50000.99
isMarray = False
print(type(name),type(age),type(salary),type(isMarray))
# 数据类型转换: int()、float()、str()、bool()
string  = "123"
print(type(string))
# 注意: 字符串的+法运算之能和字符串自己使用
print(string + "345")
# 注意: 报错
# print(string + 345)
# 拼接n次进行输出
print(string * 3)
# 468
print(int(string) + 345)
# 注意: 转换函数中最重要的是bool()
print(bool(0),bool(0.0),bool(""),bool(None),bool(()),bool([]),bool({}))
print(bool(10),bool(2.0),bool(" "),bool((1)),bool([2,3]),bool({"jack"}))
# 运算符


