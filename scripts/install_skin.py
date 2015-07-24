import xbmcgui
import time
import os
import socket


xbmcgui.Dialog().notification('Skin', 'Start skin Update', xbmcgui.NOTIFICATION_INFO, 5000)
os.system("sudo rm -r /home/pi/skin.CarPC-touch_carbon/");
xbmcgui.Dialog().notification('Skin', 'Download Update', xbmcgui.NOTIFICATION_INFO, 5000)
os.system("git clone https://github.com/idorel77/skin.CarPC-touch_carbon");
xbmcgui.Dialog().notification('Skin', 'Install Update', xbmcgui.NOTIFICATION_INFO, 5000)
os.system("sudo rm -r /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
os.system("sudo mkdir /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
os.system("sudo rsync -r skin.CarPC-touch_carbon/ /home/pi/.kodi/addons/skin.CarPC-touch_carbon-master/");
xbmcgui.Dialog().notification('Skin', 'Skin Updated', xbmcgui.NOTIFICATION_INFO, 5000)
xbmc.executebuiltin('ReloadSkin()');
