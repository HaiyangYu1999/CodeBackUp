A1=[2 4 -2;1 -1 5;4 1 -2];        %需要文件crout_lu.m linearsolve_lu.m det_lu.m 
A2=[3 1 0;9 3 1;0 9 3];
A3=[1 2 1 -2;2 5 3 -2;-2 -2 3 5;1 3 2 3];
[L1,U1]=crout_lu(A1);
[L2,U2]=crout_lu(A2);            %运行过程中此行代码会报错，说明A2的前n-1个顺序主子阵至少有一个不是非奇异的，将此行注释掉后再次运行以获得正确结果
[L3,U3]=crout_lu(A3);
L1                                %A1和A3的分解结果
U1
L3
U3
[det_lu(A1) det(A1)];              %利用LU分解求得的行列式det_lu()和直接计算得的行列式det()相等
[det_lu(A3) det(A3)];
[linearsolve_lu(A1,eye(size(A1))),inv(A1)];%利用解方程组求得的逆矩阵linearsolve_lu()和直接计算得的逆矩阵inv()相等
[linearsolve_lu(A3,eye(size(A3))),inv(A3)];
linearsolve_lu(A1,eye(size(A1)))