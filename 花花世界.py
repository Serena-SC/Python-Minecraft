from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,37)
    time.sleep(0.5)