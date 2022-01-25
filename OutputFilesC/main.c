#include <stdio.h>
#include <stdbool.h>

void main() {
bool Foo(int x) {
if (x > 3) {
return 1;
}
else {
return 0;
}
}
int x = 4;
for (int i = 1; i <= 6; i++) {
printf("Foo of");printf("%d", i);printf(" is ");printf("%d", Foo(i));printf("\n");x = i;
}
x = 2;
}
