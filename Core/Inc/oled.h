#ifndef OLED_HEADER
#define OLED_HEADER

#include "stm32f1xx_hal.h"

#define OLED_ADDR 0x3c << 1
#define CMD_ADDR 0x00
#define DATA_ADDR 0x40

#define PIX_PER_COL 8
//#define PAGES_PER_SCREEN 4
#define PAGES_PER_SCREEN 8
#define COLS_PER_PAGE 128
#define WIDTH COLS_PER_PAGE
#define HEIGHT PIX_PER_COL * PAGES_PER_SCREEN  

extern I2C_HandleTypeDef hi2c1;

void write_cmd_oled(uint8_t cmd);
void write_data_oled(uint8_t* dataBuffer, size_t dataSize);
void initOled();

#endif 
