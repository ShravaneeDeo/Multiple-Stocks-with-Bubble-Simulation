#Jump Diffusion 
#St+1​=St​⋅exp(μΔt+σΔtZt​)⋅Jt​

import random
import math 
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
drift = float(input("Drift (in %): "))/100
jump_prob = float(input("Jump Probability (in %): "))/100
jump_size = float(input("Jump Size (in %): "))/100


#Initializing
#Listing all the prices of all stocks
all_prices = []
for i in range(num_stocks):
    all_prices.append([initial_price])

#Simulation
for day in range(1, num_days +1): #loop on days
    for stock in range(num_stocks): #loop on stocks
        z = random.gauss(0,1)
        last_price = all_prices[stock][-1]
        new_price = last_price*math.exp(drift + volatility*z)
        if random.random() < jump_prob:
            jump_direction = random.choice([-1,1]) #rare jump happens
            new_price = new_price*(1 + jump_size*jump_direction)  
        
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
