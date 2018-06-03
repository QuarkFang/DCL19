#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

#define MAXSIZE 100
#define OVERFLOW 1

typedef struct{
    int r[MAXSIZE + 1];
    int length;
}SqList;

int InitList(SqList *L){
    //SqList *L;
    L = (SqList*)malloc(sizeof(SqList));
    if(!L)
        exit(OVERFLOW);
    L->length = 0;
    return 1;
}

int CreateList(SqList *L, int n){
    int e, i;
    printf("请输入元素:\n");
    for(i = 1; i <= n; i++){
        scanf("%d", &e);
        L->r[i] = e;
    }
    L->length = n;
    return 1;
}

int PrintList(SqList *L){
    int i;
    for(i = 1; i <= L->length; i++){
        printf("%2d", L->r[i]);
    }
    return 1;
}

int cmp(int i, int j){
    if(i >= j)
        return 0;
    else
        return 1;
}

void InsertSort(SqList *L){
    int i, j;
    for(i = 2; i <= L->length; i++){
        if(cmp(L->r[i], L->r[i - 1])){
            L->r[0] = L->r[i];
            L->r[i] = L->r[i-1];
            for(j = i - 2; cmp(L->r[0], L->r[j]); --j){
                L->r[j+1] = L->r[j];
            }
            L->r[j+1] = L->r[0];
        }
    }
}

int binarySearch(SqList *L, int target) {
    int low = 0, high = L->length-1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (L->r[mid] < target) { low = mid + 1; }
        if (L->r[mid] > target) { high = mid - 1; }
        if (L->r[mid] == target) { return mid; }
    }
    if(L->r[low] == target)
    {
        return low;
    }
    return 0;
}

int main()
{
    SqList L;
    int n;
    InitList(&L);
    printf("输入元素个数:\n");
    scanf("%d", &n);
    CreateList(&L, n);
    InsertSort(&L);
    PrintList(&L);
    printf("\n");
    while(1)
    {
        printf("输入查找元素:\n");
        scanf("%d", &n);
        printf("位于：");
        printf("%d\n", binarySearch(&L, n));
    }
    return 0;
}
