L1=[2 0 0;4 -3 0;-2 6 -12];     %��Ҫ�ļ�lower_triangular_inv.m
L2=[3 0 0;1 4 0;4 -7 5];
U=[1 2 1 -2;0 5 3 -2;0 0 3 5;0 0 0 3];
[lower_triangular_inv(L1) inv(L1)]          
[lower_triangular_inv(L2) inv(L2)]
[lower_triangular_inv(U')' inv(U)] %�����Զ��庯��lower_triangular_inv()��õ������ֱ�Ӽ���õ������inv()���
%����lower_triangular_inv()ֻ�����������Ǿ�������棬��U�������Ǿ������Զ�U��ȡת��U���������U���������ȡת�õõ�U����