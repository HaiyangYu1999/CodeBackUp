function yi=newton(x,y,xi)
%Newton插值方法，给定一系列插值的点(x,y)，得到在x=xi处的，牛顿插值多项的值yi
n=length(x);
m=length(y);
if m~=n
    error('x,y的长度不一样,请重新输入!');
    return
end
A=zeros(n);    %定义差商表
A(:,1)=y;      %差商表第一列为y
for j=2:n               %j为列标
    for i=1:(n-j+1)     %i为行标
        A(i,j)=(A(i+1,j-1)-A(i,j-1))/(x(i+j-1)-x(i));   %计算差商表
    end
end
%根据差商表,求对应的牛顿插值多项式在x=xi处的值yi
N(1)=A(1,1);
for j=2:n
    T=1;
    for i=1:j-1
        T=T*(xi-x(i));
    end
    N(j)=A(1,j)*T;
end
yi=sum(N);   %将x=xi带入牛顿插值多项式，得到的yi的值
end