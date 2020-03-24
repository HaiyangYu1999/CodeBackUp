function [L,U,P]=column_lu(A)
[m,n]=size(A);
if m~=n
    error('输入的矩阵必须是方阵');
end
E=eye(n);
p=cell(n-1,1);
g=cell(n-1,1);
for k=1:1:n-1
    P=eye(n);
    r=k;
    a=abs(A(k,k));
    for i=k+1:1:n
        if a<abs(A(i,k))
            r=i;
            a=abs(A(i,k));
        end
    end
    P(k,k)=0;
    P(r,r)=0;
    P(r,k)=1;
    P(k,r)=1;
    p{k,1}=P;
    A=P*A;
    l=zeros(n,1);
    l(k+1:1:n,1)=A(k+1:1:n,k);
    G=E-l*E(:,k)'/A(k,k);
    g{k,1}=G;
    A=G*A;
end
P=eye(n);
for i=n-1:-1:1
    P=P*p{i,1};
end
G=eye(n);
g_bar=cell(n-1,1);
for i=1:1:n-1
    G=g{i,1};
    for j=i+1:1:n-1
        G=p{j,1}*G*p{j,1};
    end
    g_bar{i,1}=G;
end
G=eye(n);
for i=n-1:-1:1
    G=G*g_bar{i,1};
end
L=inv(G);
U=A;
