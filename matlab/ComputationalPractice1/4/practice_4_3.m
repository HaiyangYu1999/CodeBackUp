A=[7 6 6 6;-5 -6 -9 -9;3 6 10 8;-1 -2 -3 -1];
warning('off');%由于qr算法求得的特征值十分接近A的特征值，在反幂法解方程中的系数矩阵(A-aE)趋于奇异矩阵，因此会产生许多Warning
[a1,b1]=qr_algorithm(A,1);        %ai是特征向量组，bi是对应的特征值
[a2,b2]=qr_algorithm(A,2);      
[a1 a2]                     
%由于需要调用自定义函数givens_qr()，hessenberg()和eigenvalue2()，
%而这些自定义函数并不高效，所以本程序需要较长的时间(大约8秒)才能运行出正确结果