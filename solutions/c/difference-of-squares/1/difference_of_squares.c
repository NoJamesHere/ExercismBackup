#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number){
    unsigned int final_number = 0;
    for(unsigned int i = 1; i <= number; i++){
        unsigned int current = i * i;
        final_number += current;
    }
    return final_number;
}
unsigned int square_of_sum(unsigned int number){
    unsigned int final_number = 0;
    for (unsigned int i = 1; i <= number; i++){
        final_number += i;
    }    
    return final_number * final_number;
}
unsigned int difference_of_squares(unsigned int number){
    unsigned int sum_of_squares_num = sum_of_squares(number);
    
    unsigned int square_of_sum_num = square_of_sum(number);

    return square_of_sum_num - sum_of_squares_num;
}
