# -*- coding: cp936 -*-

# 水果价格查询：
# 有4种水果，单价分别是3.00、2.50、4.10、10.20元/千克
# 首先在屏幕上显示如下菜单：
# [1] 苹果
# [2] 梨
# [3] 橘子
# [4] 葡萄
# [0] 退出
# 请输入序号：
# 然后用户输入序号查询水果价格。
# 每次运行程序可以连续查询4次，即程序输出用户所选水果的单价后自动回到菜单让用户继续查询
# 当用户用完4次查询机会就自动退出结束运行。
# 但是，任何时候用户都可选择0来主动退出。

# 水果价格会变动，所以应当用变量（以便通过input获得），而不是固化在后面的print中
apple = 3.0
pear = 2.5
orange = 4.1
grape = 10.2

n = 0
while n < 4:
    print "[1] 苹果"
    print "[2] 梨"
    print "[3] 橘子"
    print "[4] 葡萄"
    print "[0] 退出"
    i = input("请输入序号：")
    if i == 1:
        print "苹果单价为%0.2f元/千克" % apple
    elif i == 2:
        print "梨单价为%0.2f元/千克" % pear
    elif i == 3:
        print "橘子单价为%0.2f元/千克" % orange
    elif i == 4:
        print "葡萄单价为%0.2f元/千克" % grape
    elif i == 0:
        break
    else:
        print "只能输入0-4！"
    n = n + 1
    print
print "Bye."
    
    
