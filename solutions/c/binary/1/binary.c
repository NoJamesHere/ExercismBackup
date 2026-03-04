#include "binary.h"

int convert(const char *input){
    int decimal_value = 0;
    int power = 1;
    for(int i = strlen(input) - 1; i >= 0; i--){
        if(input[i] != '1' && input[i] != '0') return INVALID;
        decimal_value += (input[i] == '1') ? 1 * power : 0;
        power *= 2;
    }
    return decimal_value;
}