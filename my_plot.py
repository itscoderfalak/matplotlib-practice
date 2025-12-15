




import matplotlib.pyplot as plt

# Sample data (plain Python lists)
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
z = [5, 15, 10, 20, 25]
categories = ['A', 'B', 'C', 'D', 'E']
sizes = [20, 30, 25, 15, 10]

# Use a style
plt.style.use('ggplot')

# Create a figure and subplots
fig, axs = plt.subplots(3, 2, figsize=(14, 12))

# ----------------- First subplot: Line plot -----------------
axs[0, 0].plot(x, y, marker='o', label='Line Plot')
axs[0, 0].set_title('Line Plot (OO style)')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].legend()
axs[0, 0].grid(True)
axs[0, 0].set_xlim(0, 6)
axs[0, 0].set_ylim(0, 35)

# ----------------- Second subplot: Scatter plot -----------------
axs[0, 1].scatter(x, z, color='red', label='Scatter')
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Z-axis')
axs[0, 1].legend()
axs[0, 1].grid(True)

# ----------------- Third subplot: Vertical Bar plot -----------------
axs[1, 0].bar(categories, y, color='green', label='Bar Plot')
axs[1, 0].set_title('Vertical Bar Plot')
axs[1, 0].set_xlabel('Categories')
axs[1, 0].set_ylabel('Values')
axs[1, 0].legend()
axs[1, 0].grid(True)

# ----------------- Fourth subplot: Horizontal Bar plot -----------------
axs[1, 1].barh(categories, z, color='orange', label='Horizontal Bar')
axs[1, 1].set_title('Horizontal Bar Plot')
axs[1, 1].set_xlabel('Values')
axs[1, 1].set_ylabel('Categories')
axs[1, 1].legend()
axs[1, 1].grid(True)

# ----------------- Fifth subplot: Histogram -----------------
# Using random numbers with plain Python
import random
data = [random.gauss(0, 1) for _ in range(1000)]
axs[2, 0].hist(data, bins=20, color='purple', edgecolor='black')
axs[2, 0].set_title('Histogram')
axs[2, 0].set_xlabel('Bins')
axs[2, 0].set_ylabel('Frequency')
axs[2, 0].grid(True)

# ----------------- Sixth subplot: Pie chart -----------------
axs[2, 1].pie(sizes, labels=categories, autopct='%1.1f%%', startangle=90)
axs[2, 1].set_title('Pie Chart')

# Adjust layout
plt.tight_layout()

# Show the figure
plt.show()














