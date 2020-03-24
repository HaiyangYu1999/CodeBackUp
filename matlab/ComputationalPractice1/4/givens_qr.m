function [q,r] = givens_qr(A) %矩阵A的行数m和列数要满足m>n
[m,n]=size(A);
Q=eye(m,n);
    for i=1:1:n
        for j=(i+1):1:m
        T=eye(m,m);
        c=A(i,i)/sqrt(A(i,i)^2+A(j,i)^2);
        s=A(j,i)/sqrt(A(i,i)^2+A(j,i)^2);
        T(i,i)=c;
        T(i,j)=s;
        T(j,i)=-s;
        T(j,j)=c;
        A=T*A;
        Q=T*Q;
        end
    end
q=Q';
r=A;