#include "oled.h"


void write_cmd_oled(uint8_t cmd)
{
    //Send command one byte at at time
    HAL_I2C_Mem_Write(&hi2c1,OLED_ADDR, CMD_ADDR, 1, &cmd, 1, 100);
}

void write_data_oled(uint8_t* dataBuffer, size_t dataSize)
{
    //Send command one byte at at time
    HAL_I2C_Mem_Write(&hi2c1,OLED_ADDR, DATA_ADDR, 1, dataBuffer, dataSize, 100);
}

void initOled()
{
  
  // For 32 lines
  //  uint8_t mux_lines = 0x1f;
  //  uint8_t com_conf = 0x02;
  // For 64 lines
   uint8_t mux_lines = 0x3f;
   uint8_t com_conf = 0x12;

  
  uint8_t turn_on = 0xAF;
  uint8_t turn_off = 0xAE;
  write_cmd_oled(turn_off);
  //Set Memory addressing type
  write_cmd_oled(0x20);
  write_cmd_oled(0x00);
  //Set memory page start 
  write_cmd_oled(0xB0);
  //Mirroring
  write_cmd_oled(0xC8);
  write_cmd_oled(0xa1);
  
  //set columna low and high addr
  write_cmd_oled(0x00);
  write_cmd_oled(0x10);
  //Display start line : 0 -63 40 for 0
  write_cmd_oled(0x40);
  //Contrast 
  write_cmd_oled(0x81);
  write_cmd_oled(0xFF);
  //Set mux
  write_cmd_oled(0xa8);
  write_cmd_oled(mux_lines);
  //Follow RAM
  write_cmd_oled(0xA4);
  //No offset 
  write_cmd_oled(0xD3);
  write_cmd_oled(0x00);

  //timing
  //OScilattor freq
  write_cmd_oled(0xD5);
  write_cmd_oled(0xF0);
  //Pre-charge
  write_cmd_oled(0xD9);
  write_cmd_oled(0x22);
  //Com pins
  write_cmd_oled(0xDA);
  write_cmd_oled(com_conf);

  //Turn on
  //Vcomh
  write_cmd_oled(0xDB);
  write_cmd_oled(0x20);
  //Charge pump
  write_cmd_oled(0x8D);
  write_cmd_oled(0x14);
  write_cmd_oled(turn_on);
}
