import math
import matplotlib.pyplot as plt
import numpy as np

class NaturalLog:
    def __init__(self, x: float, eps: float):
        self.x = x
        self.eps = eps
        self.result = {}
        self.result['x'] = x
        self.result['Math F(x)'] = math.log(1 + x)
        self.result['eps'] = eps

    def calculate(self):
        t = self.eps + 1
        n = 1
        sumres = 0.
        sequence = []

        while abs(t) > self.eps:
            t = sumres
            sumres += math.pow(-1, n - 1)*(math.pow(self.x, n)/n)
            n += 1
            t = sumres - t
            sequence.append(sumres)

        self.result['F(x)'] = sumres
        self.result['n'] = n - 1
        self.result['Mean'] = np.mean(sequence)
        self.result['Median'] = np.median(sequence)
        self.result['Mode'] = self.calculate_mode(sequence)
        self.result['Variance'] = np.var(sequence)
        self.result['Standard Deviation'] = np.std(sequence)

    def calculate_mode(self, sequence):
        counts = {}
        for num in sequence:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        max_count = max(counts.values())
        mode = [num for num, count in counts.items() if count == max_count]
        return mode[0] if mode else None

    def plot_graphs(self):
        x_vals = np.linspace(-1, 1, 100)
        self.calculate()  # Calculate the values before plotting
        y_vals = [self.calculate_y_val(x) for x in x_vals]

        plt.plot(x_vals, y_vals, label='Taylor Series')
        plt.plot(x_vals, np.log1p(x_vals), label='Math Function')
        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.legend()
        plt.title('Approximation of Natural Logarithm')
        plt.grid(True)
        plt.annotate(f'n = {self.result["n"]}', xy=(0.5, self.calculate_y_val(0.5)), xytext=(0.2, self.calculate_y_val(0.5)+0.5),
                     arrowprops=dict(facecolor='black', arrowstyle='->'))
        plt.savefig('graph.png')

    def calculate_y_val(self, x):
        n = self.result['n']
        return sum([math.pow(-1, i - 1)*(math.pow(x, i)/i) for i in range(1, n + 1)])

    def get_results(self):
        return self.result