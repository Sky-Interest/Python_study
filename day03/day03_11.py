"""
    练习:if-elif-else
    作者 : Sky_Interest
    简介:
"""
age = input("年龄")
age = int(age)
# if-elif-else
if age < 18:
    print("未成年")
    print("滚")
elif age < 30:
    print("青年")
elif age < 50:
    print("中年")
elif age < 70:
    print("老年")
else:
    print("晚年")