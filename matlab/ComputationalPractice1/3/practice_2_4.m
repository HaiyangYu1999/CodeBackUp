A1=[9 -36 30;-36 192 -180;30 -180 180];   %需要文件cholesky.m
A2=hilb(6);
L1=cholesky(A1);
L2=cholesky(A2);
[L1 chol(A1)]                             %经检验, 在忽略转置的情况下自定义函数cholesky()求得的结果和内置函数chol()求得的结果相同
[L2 chol(A2)]
chol(A2)