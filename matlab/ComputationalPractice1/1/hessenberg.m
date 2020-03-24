function [P,H] = hessenberg(A)         %A±ÿ–Î «∑Ω’Û
[~,n]=size(A);
Q=eye(n);
 for i=1:1:n-2
    c=A(i+1:n,i);
    d=zeros(n-i,1);
    d(1)=norm(c);
    H=eye(n-i)-(2/(norm(c-d))^2)*(c-d)*(c-d)';
    H=blkdiag(eye(i),H);
    A=H*A*H;
    Q=Q*H;
 end
P=Q;
H=A;

