#include<stdlib.h>

int main(int argc,char* argv[])
{
    int* p=(int*)malloc(sizeof(int));
}

/* 
$gdb ./p4
$(gdb) run

Starting program: /mnt/d/materials/OS_projects/chapter14-src/p4                                                         
[Inferior 1 (process 1581) exited normally]
*/

/*
$valgrind --leak-check=yes ./p4
==1587== Memcheck, a memory error detector                                                                              
==1587== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.                                                
==1587== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info                                             
==1587== Command: ./p4                                                                                                
==1587==                                                                                                                
==1587== error calling PR_SET_PTRACER, vgdb might block                                                                 
==1587==                                                                                                                
==1587== HEAP SUMMARY:                                                                                                  
==1587==     in use at exit: 4 bytes in 1 blocks                                                                        
==1587==   total heap usage: 1 allocs, 0 frees, 4 bytes allocated                                                       
==1587==                                                                                                                
==1587== 4 bytes in 1 blocks are definitely lost in loss record 1 of 1                                                  
==1587==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)                               
==1587==    by 0x108662: main (p4.c:5)                                                                                  
==1587==                                                                                                                
==1587== LEAK SUMMARY:                                                                                                  
==1587==    definitely lost: 4 bytes in 1 blocks                                                                        
==1587==    indirectly lost: 0 bytes in 0 blocks                                                                        
==1587==      possibly lost: 0 bytes in 0 blocks                                                                        
==1587==    still reachable: 0 bytes in 0 blocks                                                                        
==1587==         suppressed: 0 bytes in 0 blocks                                                                        
==1587==                                                                                                                
==1587== For counts of detected and suppressed errors, rerun with: -v                                                   
==1587== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
*/