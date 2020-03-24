function [x,k]=SOR(A,b,x0,w,ep,M) 
[m,~]=size(b);
xa=x0;
    for k=1:1:M
    xb=xa;
    for i=1:1:m
        c=0;d=0;
        for s=1:1:i-1
            c=c+A(i,s)*xa(s);
        end
        for s=i:1:m
            d=d+A(i,s)*xb(s);
        end
        xa(i)=xb(i)-w*(c+d-b(i))/A(i,i);
    end
    if norm(xa-xb)<ep
        break;
    end
    end
    if k==M
    warning('超过最大迭代次数，可能不收敛'); 
    end
    x=xa;