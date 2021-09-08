# raspberrypi-gpio-flask-react


## Introduction

While working on my Cloud Native Architecture Nanodegree I learned how to run an app using Flask as the backend and React as the frontend. So I took the code and decided to make my own app that controls GPIO pins. I will show you the steps I took and how you can run this on your own.

### Getting Started

### Hardware

* Raspberry Pi 3B+ (any model should work just fine)
* Red LED
* 220 Ohm Resistor
* Micro SD Card for the Pi
* Jumper cables
* 9G Servo Motor
* My Robot Torvalds (any robot can be used)

### Software

* Docker and docker-compose (Follow [this](https://docs.docker.com/get-docker/) link to install docker
* Raspberry Pi OS (For the Raspberry Pis)

## Running the software

To run the software run the `docker-compose docker-compose.yml` and the app should run. Go to the `http://localhost:3000` link to access the app. There you can press the buttons to control the LED, Servo and robot. You can add to this code to add more Raspberry Pis and more Robots if you wish. 

## Screenshot of App

* `GPIO Microservice`
* ![service](https://github.com/sentairanger/raspberrypi-gpio-flask-react/blob/main/Screenshot%20from%202021-08-25%2018-42-06.png)
