#include "stdio.h"
#include <unistd.h>
#include <wiringPi.h>

#define LED 26
#define BTN 19

int counter = 0;

static void count(struct WPIWfiStatus wfiStatus, void* userdata) {
    counter++;
    printf("%d\n", counter);
}

int main(int argc, char* argv[]){
    printf("Hello, World\n");
    wiringPiSetupGpio();

    pinMode(LED, OUTPUT);
    pinMode(BTN, INPUT);
    pullUpDnControl(BTN, PUD_DOWN);

    wiringPiISR2(BTN, INT_EDGE_BOTH, &count, 3000, NULL);
    while (1){
        digitalWrite(LED, (counter % 2));
    }

    return 0;
}
