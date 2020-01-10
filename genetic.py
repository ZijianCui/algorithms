import random

class EnCoder:
    def __init__(self, min_v, max_v, quantify):
        self.min_v = min_v
        self.quantify = quantify
        self.step = (max_v - min_v) / pow(2, quantify)

    def encode(self, x):
        return bin(int((x-self.min_v)/self.step))[2:].zfill(self.quantify)

    def decode(self, x):
        return self.min_v + int(x, 2) * self.step


class Selector:
    def __init__(self, proportion, encoder, adapt_func):
        self.proportion = proportion
        self.encoder = encoder
        self.adapt_func = adapt_func
        self.scores = []

    class Adaptability:
        def __init__(self, x, encoder, adapt_func):
            self.x = x
            self.score = adapt_func(encoder.decode(x))

    def select(self, xs):
        for x in xs:
            self.scores.append(self.Adaptability(x, self.encoder, self.adapt_func))
        self.scores.sort(key=lambda k: k.score, reverse=True)
        for sc in self.scores:
            print(sc.x, sc.score)


if __name__ == '__main__':
    encoder = EnCoder(0, 30, 18)
    c = []
    for i in range(100):
        c.append(encoder.encode(random.random()*30))
    selector = Selector(0.6, encoder, lambda x: x*x)
    selector.select(c)
