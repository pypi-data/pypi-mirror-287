
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import datetime
cmp_hjnwtx={}

newcolorsNMC = np.array([
    [68,157,237, 255],
    [98,230,234, 255],
    [104,249,82, 255],
    [0,215,46, 255],
    [0,143,27, 255],
    [254,254,63, 255],
    [231,192,48, 255],
    [255,154,41, 255],
    [255,19,27, 255],
    [215,14,21, 255],
    [193,11,18, 255],
    [255,28,236, 255],
    [152,15,177, 255],
    [175,145,237, 255]])/255
cmp_hjnwtx["radar_nmc"] = ListedColormap(newcolorsNMC)

newcolorsNMC = np.array([
    [68,157,237, 255],
    [98,230,234, 255],
    [104,249,82, 255],
    [0,215,46, 255],
    [0,143,27, 255],
    [254,254,63, 255],
    [231,192,48, 255],
    [255,154,41, 255],
    [255,19,27, 255],
    [215,14,21, 255],
    [193,11,18, 255],
    [255,28,236, 255],
    [152,15,177, 255],
    [175,145,237, 255]])/255
cmp_hjnwtx["radar_moc"] = ListedColormap(newcolorsNMC)


newcolorsPRE = np.array([
    [128, 255, 255, 255],
    [35, 182, 254, 255],
    [0, 120, 180, 255],
    [0, 82, 202, 255],
    [0, 16, 220, 255],
    [150, 2, 244, 255],
    [110, 0, 182, 255],
    [77, 0, 130, 255]])/255
cmp_hjnwtx["pre_tqw"] = ListedColormap(newcolorsPRE)

newcolorsWS = np.array([
    [75, 140, 244, 255],
    [0, 89, 235, 255],
    [36, 173, 0, 255],
    [18, 129, 1, 255],
    [3, 64, 4, 255],
    [218, 183, 5, 255],
    [179, 125, 1, 255],
    [155, 70, 16, 255],
    [253, 3, 127, 255],
    [255, 0, 55, 255],
    [233, 0, 3, 255]])/255
cmp_hjnwtx["ws_nmic"] = ListedColormap(newcolorsWS)

import os
def mkDir(path):
    if "." in path:
        os.makedirs(os.path.dirname(path),exist_ok=True)
    else:
        os.makedirs(path, exist_ok=True)

def Radar_Nmc(array_dt,temp = "850"):
    now_str = datetime.datetime.now().strftime("%Y%m%d%H%M")
    if len(array_dt.shape)==3:
        for i , img_ch_nel in enumerate(array_dt): 
            plt.imshow(img_ch_nel,vmin=0,vmax=100,cmap=cmp_hjnwtx["radar_nmc"])
            plt.colorbar()
            outpath = f"./radar_nmc/{temp}_{now_str}.png"
            mkDir(outpath)
            plt.savefig(outpath)
            plt.close()
    if len(array_dt.shape)==2:
            plt.imshow(array_dt,vmin=0,vmax=100,cmap=cmp_hjnwtx["radar_nmc"])
            plt.colorbar()
            outpath = f"./radar_nmc/{temp}_{now_str}.png"
            mkDir(outpath)
            plt.savefig(outpath)
            plt.close() 
            