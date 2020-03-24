A=magic(4);              %需要文件 hessenberg.m
[P,H]=hessenberg(A);
[P_1,H_1]=hess(A);
[P,P_1];  %经检验,自定义函数hessenberg()和内置函数hess()求得的解相等
[H,H_1];
H_1