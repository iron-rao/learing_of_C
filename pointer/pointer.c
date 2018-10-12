#include<stdio.h>
int main()
{
    int a = 20;
    float b =40.0;
    char c ='a';
    int *ptrI;
    float *ptrF;
    char *ptrC;
    ptrI = &a;
    printf("%d\n",*ptrI);
    printf("%p\n",&a);
    *ptrI = *ptrI * 4;
    printf("%d\n",*ptrI);
    printf("%p\n",&a);
    return 0;

}