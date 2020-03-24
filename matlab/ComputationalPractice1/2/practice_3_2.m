N=10;h=1/N;
A=zeros(N-1,N-1);
A(1,1)=2;A(1,2)=-1;
for i=2:1:N-2
    A(i,i-1)=-1;
    A(i,i)=2;
    A(i,i+1)=-1;
end
A(N-1,N-2)=-1;A(N-1,N-1)=2;
f=zeros(N-1,1);
for i=1:1:N-1
    f(i)=4*((i*h)^2)*(5*i*h-3);
end
b=(h^2*f);
x0=ones(N-1,1);
ep=1e-6;
M=10000;
w=2/(1+sin(pi*h));
[x1,k1]=iteration1(A,b,x0,1,ep,M);
[x2,k2]=iteration1(A,b,x0,2,ep,M);
[x,k]=SOR(A,b,x0,w,ep,M);
[x1 x2 x]                       %Jacobi��������Ϊ244����Gauss-Seidel��������126��2��
[k1 k2 k]
[x,k]=SOR(A,b,x0,w,ep,M);   
s=0.01:0.01:1.99;           %�����������ɳ�����
s=s';
[n,~]=size(s);
for i=1:1:n
    [~,k(i)]=SOR(A,b,x0,s(i),ep,M);
end
[10000*s k']                       %���Թ۲쵽��w��2/(1+sin(pi*h))=1.53����ʱ�����������٣�Ϊ28��