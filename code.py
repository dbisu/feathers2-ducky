# License : GPLv2.0
# copyright (c) 2021  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# FeatherS2 board support


import usb_hid
from adafruit_hid.keyboard import Keyboard

# comment out these lines for non_US keyboards
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode

# uncomment these lines for non_US keyboards
# replace LANG with appropriate language
#from keyboard_layout_win_LANG import KeyboardLayout
#from keycode_win_LANG import Keycode

import time
import digitalio
from board import *
from duckyinpython import *
import wifi
from webapp import *


# sleep at the start to allow the device to be recognized by the host computer
time.sleep(.5)

def startWiFi():
    # Get wifi details and more from a secrets.py file
    try:
        from secrets import secrets
    except ImportError:
        print("WiFi secrets are kept in secrets.py, please add them there!")
        raise

    print("Connect wifi")
    #wifi.radio.connect(secrets['ssid'],secrets['password'])
    wifi.radio.start_ap(secrets['ssid'],secrets['password'])
    HOST = repr(wifi.radio.ipv4_address_ap)
    PORT = 80        # Port to listen on
    print(HOST,PORT)

# check GP0 for setup mode
# see setup mode for instructions
progStatus = False
progStatusPin = digitalio.DigitalInOut(IO35)
progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
progStatus = not progStatusPin.value

if(progStatus == False):
    # not in setup mode, inject the payload
    print("Starting Wifi")
    startWiFi()
    print("Starting Web Service")
    startWebService()

    print("Done")
else:
    print("Update your payload")
