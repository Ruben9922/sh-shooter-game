from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

BACKGROUND_COLOUR = [40, 40, 40]

sense.clear(BACKGROUND_COLOUR)
sleep(5)

sense.clear()
sense.low_light = False
