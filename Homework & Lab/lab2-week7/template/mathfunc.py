# -*- coding: cp936 -*-

# ����x,�������
#    f(x) = (sin(x)^2+cos(x)+1)^3 - 3(sin(x)^2+cos(x)), x>0
#           4sin(x)^2+4cos(x)-1                         x<0
#           pi                                          x=0
# ��ֵ.

from math import sin,cos,pi

x = input("������x: ")

t = sin(x)**2 + cos(x)    # ��һ��ʹ����������!
if x > 0:
    y = (t+1)**3 - 3*t
elif x < 0:
    y = 4*t - 1
else:
    y = pi
    
print "����ֵf("+str(x)+") =",y
