# Hand-Gesture-Recognition
## Introduction
With the rapid advancement of technology, human-computer interaction has evolved from traditional imput devices to more natural and intuitive methods such as hand gestures. Gesture-based control systems provide a touch-free way of interacting with electronic devices, improving ease of use, hygiene, and accessibility. Such systems are increasingly being adpoted in applications like smart homes, automation, and assistive technologies.

This project focuses on the development of a **hand gesture controlled LED system using Arduino and Python**. The system uses a webcam to capture real-time hand movements, which are processed using python with OpenCV and MediaPipe for accurate hand tracking and gesture recognition. Each recognized gesture is mapped to a predefined command to control LEDs, such as turning them ON or OFF.

The generated commands are transmitted from the Python application to the Ardiuno microcontroller through serial communication. Upon receiving the commands, the Ardiuno controls the LEDs connected to its digital output pins. This project demonstrates the effective integration of computer vision, embedded systems, and hardware-software communication. 

The propsed system provides a simple and cost-effective approach to understanding gesture recognition and Arduino-based control. It serves as an excellent learning platform for beginners to explore concepts related to computer vision, automation, and human-machine interaction. 

## Components Required
1. Arduino Uno Board ( Arduino Uno is used as the controller for handling commands sent based on the hand gestures recognized by the camera )
2. LEDs (5 pieces) for each finger (Thumb, Index, Middle, Ring, Pinky)
3. Resistors (Five 220 Ohms for each LEDs )
4. Jumper wires ( Male to Female )
5. Breadboard

| Libraries Used | Function |
|---|---|
| OpenCV (cv2) | Perform real-time image processing and video handling. |
| MediaPipe | Recognize hand gestures efficiently without complex training. |
| PySerial (serial) | Communicate between Python program and Arduino board. |
| Arduino Core Library | Executes logic to turn LEDs ON/OFF |
 

## Circuit Diagram
<img width="1920" height="1080" alt="Circuit Diagram" src="https://github.com/user-attachments/assets/7282997e-faf7-4609-a555-014752dc836f" />

# Problem Statement
## Problem Definition
Traditional methods of controlling electronic devices such as LEDs rely on physical switches, buttons, or remote controllers. These methods require direct contact or dedicated hardware, which limits flexibility and convenience. There is a need for a touch-free and intuitive control system that allows users to interact with devices using natural hand gestures without physical contact.

## Motivation
Touch-based control systems are not always convenient or hygienic, especially in shared environments. Gesture-based control offers a more natural and user-friendly alternative, improving accessibility for users with physical limitations and enabling modern human–machine interaction. Developing such a system using low-cost components like Arduino and a webcam makes the technology affordable and suitable for educational and practical applications.

## Related Work (Existing Solutions)
Several gesture control systems have been developed using specialized sensors, gloves, or advanced hardware, which increase system complexity and cost. Some existing systems also require powerful processors or cloud-based computation, making them unsuitable for beginners or small-scale projects. Although gesture recognition exists, many solutions lack simplicity, affordability, or ease of implementation using basic microcontrollers like Arduino.


## Challenges
Implementing a gesture-based control system involves multiple challenges, such as:
- Accurate detection and tracking of hand gestures in real time
- Reliable communication between the computer and Arduino
- Minimizing delay and ensuring correct gesture-to-command mapping
- Handling variations in hand size, lighting conditions, and background images
- Limitation as: LEDs fliches when 2 hands are show to the webcam.
These challenges make gesture-based systems more complex than traditional switch-based controls.

## Proposed Solution (Approach)
To address these challenges, this project uses Python with OpenCV and MediaPipe to perform real-time hand gesture recognition using a standard webcam. Recognized gestures are mapped to predefined LED control commands. These commands are sent to an Arduino microcontroller via serial communication, which controls the LEDs connected to its digital pins. This approach provides a simple, low-cost, and effective solution for gesture-based LED control while demonstrating the integration of computer vision and embedded systems.

## Background
The system relies on Computer Vision (CV). The primary library, MediaPipe, uses a machine learning pipeline to identify 3D hand landmarks from a single frame. The Arduino UNO serves as the hardware controller.

## Past/Related Work
Traditional gesture recognition often required wearable sensors (accelerometers). This project is novel because it is camera-based and non-invasive, offering better functionality and lower cost compared to sensor-glove approaches.

## Project Management
The project was managed using a modular strategy:

Phase 1: Python environment setup and Hand Tracking module.

Phase 2: Arduino UNO firmware development and circuit assembly.

Phase 3: Integration and Serial Communication.

## Technical Sections

Design Details

The system captures video at 30 FPS. The Python script calculates the distance between finger tips to recognize "Open Palm" or "Fist."

Calculations and Diagrams

The circuit utilizes 220\Omega resistors for each LED to limit current from the Arduino UNO.

## Project Results and Analysis

Principal Results: The system successfully recognized five distinct gestures with an accuracy of approximately 92% in well-lit conditions.

Comparison: Compared to basic infrared (IR) sensors, this design allows for a much wider range of complex commands through a single camera sensor.

## Final Budget
- Arduino UNO :500rs
- LEDs and Resistors: 50rs
- Breadboard and Wires: 50rs
- Total: 600

## Project Deliverables
- Functional Hand Gesture Controlled LED System.
- Python Source Code (OpenCV/MediaPipe integration).
- Arduino UNO C++ Firmware.
   
## Recommendations and Future Work
Future iterations could implement a sign language model, which can recognise the sign language are in output the LED light glows.

Assigning every sign a binary combination, and the LEDs will glow according to that binary combination. 

Example: If we give a sign "A" the binary combination would be "00001", then the output will be 1 LED ON and rest are OFF 

## Conclusions
The project met its primary objective of controlling hardware via computer vision. The results demonstrate that high-performance gesture control is achievable using consumer-grade hardware and open-source libraries.


## Demo
![Example](./img/demo.gif)

## Reference 
- [Crontrolling LEDs Using Hand Gesture](https://circuitdigest.com/microcontroller-projects/controlling-leds-using-hand-gestures-with-esp32-and-python)
