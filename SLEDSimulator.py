import mosaik_api

from SLED import SLED

META = {
    'type': 'event-based',
    'models': {
        'SLED': {
            'public': True,
            'params': [''],
            'attrs': ['inputs']
        }
    }
}

class SLEDSimulator(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)

        self.eid_prefix = 'SLED_'
        self.entities = {}
        self.time = 0

    def create(self, num, model):
        n_leds = len(self.entities)
        entities = []
        for i in range(n_leds, n_leds + num):
            eid = f"{self.eid_prefix}{i}"
            self.entities[eid] = SLED()
            entities.append({'eid': eid, 'type': model})

        return entities

    def step(self, time, inputs, max_advance):
        self.time = time
    
        for eid, model_instance in self.entities.items():
            if eid in inputs:
                attrs = inputs[eid]
                inp = attrs['inputs'].values()
                model_instance.inputs = inp


            model_instance.step()

        return None

    def get_data(self, outputs):
        return {}