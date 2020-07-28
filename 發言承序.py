from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = input('Your Name?')
message = input("message")
mc.postToChat("["+name+"]: "+message)