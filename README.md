# PrusaConnectPiCam
Setup a PiCam to connect to PrusaConnect via python

# Setup
1. Go to your PrusaConnect Dashboard and click on the "Camera" tab  
![Screenshot_2](https://github.com/postpapa/PrusaConnectPiCam/assets/22226501/f972e6fe-26d0-4eb7-8f69-ab7ee26d26ae)

2. Scroll down to the "Other cameras" section and click "Add new other camera"  
![Screenshot_3](https://github.com/postpapa/PrusaConnectPiCam/assets/22226501/9137034c-559e-414a-b533-fb60a02a0762)

3. Connect to your pi, clone the git repo and go into the new created folder  
   ```
   sudo apt install git
   git clone https://github.com/postpapa/PrusaConnectPiCam
   cd PrusaConnectPiCam
   ```

4. run the setup.py and enter the requested infos  
`python3 setup.py`

   4.1 Enter the token. You can find the token below the name of your "Other camera"  
   ![Screenshot_8](https://github.com/postpapa/PrusaConnectPiCam/assets/22226501/ee01478d-62b7-4048-b7d3-58dbad1cfb28)  
   4.2 Enter an alternative name for your "Other camera"  
   4.3 If everything went well you should see "Request was successful." in the terminal  
   4.3.1 You may need to install `pip3` and `requests` lib
   ```
   sudo apt update
   sudo apt install python3-pip
   sudo pip3 install requests
   ```

5. Check on the PrusaConnect site if the name of your "Other camera" was changed and the status changed to "Registered"  
![Screenshot_9](https://github.com/postpapa/PrusaConnectPiCam/assets/22226501/c001c6e0-81ed-447d-975a-c72214006c0b)


6. run the "sendscreenshots.py" script to test the uploading part. after a while you should see an image on your PrusaConnect Camera tab
`python3 sendscreenshot.py`

   ![Screenshot 2023-10-03 084004](https://github.com/postpapa/PrusaConnectPiCam/assets/22226501/7c8cba94-d457-41b0-a6fd-1925c66f34ac)
`ctrl + c` to exit the script

## Install `sendscreenshot.py` as a service to run it in the background

1. Make `sendscreenshot.py` executeable  
   `chmod +x sendscreenshot.py`

2. create the service file and insert the following code  
   `sudo nano /etc/systemd/system/sendscreenshot.service`
   ```
   [Unit]
   Description=Uploads images to prusacloud
   After=networking.service

   [Service]
   ExecStart=/home/pi/PrusaConnectPiCam/sendscreenshot.py
   WorkingDirectory=/home/pi/PrusaConnectPiCam
   Restart=always
   RestartSec=5

   [Install]
   WantedBy=multi-user.target
   ```
   2.1 Adjust the `ExecStart` and `WorkingDirectory` as needed. You can get the current directory if you enter `pwd` in the terminal  
   2.2 press `ctrl + x` followed by `y` to save the file

3. You can now start/stop the service with the following commands
   ```
   sudo systemctl start sendscreenshot.service
   sudo systemctl stop sendscreenshot.service
   ```

## Optional

If you want that the service starts automatically after the pi rebootet type the following line into the terminal  
`sudo systemctl enable sendscreenshot.service`
