import random
#Parameters
steps = 40
position = 0
print("Random Walk Simulation: ")
print("Step {0} : " , position)
#Simulate random walk 
#Use of iteration to create a loop
for step in range(1, steps + 1):
    move = random.choice([-1,1]) #random choice in {-1, 1}
    position = position + move #update value of position
    print("Step", {step}, " : ", position)



#Simple Stock Price Random Walk
# Goal: Simulate daily price changes of a stock.
# Exercise:
# Start with a stock price of $100.
# Each day (for 15 days), increase or decrease price randomly by ±$1.
# Print the price each day.
# Concepts: Loops, random numbers, updating variables.

St = 100
Days = 15
print("Simple Stock Price Simulation: ")
print("S0 : ", St)
for Day in range(1, Days + 1):
    Change = random.choice([-1,1])
    St = St + Change
    print("S_", Day, " : ", St )

#Random Walk with Plotting (Optional)
# Goal: Visualize randomness.
# Exercise:
# Simulate a random walk for 30 steps.
# Store positions in a list.
# Plot the walk to see the trend.
# Concepts: Lists, loops, random numbers, plotting.    

import random
import matplotlib.pyplot as plt
Days = 30
position = 0
positions = [position]
for Day in range(1, Days + 1):
    Change = random.choice([-1,1])
    position += Change
    positions.append(position)
#Plotting
plt.plot(positions, marker = 'o') #'o' is the marker
plt.xlabel("Day")
plt.ylabel("Position")
plt.title("Random Walk(30 days)")
plt.grid(True)
plt.show() 



