#include "square_root.h"

int square_root(int squared){
    // sorry but only works for perfect squares ;-;
    if(squared == 1 || squared == 0) return squared;
    for(int i = 2;;i++){
        if((i * i) == squared) return i;
    }
}