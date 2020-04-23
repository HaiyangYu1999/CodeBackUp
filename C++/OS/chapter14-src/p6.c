#include<stdlib.h>
#include<stdio.h>

int main(int argc,char* argv[])
{
    int* a=(int*)malloc(100*sizeof(int));
    free(a);
    printf("%d",a[0]);
}
/*
$gdb ./p6
$(gdb) run

Starting program: /mnt/d/materials/OS_projects/chapter14-src/p6                                                         
0[Inferior 1 (process 1832) exited normally]
*/

/*
$valgrind --leak-check=yes ./p6
==1855== Memcheck, a memory error detector                                                                              
==1855== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.                                                
==1855== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info                                             
==1855== Command: ./p6                                                                                                  
==1855==                                                                                                                
==1855== error calling PR_SET_PTRACER, vgdb might block                                                                 
==1855== Invalid read of size 4                                                                                         
==1855==    at 0x108707: main (p6.c:8)                                                                                  
==1855==  Address 0x522d040 is 0 bytes inside a block of size 400 free'd                                                
==1855==    at 0x4C30D3B: free (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)                                 
==1855==    by 0x108702: main (p6.c:7)                                                                                  
==1855==  Block was alloc'd at                                                                                          
==1855==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)                               
==1855==    by 0x1086F2: main (p6.c:6)                                                                                  
==1855==                                                                                                                
0==1855==                                                                                                               
==1855== HEAP SUMMARY:                                                                                                  
==1855==     in use at exit: 0 bytes in 0 blocks                                                                        
==1855==   total heap usage: 2 allocs, 2 frees, 912 bytes allocated                                                     
==1855==                                                                                                                
==1855== All heap blocks were freed -- no leaks are possible                                                            
==1855==                                                                                                                
==1855== For counts of detected and suppressed errors, rerun with: -v                                                   
==1855== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
*/