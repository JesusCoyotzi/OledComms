# Basic OLED interface for STM32

This repo is a small utility to convert images into appropiate serialized files and send them to an STM32 microcontroller to display on an small black and white OLED screen based on the SSD1306 driver. 

## Requirements
This repo assumes a linux distribution. I built this with Ubuntu 20.04 but any relatively normal linux distro should work. Moreover compiling to windows should be possible. The target is a STM32F103C8 microcontroller commonly found on the cheap blue-pill board as it is cheap and easy to find but should be easy to port to different STM32.

Other required things to compile and load this program into your microcontroller
* Hardware Debugger: StLink v2 works
* Arm compilation toolchain. I use gcc-arm-none-eabi:
* Openocd for debugging and loading
* Debugger. I use only openocd to load the program i prefer to use gdb-multiarch for actual debugging


