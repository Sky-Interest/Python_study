"""
    练习:猜随机数
    作者 : Sky_Interest
    简介:
"""
import random
rd = random.randint(1,100)
if int(input("你猜是啥")) == rd:
    print("1对")
elif int(input("你猜是啥")) == rd:
    print("2对")
elif int(input("你猜是啥")) == rd:
    print("3对")
else:
    print(f"废物这都猜不对,这个数是{rd}")