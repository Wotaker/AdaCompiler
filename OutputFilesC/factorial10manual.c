#include "stdbool.h"
#include <stdio.h>
void Factorial10() {
bool b_res = 1;
int acc = 1;
for (int i = 1; i <= 6 + 5; i++) {
acc = acc * i;
}
printf("res: %d\n", acc);
}

int main(int argc, char** argv){
    Factorial10();
}