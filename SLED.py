
# Super Led: Led that has n inpus which all have to be true in order to glow
class SLED:
    def __init__(self) -> None:
        self.inputs = []
        self.glowing = False

    def step(self):
        self.glowing = all(self.inputs)
        if self.glowing:
            print("LED is currently glowing")


if __name__ == "__main__":#
    l = SLED()
    l.inputs = [True, True, True, True]
    l.step()
    print(l.glowing)
