judgement=@(varargin)varargin{2*find([varargin{1:2:end}],1)}();  
%判断条件函数，如果从左起第2i-1个参数为真，则执行第2i个命令,而不执行2i之后的命令
fi=@(f,n)judgement(n<=2,1,1,@()f(f,n-1)+f(f,n-2));                %递归
fib=@(n)fi(fi,n);                                                 %为了避免创建一个函数文件，用匿名函数实现递归
a=[];
for i=1:1:15
    a(i)=fib(i);
end
[(1:1:15)',a']                                                   %fib数列前15项