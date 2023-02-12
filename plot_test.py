import matplotlib.pyplot as plt
from test_rcon import *


with open(ANGLE_FILENAME, 'w') as file:
        file.write(f"0.0")

for i in range(60):    
    x, y, z = move_spawn()

    #plt.plot([x,z])
    plt.scatter(x, z)

plt.show()
