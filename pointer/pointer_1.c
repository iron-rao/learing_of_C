/*
I need to post a question on Piazza for address.
*/
#include<stdio.h>
int main(int argc, char const *argv[])
{
    int a =10;
    int *ptrA;
    ptrA=&a;
   // ptrA = ptrA+1; 
    //printf("%d\n",a);
    printf("%d\n",*ptrA);
    printf("%p\n",ptrA);
    //printf("%p\n",&a);
    for (int i=0;i<5;i++)
    {
        ptrA = ptrA+1;
        printf("地址是：%p\n",ptrA);
        printf("数据是：%d\n",*ptrA);
    }
   /* int b =20;
    int *ptrB;
    ptrB=&b;
    ptrB=ptrA;
    printf("%d\n",b);
    printf("%d\n",*ptrB);
    printf("%p\n",ptrB);
    printf("%p\n",&b);*/

    return 0;
}
