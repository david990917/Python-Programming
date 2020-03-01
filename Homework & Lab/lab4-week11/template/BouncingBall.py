# -*- coding: cp936 -*-

# ����:Ƥ��Ӹߴ���ص���.
# �����ٶ�ʸ������Ϊ��,����Ϊ��
# ����¸߶� = ��ľɸ߶� - ����* ʱ����
# ������ٶ� = ��ľ��ٶ� + 9.8 * ʱ����
# ��ط���:if �߶� < Ƥ��뾶:                                    
#            �ٶ�ȡ��

from Tkinter import *
from time import sleep

def main():
    r = Tk()
    c = Canvas(r,width=80,height=420,bg='white')
    c.pack()

    c.create_rectangle(0,410,79,419,fill='brown')   # ����
#   c.create_line(0,10,79,10)                       # �������
    ball = c.create_oval(20,10,59,49,fill='red')

    h0 = 380                      # ��ʼ�߶� = 410 - 10 - 20
    v0 = 0.0                      # ��ʼ�ٶ�
    dt = 0.05                     # ʱ����ɢ���ļ����ԽС�˶�Խ��ȷ��������Խ��

    while True:
        h1 = h0 - v0 * dt         # dt����¸߶�
        v1 = v0 + 9.8 * dt        # dt������ٶ�

        if h1 < 20:               # ��ĸ߶�С����뾶
            h1 = 20               # �򴥵�
            v1 = -1.0 * v1        # �ٶȱ���

        if h1 > 380:              # ��ĸ߶ȴ��ڳ�ʼ�߶�
            h1 = 380              # �򴥶�
            v1 = 0.0              # �ٶ�Ҳ�ָ�Ϊ��ʼֵ0

        c.move(ball,0,h0-h1)      # �˶����¸߶�
        c.update()                # ˢ�»���
        
        h0 = h1
        v0 = v1

        sleep(0.02)

main()
