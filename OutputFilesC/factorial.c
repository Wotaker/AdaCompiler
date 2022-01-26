#include <stdio.h>
#include <stdbool.h>

bool Sdbx() {
bool bt = 1;
bool bf = 0 && !bt;
bool b_res = 1;
b_res = (!bf && bt) || bf;
if (2.0 < 4.0) {
return b_res;
}
return !b_res;
}
