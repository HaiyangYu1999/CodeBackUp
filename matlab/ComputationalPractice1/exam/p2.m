%函数文件givens_qr.m是利用givens矩阵进行qr分解的通用程序，
%函数文件householder.m是利用householder矩阵进行qr分解的通用程序.
%需要调用函数文件givens_qr.m, householder.m
A =[2.2439    0.7416    1.2046    0.0882
    0.7416    3.8766    2.4380    0.6108
    1.2046    2.4380    4.0725    2.0729
    0.0882    0.6108    2.0729    4.8069];
[q1,r1]=givens_qr(A);
[q2,r2]=householder_qr(A);
[q1 q2]                   %q1 r1是givens变换得到的qr分解
[r1 r2]                   %q2 r2是householder变换得到的qr分解