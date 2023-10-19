"""
    练习:
    作者 : Sky_Interest
    简介:
"""
# 输入信息
name = input("姓名")
cn = input("语文")
mt = input("数学")
en = input("英语")

# 类型转换
cn = float(cn)
mt = float(mt)
en = float(en)

# 格式化
print("姓名 %s 语文 %.1f 数学 %.1f 英语 %.1f 总分 %.1f 平均分 %.2f" % (
    name, cn, mt, en, (cn + mt + en), ((cn + mt + en) / 3)))

print(f"姓名 {name} 语文 {cn} 数学 {mt} 英语 {en} 总分 {cn+mt+en} 平均分 {(cn+mt+en)/3}")
