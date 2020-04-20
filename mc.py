# This script is a great starting point to get the Minecraft API
# working with the oc-miner server.  Just insert this code into
# your own project to get a started.
#
# One thing you need to do is set your username below, inside the quotes.
# Your username appears on the Minecraft Launcher, if you don't remember it.
# It is case-senstive, so type it carefully.
username = "type-username-here"
#
# Go here to learn about the Minecraft API functions.
# https://www.stuffaboutcode.com/p/minecraft-api-reference.html
# Go here to see a full list of the block IDs.
# https://minecraft-ids.grahamedgecombe.com/

from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
from mcpi import block

# Connect to our Minecraft server.  NOTE: Before this will work, Steve will
# need to add your username to the server.
mc = Minecraft.create('oc-miner.duckdns.org')

# Get your unique identifer from the server.  This changes every time you login.
id = mc.getPlayerEntityId(username)

# Get the your current position in the world.
pos = mc.entity.getTilePos(id)
print("Welcome to the Minecraft API {}.  id: {} position: {}".format(username,id,pos))

# Let everyone on the server know you are here.
mc.postToChat("{} has joined with MCPI".format(username))

# Add you own code below
