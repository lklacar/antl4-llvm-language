#include <stdio.h>


int fibbonacci(int n) {
   if(n == 0){
      return 0;
   }

   if(n == 1) {
      return 1;
   }

    return fibbonacci(n-1) + fibbonacci(n-2);
}

int main() {
    int res = fibbonacci(45);

    printf("%d", res);




    return 0;
}
