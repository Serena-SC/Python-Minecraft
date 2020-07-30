from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getPos()
for i in range(10):
    r = random.randrange(1,5)
  
    if r==1:
        mc.setBlocks(x,y,z,x,y+1,z+4,41)
        z = z+4
    elif r==2:
        mc.setBlocks(x,y,z,x,y-1,z-4,41)
        z = z-4
    elif r==3:
        mc.setBlocks(x,y,z,x+4,y+1,z,41)
        x = x-4
    else:
        mc.setBlocks(x,y,z,x+4,y-1,z,41)
        x = x+4