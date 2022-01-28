import mosaik
import mosaik.util

from Charge import Charge

# Sim config. and other parameters
SIM_CONFIG = {
    'LEDSimulator': {
        'python': 'LEDSimulator:LEDSimulator',
    },
    'PinSimulator': {
        'python': 'PinSimulator:PinSimulator'
    },
}

END = 10  # 10 seconds

# Create World
world = mosaik.World(SIM_CONFIG)

led_factory = world.start('LEDSimulator')
pin_factory = world.start('PinSimulator')

led_matrix = []

for _ in range(3):
    led_matrix.append(led_factory.LED.create(3))

x_pin_values = [0, 1, 1]
y_pin_values = [0, 0, 1]

x_pins = []
y_pins = []

for v in x_pin_values:
    x_pins.append(pin_factory.Pin(init_charge=Charge(v)))

for v in y_pin_values:
    y_pins.append(pin_factory.Pin(init_charge=Charge(v)))


for i in range(len(y_pins)):
    for j in range(len(led_matrix[i])):
        world.connect(y_pins[i], led_matrix[i][j], ('charge', 'K'))

for i in range(len(x_pins)):
    for j in range(len(led_matrix)):
        world.connect(x_pins[i], led_matrix[j][i], ('charge', 'A'))


world.run(until=END)