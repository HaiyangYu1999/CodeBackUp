H_6=hilb(6);                %��Ҫ�ļ� givens_qr.m
b=[1,6,0,9,2,7]';
b=H_6*b;
b1=b;
[Q,R]=givens_qr(H_6);       %ԭ�������Ϊ Rx = Q'b
b=Q'*b;
[m,n]=size(H_6);
x=zeros(m,1);
x(m)=b(m)/R(m,m);          %��������η�����õ���x
for i=m-1:-1:1
    a=0;
    for j=i+1:1:m
        a=a+R(i,j)*x(j);
    end
    x(i)=(b(i)-a)/R(i,i);
end
x_1=H_6\b1 ;  
[x x_1]             %������,�Զ��庯��givens_qr()��õĽ�x��ֱ����õĽ�x_1���������ķ�Χ�����