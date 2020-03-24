function [a,b]=Jacobi_eig(A,p)
if p==1                 %p=1时用古典Jacobi方法，p=2时用关卡式Jacobi方法，关卡值取a_n=1/n^3
[~,n]=size(A);
E=eye(n);
R=E;
tau=1;
while tau>eps
    sigma=0;
for i=1:1:n
    sigma=sigma+(A(i,i))^2;
end
tau=sum(sum(A.^2))-sigma;
    if tau<eps
        break;
    end
i1=1;j1=2;
for i=1:1:n
    for j=i+1:1:n
        if abs(A(i,j))>abs(A(i1,j1))
            i1=i;
            j1=j;
        end
    end
end
theta=0.5*acot((A(i1,i1)-A(j1,j1))/(-2*A(i1,j1)));
c=cos(theta);
s=sin(theta);
T=E;
p=i1;
q=j1;
T(p,p)=c;
T(p,q)=s;
T(q,p)=-s;
T(q,q)=c;
A=T'*A*T;
R=R*T;
end
a=R;



else
[~,n]=size(A);
E=eye(n);
R=E;
M=1000;
for s=1:1:M
    alpha=1/s^3;
i1=1;j1=1;
while i1~=0||j1~=0
i1=0;j1=0;o=0;
for i=1:1:n
    for j=i+1:1:n
        if abs(A(i,j))>alpha
            i1=i;
            j1=j;
            o=1;
            break;
        end
    end
    if o==1
        break;
    end
end
if i1==0||j1==0
    break;
end
theta=0.5*acot((A(i1,i1)-A(j1,j1))/(-2*A(i1,j1)));
c=cos(theta);
s=sin(theta);
T=E;
p=i1;
q=j1;
T(p,p)=c;
T(p,q)=s;
T(q,p)=-s;
T(q,q)=c;
A=T'*A*T;
R=R*T;
a=R;
end
end
end
b=A;
