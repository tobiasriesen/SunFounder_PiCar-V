# Stops the motor in case a program crashes without stopping it
from picar import front_wheels, back_wheels
bw = back_wheels.Back_Wheels()
bw.stop()
