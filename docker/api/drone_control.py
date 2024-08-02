# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os
import subprocess
import sys
import time
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
   from pynput.keyboard import Key, Listener
except:
   install('pynput==1.3')
   from pynput.keyboard import Key, Listener


client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)


def execute(key):
    try:
        rc_data = airsim.RCData()
        if key.char == 't':
            client.takeoffAsync().join()
        
        if key.char == 'a':
            rc_data.throttle = 0.5  # Throttle (0.0 to 1.0)
            rc_data.roll = -0.8  # Roll (-1.0 to 1.0)
            rc_data.pitch = 0.0  # Pitch (-1.0 to 1.0)
            rc_data.yaw = 0.0 # Yaw (-1.0 to 1.0)
            client.moveByRC(rc_data)
            time.sleep(0.1)

    except:
        pass
 
# Collect all event until released
with Listener(on_press = execute) as listener: 
  
    listener.join()