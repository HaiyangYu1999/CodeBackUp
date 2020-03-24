function a=ten2two(x)
A=floor(x);
B=x-A;
r=[];
t=[];
k=1;
j=0;
while A>=2
    r(k)=mod(A,2);
    A=(A-r(k))/2;
    k=k+1;
end
r(k)=A;
s=0;
for i=1:k
    s=s+r(i)*10^(i-1);
end

while (B>0)&&(j<15)
    j=j+1;
    t(j)=floor(2*B);
    B=2*B-t(j);
end
p=0;
if j>0
    for i=1:j
    p=p+t(i)*10^(-i);
    end
end
format long g;
a=s+p;