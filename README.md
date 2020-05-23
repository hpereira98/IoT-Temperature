# IoT-Temperature
A small project for a ESP826 microcontroller using MicroPython to check temperature and humidity

## Getting Started:

- Mount ESP32 on the Breadboard
- Erase ESP32 previous data: 
```bash
esptool.py erase_flash
```
- Flash the MicroPython firmware to the board at address O
```
esptool.py --chip esp32 --port <your_serial_port> --baud 460800 write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin
```
- Connect to your board using RShell:
```bash
rshell --port <your_serial_port>
```
And then to interact with it in real time:
```bash
repl
```
- My ESP32 board only has one programmable LED (blue) on GPIO2.

## Working with files:

- List files and dirs on board, inside RShell:
```bash
ls /pyboard
```
- Copy file to board:
```bash
rshell --port <board serial port name> cp <py_file> /pyboard
```