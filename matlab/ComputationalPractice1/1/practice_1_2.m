H_6=hilb(6);                 %��Ҫ�ļ� householder_qr.m
[q,r]=householder_qr(H_6);
[q_1,r_1]=qr(H_6);
[q,q_1]          %������,�Զ��庯��householder_qr()�����ú���qr()��õĽ���˷��������
[r,r_1]