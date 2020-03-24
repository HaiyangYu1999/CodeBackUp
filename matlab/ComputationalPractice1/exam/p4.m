%需要调用函数文件givens_qr.m, hessenberg.m, qr_algorithm.m, Jacobi_eig.m,
%需要调用函数文件eigenvalue2.m
%姓名:于海洋，教学号:21160927
A =[2.2439    0.7416    1.2046    0.0882
    0.7416    3.8766    2.4380    0.6108
    1.2046    2.4380    4.0725    2.0729
    0.0882    0.6108    2.0729    4.8069];
warning('off');
[a1,b1]=qr_algorithm(A,2) ;              %实用qr算法
[a2,b2]=Jacobi_eig(A,2);                 %关卡Jacobi方法
[a1 b1]
[a2 b2]
%这个题运行时间较长，请耐心等待