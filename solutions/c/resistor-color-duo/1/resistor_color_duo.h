#ifndef RESISTOR_COLOR_DUO_H
#define RESISTOR_COLOR_DUO_H

typedef enum {
    BLACK,
    BROWN,
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    VIOLET,
    GREY,
    WHITE
} resistor_band_t;

#include <stdint.h>
uint16_t color_code(resistor_band_t colors[]);
#endif
