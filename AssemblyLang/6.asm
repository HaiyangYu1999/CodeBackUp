assume cs:code, ss:stacksg, ds: datasg

datasg segment
	db '1. display      '
	db '2. brows        '
	db '3. replace      '
	db '4. modify       '
datasg ends

stacksg segment
	dw 0,0,0,0,0,0,0,0
stacksg ends

code segment

start:	mov ax,stacksg
		mov ss,ax
		mov sp,10h
		mov ax,datasg
		mov ds,ax
		
		mov bx,0h
		mov cx,4
		
	s:	push cx
		mov cx,4h
		mov di,3h
		
	s0:	mov al,[bx+di]
		and al,11011111b
		mov [bx+di],al
		inc di
		loop s0
		
		pop cx
		add bx,10h
		loop s
		
		mov ax,4c00h
		int 21h

code ends

end start