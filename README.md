QR Code Scanner and Authentication System
This repository contains two Python scripts for a QR code scanning system. The main functionality includes decoding QR codes from images or live video feed, highlighting the QR code areas, and providing authentication based on a predefined list of authorized QR code data.

Features
QR Code Scanner (main.py):

Utilizes OpenCV and Pyzbar library for decoding QR codes.
Can read QR codes from images or live video feed.
Displays QR code data, highlights code areas, and provides real-time feedback.
Authentication System (authentication.py):

Reads QR code data from live video feed.
Authenticates the QR code data based on a predefined list stored in mydata.txt.
Marks authorized QR codes in green and unauthorized ones in red.
How to Use
QR Code Scanner (main.py):

Run main.py to start the QR code scanning system.
Ensure OpenCV and Pyzbar libraries are installed (pip install opencv-python pyzbar).
Adjust camera settings using cp.set(3,640) and cp.set(4,480) as needed.
Authentication System (authentication.py):

Run authentication.py to start the authentication system.
Ensure OpenCV and Pyzbar libraries are installed (pip install opencv-python pyzbar).
Create a mydata.txt file with a list of authorized QR code data.
Dependencies
Python 3.x
OpenCV
Pyzbar
NumPy
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
OpenCV
Pyzbar
Feel free to contribute or report issues!
