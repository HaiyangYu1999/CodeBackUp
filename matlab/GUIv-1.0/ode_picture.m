f=@(x,y)cos(x)*cos(y);
tspan=[0,20];
y0=1;
[x1,y1]=ode45(f,tspan,y0);
[x2,y2]=ode113(f,tspan,y0);
[x3,y3]=ode23t(f,tspan,y0);
[x4,y4]=ode23s(f,tspan,y0);
[x5,y5]=Improved_Euler(f,tspan,y0);
plot(x1,y1,'b',x2,y2,'k',x3,y3,'r',x4,y4,'m',x5,y5,'g');
legend('4-order Runge-Kutta','Adams method','trapezia method','2-order Rosenbrock','Improved-Euler')