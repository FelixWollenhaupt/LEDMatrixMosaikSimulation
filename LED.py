from Charge import Charge

class LED:
    def __init__(self):
        self.A = Charge.UNDEFINED
        self.K = Charge.UNDEFINED
        self.glowing = False

    def step(self):
        self.glowing = (self.A == Charge.MINUS) and (self.K == Charge.PLUS)
        print("LED is currently {} glowing".format("not" if not self.glowing else ""))




if __name__ == "__main__":
    l1 = LED()

    l1.A = Charge.MINUS
    l1.K = Charge.PLUS

    l1.step()

    print(l1.glowing)