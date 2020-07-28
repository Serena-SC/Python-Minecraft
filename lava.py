from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.player.setPos(x+0.5,y,z+0.5)
mc.setBlock(x,y-1,z,11)