from  mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
gfdcxc = input(".        .")
mc.setSign(x,y,z,63,0,[gfdcxc])