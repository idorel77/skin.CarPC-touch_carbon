import os
import xbmc

xbmc.executebuiltin('XBMC.Quit');
os.system("sudo killall -9 xbmc.bin");
