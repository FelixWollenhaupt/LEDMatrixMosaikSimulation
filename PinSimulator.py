import mosaik_api

from Pin import Pin

META = {
    'type': 'time_based',
    'models': {
        'Pin': {
            'public': True,
            'params': ['init_charge'],
            'attrs': ['charge']
        }
    }
}

class PinSimulator(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)
        self.eid_prefix = 'Pin_'
        self.entities = {}
        self.time = 0

    def create(self, num, model, init_charge):
        n_leds = len(self.entities)
        entities = []
        for i in range(n_leds, n_leds + num):
            eid = f"{self.eid_prefix}{i}"
            self.entities[eid] = Pin(init_charge=init_charge)
            entities.append({'eid': eid, 'type': model})

        return entities

    def step(self, time, inputs, max_advance):
        self.time = time
        return None

    def get_data(self, outputs):
        return_data = {}
        return_data['time'] = self.time

        for eid, model_instance in self.entities.items():
            if eid in outputs:
                return_data[eid] = {
                    "charge": model_instance.charge
                }

        return return_data