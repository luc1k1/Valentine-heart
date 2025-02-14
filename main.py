import numpy as np
import matplotlib.pyplot as plt

def heart_function(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y


t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_function(t)


plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red', linewidth=3)
plt.fill(x, y, 'red', alpha=0.6)


plt.text(0, -2, "Happy Valentine's Day!", fontsize=14, color='white',
         ha='center', fontweight='bold', bbox=dict(facecolor='red', edgecolor='none', boxstyle='round,pad=0.5'))


plt.axis('off')
plt.show()
