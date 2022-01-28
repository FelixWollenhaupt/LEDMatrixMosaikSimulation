
# Super Led: Led that has n inpus which all have to be true in order to glow
class SLED:
    def __init__(self, coordinate):
        self.inputs = []
        self.coordinate = coordinate
        self.glowing = False

    def step(self):
        self.glowing = all(self.inputs)
        if self.glowing:
            print(f"LED is currently glowing at {self.coordinate}")


if __name__ == "__main__":#
    l = SLED()
    l.inputs = [True, True, True, True]
    l.step()
    print(l.glowing)
