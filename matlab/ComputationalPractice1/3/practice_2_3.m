H_4=hilb(4);               %需要文件column_lu.m
H_6=hilb(6);
[L_4,U_4,P_4]=column_lu(H_4);
[L_6,U_6,P_6]=column_lu(H_6);
[P_4*H_4,L_4*U_4]          
[P_6*H_6,L_6*U_6]
[l_4,u_4,p_4]=lu(H_4);
[l_6,u_6,p_6]=lu(H_6);
[L_4 l_4]                  %经检验自定义函数column_lu()的结果和内置函数lu()相同
[U_4 u_4]
[P_4 p_4]
[P_6 p_6]
[L_6 l_6]
[U_6 u_6]

x1=[1 6 0 9 2 7]';
b=H_6*x1;                 %原方程化为L_6*U_6*x=P_6*b
x=linearsolve_lu(L_6*U_6,P_6*b);
[x x1]                    %经检验三角分解求得的解x和精确解x1相等
