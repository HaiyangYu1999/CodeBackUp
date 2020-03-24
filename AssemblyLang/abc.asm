assume cs:abc

abc segment

  mov ax,2
  add ax,ax
  add ax,ax
  mov ax,4c00
  int 21
abc ends

end