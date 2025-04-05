# SunFounder PiCar-V (Updated Version)

This is an updated version of the PiCar-V Software by SunFounder. It was modified in order to work on the new Raspberry Pi OS version:

- Release date: November 19th 2024
- System: 64-bit
- Kernel version: 6.6
- Debian version: 12 (bookworm)

It might also work on other versions, but this was not tested. Further, some example scripts were added to the repository to demonstrate the usage of the camera for line following. They are located in the `examples` directory.

## Installation

For the installation of the software on a new installation of the previously mentioned operating system, the following steps are required:

- Install `git` with `sudo apt update && sudo apt install git -y`
- Clone the repository with `git clone https://github.com/tobiasriesen/SunFounder_PiCar-V.git`
- Go to the repository folder with `cd SunFounder_PiCar-V`
- Run the installation script with `sudo ./install_dependencies`
- Restart your Raspberry Pi
- Before using the remote control server, go to the `remote_control` directory and run `python manage.py migrate`
