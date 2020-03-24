assume cs:code

data segment
	db 'Welcome to masm!',0,'String2',0
data ends

code segment
start:	mov dh,8      ;row
		mov dl,3      ;column
		mov cl,2      ;color
		mov ax,data
		mov ds,ax
		mov si,0h     
		call show_ptr
		mov ax,4c00h
		int 21h
		
show_ptr:	push bx
			push cx
			push ax
			push dx
			push es
			
			mov ax,0b80ah
			mov es,ax
			mov ax,0
			mov al,dh    ;calculate offset
			mov bl,160
			mul bl
			mov bx,ax    ;bx is the beginning index
			mov ah,0
			mov al,2
			mul dl
			add bx,ax
			
			mov al,cl    ;al is the color
			
	ifzero:	mov ch,0
			mov cl,ds:[si]
			jcxz ok
			mov dl,ds:[si]
			mov es:[bx],dl
			mov es:[bx+1],al
			inc si
			add bx,2
			jmp ifzero
			
			
	ok:		pop es
			pop dx
			pop ax
			pop cx
			pop bx
			ret
			
			
code ends

end start