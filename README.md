<h1 align="center">feathers2-ducky</h1>

<div align="center">
  <strong>Make a powerful USB Rubber Ducky with a FeatherS2 board</strong>
</div>

<br />

<div align="center">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/dbisu/feathers2-ducky">
  <img alt="GitHub license" src="https://img.shields.io/github/license/dbisu/feathers2-ducky">
  <a href="https://github.com/dbisu/pico-ducky/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/dbisu/feathers2-ducky"></a>
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/dbisu/featherse-ducky">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/dbisu/feathers2-ducky">
</div>

<br />

## Install

Install and have your USB Rubber Ducky working in less than 5 minutes.

1. Download [CircuitPython for the FeatherS2](https://circuitpython.org/board/unexpectedmaker_feathers2/). Currently versin 7.0.0

2. Plug the device into a USB port. Press the Reset button, then within a second it the boot button. It will show up as a removable media device named `UFTHRS2BOOT`.

3. Copy the downloaded `.uf2` file to the root of the Pico (`RPI-RP2`). The device will reboot and after a second or so, it will reconnect as `CIRCUITPY`.

4. Download `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip` [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) and extract it outside the device.

5. Navigate to `lib` in the recently extracted folder and copy `adafruit_hid` to the `lib` folder on your FeatherS2.

6. Also from `lib`, copy adafruit_wsgi to the `lib` folder on  your FeatherS2.

7. Connect pin IO35 (`IO35`) to pin 4 (`GND`).  This will enable setup mode once the files are copied to the FeatherS2.

8. Download boot.py, code.py, ducyinpython.py, webapp.py, and wsgserver.py.

9. Download `adafruit_wsgi/wsgi_app.py` and copy to `lib/adafruit_wsgi` on the FeatherS2.  Remove `wsgi_app.mpy` from that folder.

10. Copy boot.py, code.py, ducyinpython.py, webapp.py, and wsgserver.py to the root of the FeatherS2.

11. Find a script [here](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads) or [create your own one using Ducky Script](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript) and save it as `payload.dd` on the FeatherS2.

12. Create the file `secrets.py` in the root of the FeatherS2.  This contains the AP name and password to be created by the FeatherS2.   
`secrets = {
    'ssid' : "BadAPName",
    'password' : "badpassword"
}`

13. Unplug the FeatherS2, remove the jumper from `IO35`, and plug back in your FeatherS2.

14. The FeatherS2 should reboot into AP mode, serving from the address of `http://192.168.4.1`

15. Navigating to `http://192.168.4.1` should list out the available payloads.  You can run the scripts from the menus.

## Notes

Editing scripts is currently broken.  To be fixed soon.

### Setup mode

To edit the payload, enter setup mode by connecting the pin IO35 (`IO35`) to pin 4 (`GND`), this will stop the feathers2-ducky from starting the Wifi and will reenable USB drive function.
The easiest way to so is by using a jumper wire between those pins.

![FeatherS2 pinout](https://feathers2.io/images/feathers2_pinout_extended2.jpg)


### Changing Keyboard Layouts

See the [Wiki](https://github.com/dbisu/feathers2-ducky/wiki)

## Useful links and resources

### Docs

[CircuitPython](https://circuitpython.readthedocs.io/en/6.3.x/README.html)

[CircuitPython HID](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

[Ducky Script](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript)

### Video tutorials

[pico-ducky tutorial by **NetworkChuck**](https://www.youtube.com/watch?v=e_f9p-_JWZw)

[USB Rubber Ducky playlist by **Hak5**](https://www.youtube.com/playlist?list=PLW5y1tjAOzI0YaJslcjcI4zKI366tMBYk)

[CircuitPython tutorial on the Raspberry Pi Pico by **DroneBot Workshop**](https://www.youtube.com/watch?v=07vG-_CcDG0)
