n=5;                                          %n=5
A=zeros(n,n);                                 %����ϵ������A�ͳ�������b
b=[];
for i=1:1:n
    for j=1:1:n
        if abs(i-j)==1
            A(i,j)=1;
        end
        if i==j
            A(i,j)=-4;
        end
    end
end
for i=1:1:n
    if i==1
        b(i)=-27;
    else
        b(i)=-15;
    end
end
D={};                                          %����cramer������Di��Ӧ�ľ���
for i=1:1:n
    D{i}=A;
    for j=1:1:n
        D{i}(j,i)=b(j);
    end
end
x=[];
tic                                        %��ʼ�ⷽ��
  
for i=1:1:n
    x(i)=det(D{i})/det(A);
end

toc


n=10;                                          %n=10
A=zeros(n,n);                                 %����ϵ������A�ͳ�������b
b=[];
for i=1:1:n
    for j=1:1:n
        if abs(i-j)==1
            A(i,j)=1;
        end
        if i==j
            A(i,j)=-4;
        end
    end
end
for i=1:1:n
    if i==1
        b(i)=-27;
    else
        b(i)=-15;
    end
end
D={};                                          %����cramer������Di��Ӧ�ľ���
for i=1:1:n
    D{i}=A;
    for j=1:1:n
        D{i}(j,i)=b(j);
    end
end
x1=[];
tic                                         %��ʼ�ⷽ��
  
for i=1:1:n
    x1(i)=det(D{i})/det(A);
end

toc
