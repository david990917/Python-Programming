# -*- coding: cp936 -*-

# 输入一个四位整数,对其加密后输出
# 加密方法:每位数字分别加9后除以10取余数,从而得到四位新数字
# 然后将千位和十位数字互换,百位和个位数字互换.
# 例如:2017经加密变成0619.
# 注意:若加密后整数的最高位为0,也要求输出.

# 以字符串形式输入四位数，取各位数字比较方便
a = raw_input("请输入一个四位数：")

a0 = (eval(a[0])+9)%10
a1 = (eval(a[1])+9)%10
a2 = (eval(a[2])+9)%10
a3 = (eval(a[3])+9)%10

# 字符串拼接,避免各位数字间有空格,首位为0也不会丢弃
s = str(a2)+str(a3)+str(a0)+str(a1)

print "加密结果是：",s
