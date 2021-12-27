# License : GPLv2.0
# copyright (c) 2021  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)


from board import *
import digitalio
import storage

noStorageStatus = False
noStoragePin = digitalio.DigitalInOut(IO35)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = not noStoragePin.value

if(noStorageStatus == False):
    # don't show USB drive to host PC
    storage.disable_usb_drive()
    print("Disabling USB drive")
else:
    # normal boot
    print("USB drive enabled")
