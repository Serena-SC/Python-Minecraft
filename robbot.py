from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
try:
    blockType = int(input("請輸入要放的方塊ID:"))
    mc.setBlock(x, y, z, blockType)
except:
    print("只能輸入數字!!!!!!")
    mc.postToChat("只能輸入數字!!!!!!")