judgement=@(varargin)varargin{2*find([varargin{1:2:end}],1)}();  
%�ж���������������������2i-1������Ϊ�棬��ִ�е�2i������,����ִ��2i֮�������
fi=@(f,n)judgement(n<=2,1,1,@()f(f,n-1)+f(f,n-2));                %�ݹ�
fib=@(n)fi(fi,n);                                                 %Ϊ�˱��ⴴ��һ�������ļ�������������ʵ�ֵݹ�
a=[];
for i=1:1:15
    a(i)=fib(i);
end
[(1:1:15)',a']                                                   %fib����ǰ15��