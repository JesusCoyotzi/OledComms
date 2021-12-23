# Basic OLED interface for STM32

This repo is a small utility to convert images into appropriate serialized files and send them to an STM32 micro-controller to display on an small black and white OLED screen based on the SSD1306 driver. This is part of my experiments about STM32 but since it is an standalone app plus some extra scripts decided to make a separate repo.

## Requirements
This repo assumes a Linux distribution. I built this with Ubuntu 20.04 but any relatively normal Linux distro should work. Moreover compiling to windows should be possible. The target is a STM32F103C8 micro-controller commonly found on the cheap blue-pill board as it is cheap and easy to find but should be easy to port to different STM32.

Other required things to compile and load this program into your micro-controller
* Hardware Debugger: St-link v2 works
* Arm compilation tool-chain. I use gcc-arm-none-eabi:
* Openocd for debugging and loading
* Debugger. I use only openocd to load the program i prefer to use gdb-multiarch for actual debugging


## Image serialization
This also includes a couple py scripts to allow image serialization and some basic image processing. The idea is you can provide a reasonably sized image and produce and .oled file which can then be loaded using the send_image.py script. send_batch.sh is simply an example in case you want to send more than one image at a time. The image serialization scripts are meant more as an example of how to produce and send the correct streams to the micro-controller. Refer to the scripts themselves for full usage
