#include<stdlib.h>

int main(int argc,char* argv[])
{
    int* p=NULL;
    free(p);
}

/* 
$gdb ./null
$(gdb) run

Starting program: /mnt/d/materials/OS_projects/chapter14-src/null                                                       
[Inferior 1 (process 1179) exited normally]
*/

/* 
$valgrind --leak-check=yes ./null
==1547== Memcheck, a memory error detector                                                                              
==1547== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.                                                
==1547== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info                                             
==1547== Command: ./null                                                                                                
==1547==                                                                                                                
==1547== error calling PR_SET_PTRACER, vgdb might block                                                                 
==1547==                                                                                                                
==1547== HEAP SUMMARY:                                                                                                  
==1547==     in use at exit: 0 bytes in 0 blocks                                                                        
==1547==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated                                                       
==1547==                                                                                                                
==1547== All heap blocks were freed -- no leaks are possible                                                            
==1547==                                                                                                                
==1547== For counts of detected and suppressed errors, rerun with: -v                                                   
==1547== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
*/