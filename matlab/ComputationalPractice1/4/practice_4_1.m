A1=[1 5 3 2;5 3 1 8;6 2 8 9;4 2 1 7];
A2=[7 6 6 6;-5 -6 -9 -9;3 6 10 8;-1 -2 -3 -1];
[a1,b1,c1]=eigenvalue1(A1,1);          %ai是对应bi的特征向量，bi是最大特征值，ci是迭代次数
[a2,b2,c2]=eigenvalue1(A1,2);
[a3,b3,c3]=eigenvalue1(A2,1);
[a4,b4,c4]=eigenvalue1(A2,2);
[a1 a2 a3 a4]
[b1 b2 b3 b4]
[c1 c2 c3 c4]
p1=abs(b1);                    %谱半径
p2=abs(b3);
[~,s1,~]=eigenvalue1(A1'*A1,1);
[~,s2,~]=eigenvalue1(A2'*A2,1);
n21=sqrt(s1);                     %2范数
n22=sqrt(s2);