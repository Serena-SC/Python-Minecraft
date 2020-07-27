from mcpi.minecraft import Minecraft
import time   
mc=Minecraft.create()
x=254
y=541
z=821
print(mc.player.getTilePos())
time.sleep(5)
mc.player.setTilePos(-349,135,205)
time.sleep(5)
mc.player.setTilePos(-333,111,222)
time.sleep(5)
mc.player.setTilePos(-344,122,288)
print(mc.player.getTilePos())
time.sleep(5)
mc.player.setTilePos(-x,y,z)

