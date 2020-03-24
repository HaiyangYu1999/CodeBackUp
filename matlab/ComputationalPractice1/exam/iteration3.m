function [x,k]=iteration3(A,b,x0,p,ep,M)          
if nargin==4                              %默认误差限为1e-6, 最大迭代次数为10000 
    ep=1e-6;                              %当p=1时用最速下降法，p=2时用极小残量法，p=3时用共轭梯度法
    M=10000;
end
if p==1
r0=b-A*x0;
ra=r0;
xa=x0;
for k=0:1:M
    rb=ra;
    xb=xa;
    alpha=(ra'*ra)/((A*ra)'*ra);
    xa=xb+alpha*rb;
    ra=rb-alpha*A*rb;
    if norm(ra)<ep
        break;
    end
end
if k==M
    warning('超过最大迭代次数，可能不收敛'); 
end
end
if p==2
r0=b-A*x0;
ra=r0;
xa=x0;
for k=0:1:M
    rb=ra;
    xb=xa;
    beta=((A*ra)'*ra)/((A*ra)'*(A*ra));
    xa=xb+beta*rb;
    ra=rb-beta*A*rb;
    if norm(ra)<ep
        break;
    end
end
if k==M
    warning('超过最大迭代次数，可能不收敛'); 
end
end
if p==3
r0=b-A*x0;
p0=r0;
ra=r0;
xa=x0;
pa=p0;
for k=0:1:M
    xb=xa;
    rb=ra;
    pb=pa;
    if (pb'*(A*pb)==0) | (ra==zeros(size(ra)))
        break;
    end
    alpha=(rb'*pb)/((A*pb)'*pb);
    xa=xb+alpha*pb;
    ra=rb-alpha*A*pb;
    
    beta=-(ra'*(A*pb))/(pb'*(A*pb));
    pa=ra+beta*pb;
end
if k==M
    warning('超过最大迭代次数，可能不收敛'); 
end
end
x=xa;