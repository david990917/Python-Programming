# -*- coding: cp936 -*-

# ������Ȼ��n�����������ʽ��n�׷�����n=4Ϊ������
# 1   2   3   4
# 12  0   0   5
# 11  0   0   6
# 10  9   8   7

# ��ͨ˼ά�汾���������

n = input("������Ȼ��n��")

# ����һ��ȫ0��n�׷���
mat = []
for i in range(n):
    mat = mat + [n*[0]]

# ��һ��mat[0]�ĸ�Ԫ��
for i in range(n):
    mat[0][i] = i+1

# ���¸���mat[j]����βԪ��ֵ
for j in range(1,n):
    if j == 1:
        mat[j][0] = 4*(n-1)           # �ڶ�����Ԫ����4(n-1)
    else:
        mat[j][0] = mat[j-1][0] - 1   # ����������Ԫ������һ����Ԫ��-1
    mat[j][n-1] = mat[j-1][n-1] + 1   # ����βԪ������һ��βԪ��+1

# ���һ�з���βԪ��
for k in range(1,n-1):
    mat[n-1][k] = mat[n-1][k-1] - 1

# ��ʾ
for i in range(n):
    for j in range(n):
        print "%4d" % mat[i][j],
    print


