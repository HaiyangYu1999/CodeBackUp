function d=det_lu(A)        %利用lu分解求矩阵的行列式
a=1;                        %需要文件crout_lu.m
[L,U]=crout_lu(A);
for i=1:1:size(A)
   a=a*L(i,i)*U(i,i);
end
d=a;