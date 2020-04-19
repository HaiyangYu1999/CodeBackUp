function  [ x, y ] = Improved_Euler( f, tspan,y0 )
y ( 1 ) = y0;
a=tspan(1);
b=tspan(2);
h = 0.01;
n=((b-a)/h);
x = a : h : b;
for i = 1 : n
    yt = y ( i ) + h * feval ( f, x ( i ), y ( i ) );
    yi = y ( i ) + h * feval ( f, x ( i + 1 ), yt );
    y ( i + 1 ) = 1 / 2 * ( yt + yi );
end
x=x';
y=y';