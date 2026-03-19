#Ornstein-Uhlenbeck Process (Mean-Reverting Model)
#St+1​=St​+θ(μ−St​)Δt+σΔt​Zt

import math
import random
import numpy as np
import matplotlib.pyplot as plt

#Parameters
num_stocks = int(input("No. of Stocks: "))
num_days = int(input("No. of Days to simulate: "))
initial_price= float(input("Initial Stock Price: "))
volatility = float(input("Daily volatility (in %): "))/100
bubble_growth = float(input("Bubble growth (in %): "))/100
bubble_prob = float(input("Bubble Probability (in %): "))/100
burst_prob = float(input("Burst probability (in %): "))/100
burst_drop = float(input("Burst drop (in %): "))/100
mu = float(input("Long-term mean price: "))
theta = float(input("Mean reversion speed: "))

#Initializing
all_prices = []
for i in range(num_stocks):
    all_prices.append([initial_price])
#Bubble Flags
bubble_flags = []
for i in range(num_stocks):
    bubble_flags.append(False)

#Simulation
for day in range(1, num_days+1): #loop on days
    for stock in range(num_stocks): #loop on stocks
        z = random.gauss(0,1)
        last_price = all_prices[stock][-1]
        new_price = last_price + theta*(mu - last_price) + volatility*z
        #Bubble Start
        if not bubble_flags[stock]:
            if random.random() < bubble_prob: #random.random() gives random choice of a floating point in (0,1)
                bubble_flags[stock] = True 
        #Bubble Growth
        if bubble_flags[stock]:
            new_price += new_price * bubble_growth
        #Bubble Burst
        if bubble_flags[stock]:
            if random.random() < burst_prob:
                new_price = new_price*(1 - burst_drop)
                bubble_flags[stock] = False 
        #List new prices
        all_prices[stock].append(new_price)
for i in range(num_stocks):
    print(f"Stock{i+1} Prices: ")
    print(all_prices[i])

#Plotting
for stock in range(num_stocks):
    plt.plot(all_prices[stock], label = f'Stock {stock + 1}')
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Simulated Stocks with Bubble")
plt.legend()
plt.show()
print(bubble_flags)
