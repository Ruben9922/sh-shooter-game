from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

background_colour = [40, 40, 40]

sense.clear(background_colour)
sleep(5)

sense.clear()
sense.low_light = False
