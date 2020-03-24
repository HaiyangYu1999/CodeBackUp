assume cs:code,ds:data,es:table

data segment
db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
db '1993','1994','1995'


dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5937000


dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
dw 11542,14430,15257,17800

data ends

table segment
db 21 dup ('year summ ne ?? ') 
table ends

stack segment
	dw 0,0,0,0,0,0,0,0
stack ends

code segment
start:	mov ax,data
		mov ds,ax
		mov ax,table
		mov es,ax
		mov ax,stack
		mov ss,ax
		mov sp,10h
		
		mov bp,0             ;table index
		mov bx,0             ;data index
		mov cx,21
	year:	push cx
			mov si,0
			mov cx,4
			
	year0:	mov al,ds:[bx]
			mov es:[bp+si],al
			inc bx
			inc si
			loop year0
			
			pop cx
			add bp,10h
			loop year
			
		mov bp,0
		mov cx,21

	rvn:	mov ax,ds:[bx]
			mov dx,ds:[bx+2]
			mov es:[bp+5],ax
			mov es:[bp+7],dx
			add bp,10h
			add bx,4
			loop rvn;
	
		mov bp,0
		mov cx,21

	num:	mov ax,ds:[bx]
			mov es:[bp+10],ax
			add bp,10h
			add bx,2
			loop num
	
		mov bp,0
		mov cx,21
	
	dvd:	mov ax,es:[bp+5]
			mov dx,es:[bp+7]
			div word ptr es:[bp+0ah]
			mov es:[bp+0dh],ax
			add bp,10h
			loop dvd
	
		
		mov ax,4c00h
		int 21h
		
code ends

end start