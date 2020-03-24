A=[6.5 8;8 10];
b=[0.8,1]';
b_1=[0.79,1.01]';
delta_b=b_1-b;
[Q,R]=qr(A);
b=Q'*b;
b_1=Q'*b_1;
m=2;
x=zeros(m,1);
x(m)=b(m)/R(m,m);          
for i=m-1:-1:1
    a=0;
    for j=i+1:1:m
        a=a+R(i,j)*x(j);
    end
    x(i)=(b(i)-a)/R(i,i);
end
x_1=zeros(m,1);
x_1(m)=b_1(m)/R(m,m);          
for i=m-1:-1:1
    a=0;
    for j=i+1:1:m
        a=a+R(i,j)*x_1(j);
    end
    x_1(i)=(b_1(i)-a)/R(i,i);
end                        %用解方程组的qr算法解出x是原方程的解，x_1是扰动方程的解 
[x,x_1]
delta_x=x_1-x;
p=norm(delta_x,inf)/norm(x,inf);
q=norm(delta_b,inf)/norm(b,inf);      
r=p/q;                         %cond(A)的下界为r,即230.5059
s=r/norm(A,inf);               %s是A的逆的范数的估计
r_1=cond(A);                     %用内置函数求得的条件数c为270.2463
s_1=norm(inv(A),inf);            %用内置函数求得的A的逆的范数为18
