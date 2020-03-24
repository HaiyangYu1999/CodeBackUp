H_6=hilb(6);                 %需要文件 householder_qr.m
[q,r]=householder_qr(H_6);
[q_1,r_1]=qr(H_6);
[q,q_1]          %经检验,自定义函数householder_qr()和内置函数qr()求得的解除了符号外相等
[r,r_1]