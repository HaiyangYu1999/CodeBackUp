assume cs:codeseg

codeseg segment
	
	mov ax,0
	mov ds, ax
	mov ds:[26h],ax
	
	mov ax,004ch
	int 21h
codeseg ends
	
end