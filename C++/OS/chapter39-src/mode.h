#ifndef GETMODE
#define GETMODE
#include<sys/stat.h>
void getMod(struct stat *buf, char* protection, char* mod, char* fileType);
#endif