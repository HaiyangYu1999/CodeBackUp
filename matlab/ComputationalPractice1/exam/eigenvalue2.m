function [a,b,c]=eigenvalue2(A,l,p,z,M,ep)

[~,n]=size(A);
if nargin==3
    ep=1e-6;
    M=1e5;
    z=ones(n,1);
end
m=l;
r=l;
if p==1          %p=1ʱ�ô�ԭ��λ�Ƶķ��ݷ���p=2ʱ�ô������̼��ٵĴ�ԭ��λ�Ƶķ��ݷ�
for s=1:1:M
    z1=z;
    m1=m;
    v1=(A-l*eye(4))\z;
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
b=1/m+l;
c=s;
a=z;
end

if p==2
for s=1:1:M
    z1=z;
    r1=r;
    [~,id]=max(abs(z));
    m=z(id);
    z=(A-r*eye(4))\z/m;
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
[~,id]=max(abs(z));
    m=z(id);
a=z/m;
end

