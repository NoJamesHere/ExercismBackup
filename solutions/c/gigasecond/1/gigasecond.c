#include "gigasecond.h"

void gigasecond(time_t input, char *output, size_t size){
    input += 1000000000;   
    struct tm *utc_time = gmtime(&input);

    snprintf(output, size, "%04d-%02d-%02d %02d:%02d:%02d",
            utc_time->tm_year + 1900,
            utc_time->tm_mon + 1,
            utc_time->tm_mday, 
            utc_time->tm_hour,
            utc_time->tm_min,
            utc_time->tm_sec);
}