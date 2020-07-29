from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockHits()
    if len (hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        blockID = mc.getBlock(x,y,z)
        print("恭喜你列到了ID為"+str(blockID)+"的方塊")
        mc.postToChat("恭喜你列到了ID為"+str(blockID)+"的方塊")