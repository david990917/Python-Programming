# -*- coding: cp936 -*-
from Tkinter import *

def prepare(s):
    for ch in ",.":
        s.replace(ch," ")
    return s

def drawBar(c,k,t,aHi,aLo,bHi,bLo):
    a = aHi + aLo            # ĳָ��a�ࣺ������͵���������
    b = bHi + bLo            # ĳָ��b�ࣺ������͵���������
    n = a + b                # ĳָ��������
    x0 = 20+(k-1)*60         # ĳָ��a��������������Ͻ�x
    y0 = 200-aHi*200/n       # ĳָ��a��������������Ͻ�y
    x1 = x0+20               # ĳָ��a��������������½�x
    y1 = 200                 # ĳָ��a��������������½�y
    c.create_rectangle(x0,y0,x1,y1,fill='red')    # ĳָ��a���������
    y2 = y0-aLo*200/n        # ĳָ��a��������������Ͻ�y
    y3 = y0                  # ĳָ��a��������������½�y
    c.create_rectangle(x0,y2,x1,y3,fill='green')  # ĳָ��a���������
    
    u0 = x1                  # ����,ĳָ��b��ĸ��������͵�������
    v0 = 200-bHi*200/n
    u1 = u0+20
    v1 = 200
    c.create_rectangle(u0,v0,u1,v1,fill='red')
    v2 = v0-bLo*200/n
    v3 = v0
    c.create_rectangle(u0,v2,u1,v3,fill='green')    

    c.create_text(x0+4,204,text=t[0],anchor=NW)   # ĳָ��a���ǩ
    c.create_text(u0+4,204,text=t[1],anchor=NW)   # ĳָ��b���ǩ
    
    pct1 = unicode("%d%%" % (100*aLo/a),'gbk')    # ĳָ��a�������ռ��
    c.create_text(x0+4,y2,text=pct1,anchor=NW)
    pct2 = unicode("%d%%" % (100*bLo/b),'gbk')    # ĳָ��b�������ռ��
    c.create_text(u0+4,v2,text=pct2,anchor=NW)
    
def main():
    f = open("data.txt","r")      # ������������ļ�data.txt��ͬһ�ļ�����
    dHi,dLo,ndHi,ndLo = 0,0,0,0   # degree vs nodegree
    wHi,wLo,cHi,cLo = 0,0,0,0     # white vs colored
    mHi,mLo,fHi,fLo = 0,0,0,0     # male vs female
    s = f.readline()
    while s != "":
        s = prepare(s)
        w = s.split()        
        if "Bac" in w[3] or "Mas" in w[3] or "Doc" in w[3]:
            if ">" in w[14]:
                dHi = dHi + 1     # ��ѧλ������
            else:
                dLo = dLo + 1     # ��ѧλ������
        else:
            if ">" in w[14]:
                ndHi = ndHi + 1   # ��ѧλ������
            else:
                ndLo = ndLo + 1   # ��ѧλ������

        if "White" in w[8]:
            if ">" in w[14]:
                wHi = wHi + 1     # ���˸�����
            else:
                wLo = wLo + 1     # ���˵�����
        else:
            if ">" in w[14]:
                cHi = cHi + 1     # ��ɫ�˸�����
            else:
                cLo = cLo + 1     # ��ɫ�˵�����
                
        if "Male" in w[9]:
            if ">" in w[14]:
                mHi = mHi + 1     # ���Ը�����
            else:
                mLo = mLo + 1     # ���Ե�����
        else:
            if ">" in w[14]:
                fHi = fHi + 1     # Ů�Ը�����
            else:
                fLo = fLo + 1     # Ů�Ե�����
        
        s = f.readline()

    r = Tk()
    c = Canvas(r,width=200,height=260,bg="white")
    c.pack()
    td=[unicode("��\nѧ\nλ","gbk"),unicode("��\nѧ\nλ","gbk")]
    ts=[unicode("��\n��","gbk"),unicode("��\nɫ\n��","gbk")]
    tg=[unicode("��\n��","gbk"),unicode("Ů\n��","gbk")]
    drawBar(c,1,td,dHi,dLo,ndHi,ndLo)
    drawBar(c,2,ts,wHi,wLo,cHi,cLo)
    drawBar(c,3,tg,mHi,mLo,fHi,fLo)

    r.mainloop()

main()
