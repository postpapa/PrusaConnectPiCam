#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import picamera
import time
import os

def send_snapshot():
    camera = picamera.PiCamera()
    current_path = os.path.dirname(os.path.realpath(__file__))  # Aktueller Pfad des Python-Skripts
    image_path = os.path.join(current_path, 'snapshot.jpg')  # Vollständiger Pfad zur Schnappschussdatei
    url = 'https://connect.prusa3d.com/c/snapshot'
    headers = {
        'Token': 'CAMERATOKEN',
        'Fingerprint': 'CAMERAFINGERPRINT',
        'Content-Type': 'image/jpeg'
    }

    camera.capture(image_path)
    camera.close()

    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    headers['Content-Length'] = str(len(image_data))

    response = requests.put(url, headers=headers, data=image_data)

while True:
    send_snapshot()
    time.sleep(10)
