A=[1 .5 .5;.5 1 .5;.5 .5 1];
x=[9 2 7]';                 %��ѧ�ź�3λ
b=A*x;
s1=0;s2=3;s3=10;s4=100;
x1=[s1,s1,s1]';
x2=[s2,s2,s2]';
x3=[s3,s3,s3]';
x4=[s4,s4,s4]';
[j1,k1]= iteration1(A, b, x1, 1);[g1,n1]= iteration1(A, b, x1, 2);
[j2,k2]= iteration1(A, b, x2, 1);[g2,n2]= iteration1(A, b, x2, 2);
[j3,k3]= iteration1(A, b, x3, 1);[g3,n3]= iteration1(A, b, x3, 2);
[j4,k4]= iteration1(A, b, x4, 1);[g4,n4]= iteration1(A, b, x4, 2);
[j1 j2 j3 j4]               %ʹ��Jacobi�������Ľ�
[k1 k2 k3 k4]               %ʹ��Jacobi�������ĵ�������
[g1 g2 g3 g4]               %ʹ��Gauss-Seidel�������Ľ�
[n1 n2 n3 n4]               %ʹ��Gauss-Seidel�������ĵ�������
