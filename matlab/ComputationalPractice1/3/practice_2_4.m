A1=[9 -36 30;-36 192 -180;30 -180 180];   %��Ҫ�ļ�cholesky.m
A2=hilb(6);
L1=cholesky(A1);
L2=cholesky(A2);
[L1 chol(A1)]                             %������, �ں���ת�õ�������Զ��庯��cholesky()��õĽ�������ú���chol()��õĽ����ͬ
[L2 chol(A2)]
chol(A2)