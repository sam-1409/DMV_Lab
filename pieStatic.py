import matplotlib.pyplot as plt
slices = [7, 2, 8, 13]
activities = ['Sleeping', 'Eating', 'Working', 'Playing']
cols = ['c', 'm', 'r', 'b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        autopct='%1.1f%%')
plt.title('My Daily Activities')
plt.show()
