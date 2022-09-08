#include <stdio.h>
#include <stdlib.h>

int main(){
    int x = 1;
    auto fun = [x](){
        printf("%d\n", x);
    };
    fun();

    return 0;
}
