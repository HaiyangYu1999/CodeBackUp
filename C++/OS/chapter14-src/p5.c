#include<stdlib.h>

int main(int argc,char* argv[])
{
    int* a=(int*)malloc(100*sizeof(int));
    a[100]=0;
}

/* 
$gdb ./p5
$(gdb) run

Starting program: /mnt/d/materials/OS_projects/chapter14-src/p5                                                         
[Inferior 1 (process 1700) exited normally] 
*/

/*
$valgrind --leak-check=yes ./p5
==1725== Memcheck, a memory error detector                                                                              
==1725== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.                                                
==1725== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info                                             
==1725== Command: ./p5                                                                                                  
==1725==                                                                                                                
==1725== error calling PR_SET_PTRACER, vgdb might block                                                                 
==1725== Invalid write of size 4                                                                                        
==1725==    at 0x108671: main (p5.c:6)                                                                                  
==1725==  Address 0x522d1d0 is 0 bytes after a block of size 400 alloc'd                                                
==1725==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)                               
==1725==    by 0x108662: main (p5.c:5)                                                                                  
==1725==                                                                                                                
==1725==                                                                                                                
==1725== HEAP SUMMARY:                                                                                                  
==1725==     in use at exit: 400 bytes in 1 blocks                                                                      
==1725==   total heap usage: 1 allocs, 0 frees, 400 bytes allocated                                                     
==1725==                                                                                                                
==1725== 400 bytes in 1 blocks are definitely lost in loss record 1 of 1                                                
==1725==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)                               
==1725==    by 0x108662: main (p5.c:5)                                                                                  
==1725==                                                                                                                
==1725== LEAK SUMMARY:                                                                                                  
==1725==    definitely lost: 400 bytes in 1 blocks                                                                      
==1725==    indirectly lost: 0 bytes in 0 blocks                                                                        
==1725==      possibly lost: 0 bytes in 0 blocks                                                                        
==1725==    still reachable: 0 bytes in 0 blocks                                                                        
==1725==         suppressed: 0 bytes in 0 blocks                                                                        
==1725==                                                                                                                
==1725== For counts of detected and suppressed errors, rerun with: -v                                                   
==1725== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
*/
