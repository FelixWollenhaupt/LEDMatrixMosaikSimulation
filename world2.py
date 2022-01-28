import mosaik
import mosaik.util
import mosaik.scenario

import numpy as np

from Charge import Charge

# Sim config. and other parameters
SIM_CONFIG = {
    'SLEDSimulator': {
        'python': 'SLEDSimulator:SLEDSimulator',
    },
    'PinSimulator': {
        'python': 'PinSimulator:PinSimulator'
    },
}

END = 10  # 10 seconds

# Create World
world = mosaik.World(SIM_CONFIG)

led_factory = world.start('SLEDSimulator')
pin_factory = world.start('PinSimulator')



pin_values = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
]

sizes = []
for i in pin_values:
    sizes.append(len(i))

pins = []
for dimnesion_values in pin_values:
    dimension_pins = []
    for pin_value in dimnesion_values:
        dimension_pins.append(pin_factory.Pin(init_charge=pin_value))
    pins.append(dimension_pins)


print("hier")
led_matrix = np.ndarray(shape=sizes, dtype=mosaik.scenario.Entity)
print('da')
print(led_matrix.size)

runs = 0

for coordinate, x in np.ndenumerate(led_matrix):
    led_matrix[coordinate] = led_factory.SLED()
    for dim in range(len(sizes)):
        world.connect(pins[dim][coordinate[dim]], led_matrix[coordinate], ('charge', 'inputs'))
    if runs % 100 == 0:
        print(coordinate)

    runs += 1

print("fertich")

world.run(until=END, print_progress=True)
