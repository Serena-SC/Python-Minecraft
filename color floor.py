from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
from time import sleep
for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for j in range(10):
        color = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,color)

ans = randrange(0,16)
t=0
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data ==ans:
            mc.postToChat("恭喜你找到我!")
            mc.setBlock(hit.pos,57)
            break
        elif data<ans:
            mc.postToChat("Try Bigger")
        elif data>ans:
            mc.postToChat("Try Smaller")
        t = t+1
        if t>5:
            mc.postToChat("猜太多次了~~~~~~~~快逃!!")
            sleep(3)
            x,y,z = mc.player.getTilePos()
            mc.createExplosion(x,y,z)
            break