function l=cholesky(A)
[m,n]=size(A);
if m~=n
    error('输入的矩阵必须是方阵');
end
L=[];
for j=1:1:n
    s=0;
    for k=1:1:j-1
        s=s+L(j,k)^2;
    end
    L(j,j)=sqrt(A(j,j)-s);
    for i=j+1:1:n
        r=0;
        for k=1:1:j-1
            r=r+L(i,k)*L(j,k);
        end
        L(i,j)=(A(i,j)-r)/L(j,j);
    end
end
l=L;