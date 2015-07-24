import os
import xbmc

os.system("sudo rm -r /home/pi/skin.CarPC-touch_carbon/");
os.system("git clone https://github.com/idorel77/skin.CarPC-touch_carbon");
    print "Download done"
os.system("sudo rm -r /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
os.system("sudo mkdir /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
os.system("rsync -r skin.CarPC-touch_carbon/ /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
    print "Sync done"
xbmc.executebuiltin('ReloadSkin()');
