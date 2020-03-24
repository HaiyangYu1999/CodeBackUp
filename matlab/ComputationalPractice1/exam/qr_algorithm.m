function [b,t]=qr_algorithm(A,p)
if nargin==1                           %���û�и���p��ֵ��Ĭ��ʹ�û���qr�㷨
    p=1;
end
if p==1                                 %p=1ʱ�û���qr�㷨��p=2ʱ��ʵ��qr�㷨
M=1000;
[~,n]=size(A);
A2=A;
for s=1:1:M
    
    [Q,R]=givens_qr(A2);
    A2=R*Q;
end
b=[];
for i=1:1:n
    [a,~,~]=eigenvalue2(A,A2(i,i),1);
    b=[b,a];
end
end

if p==2
[P,A]=hessenberg(A);
M=1e4;
A2=A;
[~,n]=size(A);
for s=1:1:M
    
    [Q,R]=givens_qr(A2);
    A2=R*Q;
end
b=[];
for i=1:1:n
    [a,~,~]=eigenvalue2(A,A2(i,i),1);
    b=[b,P*a];
end
end
for i=1:1:n
    for j=1:1:n
        if i<j
            R(i,j)=0;
        end
    end
end
t=R;
