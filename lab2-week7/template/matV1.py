# -*- coding: cp936 -*-

# ������Ȼ��n�����������ʽ��n�׷�����n=4Ϊ������
# 1   2   3   4
# 12  0   0   5
# 11  0   0   6
# 10  9   8   7

# ֱ��˼ά�汾����������˳ʱ�뷽�����

n = input("������Ȼ��n��")

# ����һ��ȫ0��n�׷���mat
mat = []
for i in range(n):
    mat = mat + [n*[0]]

# ��mat�ĺ���λ��������Ȼ��
for k in range(4*n-4):                # �ܹ�4n-4��Ԫ��
    if k < n:                         # mat������������
        i = 0                         # i:�к�,j:�к�
        j = k
    elif k >= n and k < 2*n-1:        # mat��������������
        i = k-(n-1)
        j = n-1
    elif k >= 2*n-1 and k < 3*n-2:    # mat������������
        i = n-1
        j = (3*n-3)-k
    else:                             # mat��������������
        i = (4*n-4)-k
        j = 0
    mat[i][j] = k+1                   # ������Ȼ��k+1
        
# ��ʾ
for i in range(n):
    for j in range(n):
        print "%4d" % mat[i][j],
    print
