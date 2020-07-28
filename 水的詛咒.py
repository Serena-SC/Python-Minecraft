from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    time.sleep(1)