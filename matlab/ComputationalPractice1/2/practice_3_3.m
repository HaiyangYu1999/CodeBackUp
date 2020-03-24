A=eye(3);
B=-ones(3,3)/4;
x0=zeros(6,1);
x=[1 6 0 9 2 7]';           %教学号后6位
b=[A B;B A]*x;
[x1,k1]=iteration2(A,B,b,x0,1);  
[x2 k2]=iteration2(A,B,b,x0,2);
[x1 x2]                     %分块Jacobi迭代法和分块Gauss-Seidel迭代法的结果
[k1 k2]                     %分块Jacobi迭代法和分块Gauss-Seidel迭代法的迭代次数