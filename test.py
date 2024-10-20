import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class ImpulseWaveAnalyzer:
    def __init__(self, low_price, high_price, duration_days):
        self.low_price = low_price
        self.high_price = high_price
        self.duration_days = duration_days
        self.price_diff = high_price - low_price
        self.multiples = [1, 1.25, 1.5, 1.75, 2, 2.5, 3]
        self.fib_ratios = [1, 1.382, 1.618, 2.618]

    def calculate_projections(self):
        price_projections = [self.low_price + self.price_diff * m for m in self.multiples + self.fib_ratios]
        time_projections = [self.duration_days * m for m in self.multiples + self.fib_ratios]
        return price_projections, time_projections

    def construct_growth_squares(self):
        price_proj, time_proj = self.calculate_projections()
        squares = []
        for p in price_proj:
            for t in time_proj:
                squares.append((p, t))
        return squares

    def analyze_turning_points(self):
        squares = self.construct_growth_squares()
        turning_points = []
        for price, time in squares:
            if any(abs(price - p) < 0.01 * self.price_diff and abs(time - t) < 0.01 * self.duration_days 
                   for p, t in squares if (p, t) != (price, time)):
                turning_points.append((price, time))
        return turning_points

    def generate_report(self):
        price_proj, time_proj = self.calculate_projections()
        turning_points = self.analyze_turning_points()
        
        report = f"Impulse Wave Analysis Report\n"
        report += f"Initial low: ${self.low_price:.2f}\n"
        report += f"First wave high: ${self.high_price:.2f}\n"
        report += f"Duration: {self.duration_days} trading days\n\n"
        
        report += "Price Projections:\n"
        for i, price in enumerate(price_proj):
            report += f"  Level {i+1}: ${price:.2f}\n"
        
        report += "\nTime Projections (trading days):\n"
        for i, time in enumerate(time_proj):
            report += f"  Level {i+1}: {time:.0f} days\n"
        
        report += "\nPotential Turning Points (Price, Time):\n"
        for price, time in turning_points:
            report += f"  ${price:.2f}, {time:.0f} days\n"
        
        return report

    def plot_analysis(self):
        price_proj, time_proj = self.calculate_projections()
        turning_points = self.analyze_turning_points()
        
        plt.figure(figsize=(12, 8))
        plt.scatter(time_proj, price_proj, color='blue', label='Projections')
        plt.scatter([t for _, t in turning_points], [p for p, _ in turning_points], color='red', label='Turning Points')
        plt.plot([0, self.duration_days], [self.low_price, self.high_price], 'g-', label='Initial Impulse')
        plt.xlabel('Time (trading days)')
        plt.ylabel('Price ($)')
        plt.title('Impulse Wave Analysis')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
analyzer = ImpulseWaveAnalyzer(low_price=25.42, high_price=80, duration_days=104)
print(analyzer.generate_report())
analyzer.plot_analysis()