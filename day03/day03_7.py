"""
    练习:输入与输出
    作者 : Sky_Interest
    简介:
"""
# 输出
print("姓名")

# 输入
name =  input()

# 简化版
age = input("年龄")

money = input("工资")
print(f"{name} , {age} , {money}")

# 查看输出类型(str型)
print(f"{type(name)},{type(age)},{type(money)})")

# 类型转换
age = int(age)
money = float(money)

# 查看转化后类型
print(f"{type(name)},{type(age)},{type(money)})")

