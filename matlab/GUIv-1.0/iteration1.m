function [x,k]=iteration1(A,b,x0,p,ep,M)          
if nargin==4                              %默认误差限为1e-6, 最大迭代次数为10000 
    ep=1e-6;                              %当函数参数p=1时用Jacobi迭代法，p=2时用Gauss-Seidel迭代法
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
    warning('超过最大迭代次数，可能不收敛'); 
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
    warning('超过最大迭代次数，可能不收敛'); 
end
end
x=xa;
