L1=[2 0 0;4 -3 0;-2 6 -12];     %需要文件lower_triangular_inv.m
L2=[3 0 0;1 4 0;4 -7 5];
U=[1 2 1 -2;0 5 3 -2;0 0 3 5;0 0 0 3];
[lower_triangular_inv(L1) inv(L1)]          
[lower_triangular_inv(L2) inv(L2)]
[lower_triangular_inv(U')' inv(U)] %利用自定义函数lower_triangular_inv()求得的逆矩阵直接计算得的逆矩阵inv()相等
%由于lower_triangular_inv()只适用于下三角矩阵的求逆，而U是上三角矩阵，所以对U先取转置U’，计算出U’的逆后再取转置得到U的逆