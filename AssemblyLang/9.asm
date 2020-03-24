assume cs:code

data segment
	db 'welcome to masm!'
data ends 

code segment
start:	mov ax,data
		mov es,ax
		
		mov ax,0b872h
		mov ds,ax
		mov di,00
		
		mov cx,10h
		mov bx,0h

	s:	mov dl,00000010b
		mov al,es:[bx]
		mov ds:[di],al
		inc di
		mov ds:[di],dl
		inc di
		inc bx
		loop s
		
		mov cx,10h
		mov bx,0h

	s2:	mov dl,00100100b
		mov al,es:[bx]
		mov ds:[di],al
		inc di
		mov ds:[di],dl
		inc di
		inc bx
		loop s2
		
		mov cx,10h
		mov bx,0h

	s3:	mov dl,01110001b
		mov al,es:[bx]
		mov ds:[di],al
		inc di
		mov ds:[di],dl
		inc di
		inc bx
		loop s3
		
		mov ax,4c00h
		int 21h
	code ends
	
end start