function [a,b,c]=eigenvalue1(A,p,M,ep,z)
[~,n]=size(A);
if nargin==2
    ep=1e-6;
    M=1e5;
    z=ones(n,1);
end
m=0;
r=1;
u=z;
if p==1          %p=1ʱ�ó��ݷ���p=2ʱ�ô������̼��ٵĳ��ݷ�

for s=1:1:M
    z1=z;
    m1=m;
    v1=A*z;
    [~,id]=max(abs(v1));
    m=v1(id);
    z=v1/m;
    
    if norm(m1-m)<ep
        break;
    end
end
if s==M
    warning('����������������ֵ�����ܲ�����');
end
b=m;
c=s;
a=z;
end


if p==2
   
for s=1:1:M
    z1=z;
    r1=r;
    z=A*z;
    [~,id]=max(abs(z));
    m=z(id);
    z=z/m;
    r=((A*z)'*(z))/(z'*z);
    if norm(r1-r)<ep
        break;
    end
end
if s==M
    warning('����������������ֵ�����ܲ�����');
end
b=r;
c=s;
a=z;
end

