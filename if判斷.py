from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    a=mc.getBlock(x,y,z)
    b=mc.getBlock(x+1,y,z)
    c=mc.getBlock(x,y,z-1)
    d=mc.getBlock(x,y,z+1)
    if a==9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)