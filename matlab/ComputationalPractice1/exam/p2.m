%�����ļ�givens_qr.m������givens�������qr�ֽ��ͨ�ó���
%�����ļ�householder.m������householder�������qr�ֽ��ͨ�ó���.
%��Ҫ���ú����ļ�givens_qr.m, householder.m
A =[2.2439    0.7416    1.2046    0.0882
    0.7416    3.8766    2.4380    0.6108
    1.2046    2.4380    4.0725    2.0729
    0.0882    0.6108    2.0729    4.8069];
[q1,r1]=givens_qr(A);
[q2,r2]=householder_qr(A);
[q1 q2]                   %q1 r1��givens�任�õ���qr�ֽ�
[r1 r2]                   %q2 r2��householder�任�õ���qr�ֽ�