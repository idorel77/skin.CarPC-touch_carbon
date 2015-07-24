import os
import xbmc


os.system("git clone https://github.com/idorel77/skin.CarPC-touch_carbon");
print "Download done"
os.system("rsync -avz -e skin.CarPC-touch_carbon/ /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
print "Sync done"
xbmc.executebuiltin('ReloadSkin()');
