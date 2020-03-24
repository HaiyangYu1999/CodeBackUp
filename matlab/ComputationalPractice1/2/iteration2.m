function [x,k]=iteration2(A,B,b,x0,p,ep,M)          
if nargin==5                             %Ĭ�������Ϊ1e-6, ����������Ϊ10000 
    ep=1e-6;                             %��p=1ʱ�÷ֿ�Jacobi��������p=2ʱ�÷ֿ�Gauss-Seidel������
    M=10000;
end
C=[A B;B A];
D=mat2cell(C,[size(A,1) size(B,1)],[size(A,2),size(B,2)]);
B0=mat2cell(b,[size(A,1) size(B,1)],1);
X0=mat2cell(x0,[size(A,1) size(B,1)],1);
Xa=X0;
if p==1                                    
    for k=1:1:M
    Xb=Xa;
    for i=1:1:size(D,1)
        c=0;d=0;
        for s=1:1:i-1
            c=c+D{i,s}*Xb{s};
        end
        for s=i+1:1:size(D,1)
            d=d+D{i,s}*Xb{s};
        end
        Xa{i}=-D{i,i}\(c+d-B0{i});
    end
    xa=[];
    xb=[];
    for i=1:1:size(Xa,1)
        xa=[xa;Xa{i}];
        xb=[xb;Xb{i}];
    end
    if norm(xa-xb)<ep
        break;
    end
    end
    if k==M
    warning('�������������������ܲ�����'); 
    end
end
if p==2                                    %��p=1ʱ�÷ֿ�Jacobi��������p=2ʱ�÷ֿ�Gauss-Seidel������
    for k=1:1:M
    Xb=Xa;
    for i=1:1:size(D,1)
        c=0;d=0;
        for s=1:1:i-1
            c=c+D{i,s}*Xa{s};
        end
        for s=i+1:1:size(D,1)
            d=d+D{i,s}*Xb{s};
        end
        Xa{i}=-D{i,i}\(c+d-B0{i});
    end
    xa=[];
    xb=[];
    for i=1:1:size(Xa,1)
        xa=[xa;Xa{i}];
        xb=[xb;Xb{i}];
    end
    if norm(xa-xb)<ep
        break;
    end
    end
    if k==M
    warning('�������������������ܲ�����'); 
    end
end
    x=xa;
