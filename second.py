# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:17:13 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(5)

x = -13
y = 16
z = 8

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)