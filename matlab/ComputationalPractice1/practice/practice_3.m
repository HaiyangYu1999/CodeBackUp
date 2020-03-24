s=0;                                       %循环结构
a=1/2;
for i=0:1:63
    a=a*2;
    s=s+a;
end
 
b=[];                                    %sum函数
for i=1:1:64
    b(i)=2^(i-1);
end
r=sum(b); 