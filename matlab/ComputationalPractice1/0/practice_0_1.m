n=[1,2,3,5,10,20,100];
x=[.5,.9,1.1,1.5];
A=[];
for j=1:1:9
    for i=1:1:4
        if j==1
           A(i,j)=x(i);
        end
        if j==9
            A(i,j)=log(x(i));
        end
        if (j<9)&&(j>1)
            A(i,j)=log_Taylor(x(i),n(j-1));
        end
    end
end
A           %A的第1列为x的4个取值, 第2到8列分别为n取1,2,3,5,10,20,100时计算出4个x的近似对数值，第9列为4个x的真正对数值