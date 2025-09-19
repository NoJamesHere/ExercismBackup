#include "grains.h"

namespace grains {

unsigned long long square(int number){
    if (number < 1 || number > 64){
        throw std::invalid_argument("Square must be between 1 and 64");
    }
    
    return 1ULL << (number - 1);
}
    
unsigned long long total(){
        return ~0ULL;
    }
}  // namespace grains
