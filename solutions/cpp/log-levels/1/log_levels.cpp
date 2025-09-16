#include <string>

namespace log_line {
std::string message(std::string line) {
    // ??????
    size_t finalIndex = line.find(":") + 2;
    std::string finals = line.substr(finalIndex);
    return finals;
}
std::string log_level(std::string line) {
    size_t first = line.find("[") + 1;
    size_t last = line.find("]") - 1;
    std::string finalline = line.substr(first, last);
    return finalline;
}

std::string reformat(std::string line) {
    size_t firstbracket =  line.find("[") + 1;
    size_t secondbracket = line.find("]") - 1;
    std::string insidebracket = line.substr(firstbracket, secondbracket);
    size_t finalIndex = line.find(":") + 2; 
    std::string message = line.substr(finalIndex);

    std::string level = "(" + insidebracket + ")";

    
    return message + " " + level;
    
}
}  // namespace log_line
