function x=lower_triangular_inv(A)
[m,n]=size(A);
if m~=n
    error('����ľ�������Ƿ���');
end
B=eye(n);
X=zeros(n,n);
for i=1:1:n-1
    for j=i+1:1:n
        if A(i,j)~=0
            error('����ľ�������������Ǿ���');
        end
    end
end
for i=1:1:n
    if A(i,i)==0
        error('����ľ�����������');
    end
end
for s=1:1:n
    b=B(:,s);
    c=zeros(n,1);
    c(1)=b(1)/A(1,1);
    for i=2:1:n
        a=0;
        for j=1:1:i-1
            a=a+A(i,j)*c(j);
        end
        c(i)=(b(i)-a)/A(i,i);
    end
    X(:,s)=c;
end
x=X;