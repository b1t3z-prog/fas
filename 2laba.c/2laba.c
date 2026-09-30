#include <stdio.h>

int main() {
    int count_x = 1;
    for (int a = 1; a <= 20; a++) {
        for (int b = 0; b < 20 - a; b++) {
            printf(" ");
        }
        for (int k = 0; k < count_x; k++) {
            printf("X");
        }
        printf("\n");
        count_x = count_x + 2;
    }
    return 0;
}