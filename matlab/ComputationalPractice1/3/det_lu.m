function d=det_lu(A)        %����lu�ֽ�����������ʽ
a=1;                        %��Ҫ�ļ�crout_lu.m
[L,U]=crout_lu(A);
for i=1:1:size(A)
   a=a*L(i,i)*U(i,i);
end
d=a;