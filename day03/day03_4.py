"""
    格式化输出
    作者 : Sky_Interest
    简介:
"""
name = "足球"
pr = 114.514
count = 19
sum_pr = pr * count
# 格式化输出
print("%s %s %f %f " % (name, pr, count, sum_pr))

# 精度控制
print("%s %1.f %d %6.3f" % (name, pr, count, sum_pr))

# 指定宽度比实际数据小,则恢复原数
print("%s %1.2f %d %1.2f" % (name, pr, count, sum_pr))
