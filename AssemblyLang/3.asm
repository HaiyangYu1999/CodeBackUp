assume cs:code

code segment

	mov ax,code
	mov ds,ax
	mov ax,20h
	mov es,ax
	mov bx,0
	mov cx,002fh
s:	mov al,[bx]
	mov es:[bx],al
	inc bx
	loop s
	mov ax,4c00h
	int 21h
	
code ends
end