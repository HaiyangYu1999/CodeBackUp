function s=log_Taylor(x,n)
a=1;
s=0;
for i=1:1:n                          %���ؾ����㷨����Taylorչ��
    if i==1
        a=x-1;
    else
        a=a*(-1)*(x-1)*((i-1)/i);
    end
    s=s+a;
end
