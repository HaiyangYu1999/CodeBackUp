A1=[2 4 -2;1 -1 5;4 1 -2];        %��Ҫ�ļ�crout_lu.m linearsolve_lu.m det_lu.m 
A2=[3 1 0;9 3 1;0 9 3];
A3=[1 2 1 -2;2 5 3 -2;-2 -2 3 5;1 3 2 3];
[L1,U1]=crout_lu(A1);
[L2,U2]=crout_lu(A2);            %���й����д��д���ᱨ��˵��A2��ǰn-1��˳��������������һ�����Ƿ�����ģ�������ע�͵����ٴ������Ի����ȷ���
[L3,U3]=crout_lu(A3);
L1                                %A1��A3�ķֽ���
U1
L3
U3
[det_lu(A1) det(A1)];              %����LU�ֽ���õ�����ʽdet_lu()��ֱ�Ӽ���õ�����ʽdet()���
[det_lu(A3) det(A3)];
[linearsolve_lu(A1,eye(size(A1))),inv(A1)];%���ýⷽ������õ������linearsolve_lu()��ֱ�Ӽ���õ������inv()���
[linearsolve_lu(A3,eye(size(A3))),inv(A3)];
linearsolve_lu(A1,eye(size(A1)))