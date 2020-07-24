import math

class Opcao:

    def __init__(self, ticker):
        self.ticker = ticker

    values = {'c':0.0, 'K':0.0, 'r':0.0, 'T':0.0, 'p':0.0, 'So':0.0 }

    def privateimput(self, key):
        return float(input('Digite a variável {}: '.format(key)))

    def get_values(self):
        for c in self.values:
            self.values[c] = self.privateimput(c)

    def ispair(self):
        portfolio_a = self.values['c'] + self.values['K'] * math.exp(self.values['r'] * self.values['T'] * - 1)
        portfolio_b = self.values['p'] + self.values['So']
        print('{:.2f}'.format(portfolio_a), '\n', '{:.2f}'.format(portfolio_b))

        if portfolio_a != portfolio_b:
            return False

        return True
    
