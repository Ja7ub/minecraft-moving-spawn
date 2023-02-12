from mcipc.rcon.je import Biome, Client     # For Java Edition servers.
#from mcipc.rcon.be import Client           # For Bedrock Edition servers.
#from mcipc.rcon.ee import Client           # For Education Edition servers.

import math

ANGLE_FILENAME = "last_angle.txt"

# this is periodically run every minute
def move_spawn():
    with open(ANGLE_FILENAME) as f:
        current_angle = float(f.readline())

    print(f"Current angle loaded: {current_angle}")

    circle_center = (-874, 1444) # x, z
    circle_radius = 1010 # blocks
    rotation_speed = 6 # deg/min


    new_angle = current_angle + rotation_speed

    r = circle_radius
    x_ctr = circle_center[0]
    z_ctr = circle_center[1]
    t = math.radians(new_angle)

    x = r * math.cos(t)  + x_ctr
    z = r * math.sin(t)  + z_ctr
    y = 65 # uvidíme, jak se to popasuje s horami

    x = int(x)
    z = int(z)

    if(new_angle>360):
        new_angle = new_angle - 360
    with open(ANGLE_FILENAME, 'w') as file:
        file.write(f"{new_angle}")

    msg = f"World spawn moved to: {x}, {y}, {z}."
    print(msg)

    return x, y, z, msg


if __name__ == "__main__":
    with Client('127.0.0.1', 25575, passwd='') as client:
        pass
        #seed = client.seed                              # Get the server's seed.
        #players = client.list()                         # Get the server's players info.
        #mansion = client.locate('mansion')              # Get the next mansion's location.
        #badlands = client.locatebiome(Biome.BADLANDS)   # Get the next location of a badlands biome.

        x, y, z, msg = move_spawn()
        client.setworldspawn((x, y, z))
        client.say(msg)




    #print(seed)
    #print(players)
    #print(mansion)
    #print(badlands)
