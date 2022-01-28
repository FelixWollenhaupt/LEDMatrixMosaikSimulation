import mosaik_api

from LED import LED

META = {
    'type': 'event-based',
    'models': {
        'LED': {
            'public': True,
            'params': [''],
            'attrs': ['A', 'K']
        }
    }
}

class LEDSimulator(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)

        self.eid_prefix = 'LED_'
        self.entities = {}
        self.time = 0

    def create(self, num, model):
        n_leds = len(self.entities)
        entities = []
        for i in range(n_leds, n_leds + num):
            eid = f"{self.eid_prefix}{i}"
            self.entities[eid] = LED()
            entities.append({'eid': eid, 'type': model})

        return entities

    def step(self, time, inputs, max_advance):
        self.time = time
    
        for eid, model_instance in self.entities.items():
            if eid in inputs:
                attrs = inputs[eid]
                a = list(attrs['A'].values())[0]
                k = list(attrs['K'].values())[0]
                model_instance.A = a
                model_instance.K = k

            model_instance.step()

        return None

    def get_data(self, outputs):
        return {}