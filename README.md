DCMS
===
The system DCMS (Distributed Classroom Management System) is designed to enhance the learning experience.

This repository is included the demo of Portable Camera Module.

Installation
----
1. Install the Raspberry Pi OS into the SD card according to [official website](https://www.raspberrypi.org/downloads/).
2. Boot to Raspbian
3. Config the system to boot to console with auto-login (user: pi)
4. Checkout the source code into the pi's home folder
5. Append the following command into ~/pi/.bashrc

        python /home/pi/dcms/demo.py
6. Connect the Raspberry Pi to the circuit

       ![Circuit](https://raw.githubusercontent.com/kensonman/dcms/master/DemoCircuit.png)
       - LED1 – The YELLOW LED; Indicate the Ready Mode;
       - LED2 – The RED LED; Indicatee the Recording Mode;
       - R1 – 1KΩ Resistor; Limit the current;
       - R2 – 1KΩ Resistor; Limit the current;
       - R3 – 10KΩ Resistor; Limit the current;
       - SW1 – Switch between Ready Mode and Recording Mode;
7. Reboot
