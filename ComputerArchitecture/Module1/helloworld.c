#include <stdio.h>

int main() {
    int arr[] = {15, 20, 25, 30, 35};
    int size = 5;
    int temp;
    for (int i = 0; i < size / 2; i++) {
        temp = arr[i];
        arr[i] = arr[size - i - 1];
        arr[size - i - 1] = temp;
    }
    for (int i = 0; i < (sizeof(arr) / sizeof(arr[0])); i++) {
        printf("%d\n", arr[i]);
    }
}
