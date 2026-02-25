#include "collatz_conjecture.h"

int steps(int start){
    if(start <= 0) return -1;
    int current_steps = 0;
    while(start != 1){
        if(start % 2 == 0){
            start /= 2;
        }
        else start = start * 3 + 1;
        current_steps++;
    }
    return current_steps;
}