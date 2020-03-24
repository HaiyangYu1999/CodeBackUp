format short g;
n=0:1:20;
a=[];
a(1)=0.6321;                             %从I0开始递推I20
for i=2:21
    a(i)=1-i*a(i-1);
end
b=[];
b(21)=0.0455;                             %从I20开始递推I0
for i=20:-1:1
    b(i)=(1-b(i+1))/(i+1);
end
c=[];                                     %数值积分(自适应Lobatto法)
for i=1:21
    f=@(x)x.^(i-1).*exp(x-1);
    c(i)=quadl(f,0,1);
end
d=[];                                     %符号积分
sym x;
for i=1:21
    d(i)=int(x^(i-1)*exp(x-1),x,0,1);
end
A=[n' a' b' c' d']