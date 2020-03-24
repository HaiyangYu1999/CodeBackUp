function x=linearsolve_lu(A,B)     %����lu�ֽ�����Է�����
[m,n]=size(A);                     %��Ҫ�ļ�crout_lu.m
[m1,n1]=size(B);
if m1~=m
    error('�����ά������ƥ��');
end
X=zeros(n,n1);
[L,U]=crout_lu(A);
for s=1:1:n1
    b=B(:,s);
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
X(:,s)=d;
end
x=X;