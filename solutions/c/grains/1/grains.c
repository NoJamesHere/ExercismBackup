#include "grains.h"


uint64_t square(uint8_t index){
    if(index > 64 || index <= 0) return 0;
    uint64_t final_number = 1;
    for(uint64_t i = 1; i < index; i++){
        final_number *= 2;
    }
    return final_number;
}
uint64_t total(void){
    return UINT64_MAX;
}
