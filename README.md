# friedelino's Raspi-Weatherstation

... my tiny little weatherstation running on my good old Raspi 2B+ @home using
the [Adafruit BMP280](https://www.adafruit.com/product/2651 "Adafruit BMP280")
Sensor.

!!! Extremly WIP !!!

General TODOs:
- [ ] Make it clean code
- [ ] Publish the backend
- [ ] Get rid of shell-scripts
- [ ] Turn into pyproject
- [ ] Add nix files


## Refactoring `raspi-weatherstation.py`:

### Basic Structure: 

1. cmdline parsing, 
2. reading data 
3. Plotting

### TODOs

- [ ] move each structure section to seperate functions (classes?!?)
- [ ] make STARTDATE first data point.
- [ ] implement error handling
- [ ] switch to english
- [ ] maybe use more fancy cmd line parsing / menu (click, cloup, ...)
