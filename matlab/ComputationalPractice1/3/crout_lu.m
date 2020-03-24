function [l,u]=crout_lu(A)
[m,n]=size(A);
if m~=n
    error('输入的矩阵必须是方阵');
end
L=zeros(n,n);
U=zeros(n,n);
U(1,1)=1;
for k=1:1:n
    L(k,1)=A(k,1);
    if L(1,1)==0
        error('输入的矩阵的前n-1个顺序主子阵必须是非奇异的');
    end
end
for k=2:1:n
    U(1,k)=A(1,k)/L(1,1);
end
for i=2:1:n
    for k=i:1:n
        a=0;
        b=0;
        for j=1:1:(i-1)
            a=a+L(k,j)*U(j,i);
        end
        L(k,i)=A(k,i)-a;
        if L(i,i)==0
            error('输入的矩阵的前n-1个顺序主子阵必须是非奇异的');
        end
        for j=1:1:(i-1)
            b=b+L(i,j)*U(j,k);
        end
        U(i,k)=(A(i,k)-b)/L(i,i);
    end
end
l=L;
u=U;
end