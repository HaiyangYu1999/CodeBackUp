function [x,k]=iteration1(A,b,x0,p,ep,M)          
if nargin==4                              %Ĭ�������Ϊ1e-6, ����������Ϊ10000 
    ep=1e-6;                              %����������p=1ʱ��Jacobi��������p=2ʱ��Gauss-Seidel������
    M=10000;
end
[m,~]=size(b);
xa=x0;
if p==1                                   
    for k=1:1:M
    xb=xa;
    for i=1:1:m
        c=0;d=0;
        for s=1:1:i-1
            c=c+A(i,s)*xb(s);
        end
        for s=i+1:1:m
            d=d+A(i,s)*xb(s);
        end
        xa(i)=-(c+d-b(i))/A(i,i);
    end
    if norm(xa-xb)<ep
        break;
    end
    end
if k==M
    warning('�������������������ܲ�����'); 
end
end
if p==2
    for k=1:1:M
    xb=xa;
    for i=1:1:m
        c=0;d=0;
        for s=1:1:i-1
            c=c+A(i,s)*xa(s);
        end
        for s=i+1:1:m
            d=d+A(i,s)*xb(s);
        end
        xa(i)=-(c+d-b(i))/A(i,i);
    end
    if norm(xa-xb)<ep
        break;
    end
    end
if k==M
    warning('�������������������ܲ�����'); 
end
end
x=xa;
