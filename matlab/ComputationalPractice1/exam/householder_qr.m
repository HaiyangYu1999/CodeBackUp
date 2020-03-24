function [q,r] = householder_qr(A)    %不需要满足A是方阵，但矩阵A的行数m和列数要满足m>n
[m,n]=size(A);
Q=eye(m);
for i=1:1:n-1
    x=A(i:m,i);
    y=zeros(m+1-i,1);
    y(1)=norm(x);
    H=eye(m+1-i)-(2/(norm(x-y))^2)*(x-y)*(x-y)';
    if i>1
        H=blkdiag(eye(i-1),H);
    end
    A=H*A;
    Q=H*Q;
end
q=Q';
r=A;
