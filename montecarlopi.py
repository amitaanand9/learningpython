import random
import pandas as pd
import matplotlib.pyplot as plt
import statistics
interval = 1000
circlepoints = 0
outsidepoints = 0

estimates = []

for i in range(interval):
    randx = random.uniform(0,1)
    randy = random.uniform(0,1)
    if (randx**2 + randy**2 <= 1):
        circlepoints = circlepoints + 1
    
    outsidepoints = outsidepoints + 1
    pi = 4 * (circlepoints/outsidepoints)
    estimates.append(pi)

print(estimates[0:10])
s = pd.DataFrame(estimates)
print(s.head)
mean = statistics.mean(estimates)
sd = statistics.stdev(estimates)
plt.hist(estimates, bins = 50, rwidth=0.5, range=(2,4.5))

min_ylim, max_ylim = plt.ylim()

#plot mean line
plt.axvline(mean, color='k', linestyle='dotted', linewidth=1)
plt.text(mean, max_ylim*0.9, 'Mean: {:.2f}'.format(mean))

#plot first standard deviation
sd1 = mean + sd
sd2 = mean - sd
plt.axvline(sd1, color='k', linestyle='dotted', linewidth=1)
plt.axvline(sd2, color='k', linestyle='dotted', linewidth=1)
plt.text(sd1, max_ylim*0.8, 'Standard Deviation 1: {:.2f}'.format(sd1))

#plot second standard deviation
sd3 = mean + 2*sd
sd4 = mean - 2*sd
plt.axvline(sd3, color='k', linestyle='dotted', linewidth=1)
plt.axvline(sd4, color='k', linestyle='dotted', linewidth=1)
plt.text(sd3, max_ylim*0.7, 'Standard Deviation 2: {:.2f}'.format(sd3))

#plot third standard deviation
sd5 = mean + 3*sd
sd6 = mean - 3*sd
plt.axvline(sd5, color='k', linestyle='dotted', linewidth=1)
plt.axvline(sd6, color='k', linestyle='dotted', linewidth=1)
plt.text(sd5, max_ylim*0.6, 'Standard Deviation 3: {:.2f}'.format(sd5))
plt.show()
print(sd)







