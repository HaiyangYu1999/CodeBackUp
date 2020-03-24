A=[2.2439 0.7416 1.2046 0.0882;
    0.7416 3.8766 2.4380 0.6108;                 %姓名:于海洋，教学号:21160927
    1.2046 2.4380 4.0725 2.0729;
    0.0882 0.6108 2.0729 4.8069];
x1=[0,9,2,7]';                                 %构造精确解
b=A*x1;
D={};                                          %构造cramer法则中Di对应的矩阵
n=4;
for i=1:1:n
    D{i}=A;
    for j=1:1:n
        D{i}(j,i)=b(j);
    end
end
x=[];
for i=1:1:n                                    %开始解方程
    x(i)=det(D{i})/det(A);
end
x=x'                                             %x即为用克莱默法则的解
[L,U,P]=column_lu(A)                          %L,U,P为三角分解的结果,需要调用函数文件column_lu.m

                                             %用三角分解的结果求解方程组
c=zeros(n,1);
c(1)=b(1)/L(1,1);
for i=2:1:n
    a=0;
    for j=1:1:i-1
        a=a+L(i,j)*c(j);
    end
    c(i)=(b(i)-a)/L(i,i);
end
d=zeros(n,1);
d(n)=c(n)/U(n,n);
for i=n-1:-1:1
    a=0;
    for j=i+1:1:n
        a=a+U(i,j)*d(j);
    end
    d(i)=(c(i)-a)/U(i,i);
end
d                                                  %d为用三角分解求得的方程的解

