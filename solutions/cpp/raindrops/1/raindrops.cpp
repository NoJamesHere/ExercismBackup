#include <string>
#include "raindrops_test.cpp"
#include "raindrops.h"

namespace raindrops {
// wtf is the number??
// huh?
    // am i too woke or something? WHAT DO YOU WANT FROM MEEEE
    std::string convert(int number){
        // I guess
        std::string st;
        if (number % 3 == 0){
            st += "Pling";
        }
        if(number % 5 == 0){
            st += "Plang";
        }
        if(number %  7 == 0){
            st += "Plong";
        }
        if(number % 5 != 0 && number % 3 != 0 && number % 7 != 0){
            st = std::to_string(number);
        }
        return st;
    }
// this is so stupid how am i supposed to know where what goes????
}  // namespace raindrops
