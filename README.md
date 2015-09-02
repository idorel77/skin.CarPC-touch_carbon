skin.CarPC-touch_carbon
=======================

skin_xbmc
Update 2.09.2015
- Fixed file manager and add button in home.

- update 27-09-20015
- added new page for connecting 3g. If you don't need -> Hide button from - Settings/Skin settings/settings buttons/
- This working only with sakis3g
- The buttons send commands :
- sudo /usr/bin/modem3g/sakis3g connect
- sudo /usr/bin/modem3g/sakis3g disconnect

- For install sakis3g 
- wget "http://raspberry-at-home.com/files/sakis3g.tar.gz"
- I suggest you copy the file to /usr/bin/modem3g directory and unpack it:

- sudo mkdir /usr/bin/modem3g
- sudo chmod 777 /usr/bin/modem3g
- sudo cp sakis3g.tar.gz /usr/bin/modem3g
- cd /usr/bin/modem3g
- sudo tar -zxvf sakis3g.tar.gz
- sudo chmod +x sakis3g

- Config: (This is my config ,i use Huawei E3131)
- sudo nano /etc/sakis3g.conf
- Add:
- APN="internet"
MODEM="OTHER"
OTHER="USBMODEM"
USBINTERFACE="0"
USBDRIVER="option"
USBMODEM="12d1:1506"
APN_USER="foo"
APN_PASS="foo"

- More info: http://raspberry-at-home.com/installing-3g-modem/
