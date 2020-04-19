assume cs:code

a segment
	dw 0fh
a ends

b segment
	db 2
b ends

code segment

start: 	mov ax,a
		mov es,ax
		
		mov ax,b
		mov ss,ax
		
		mov ax,es:[0]
		
		div byte ptr ss:[0]

		mov ax,4c00h
		int 21h

code ends

end start