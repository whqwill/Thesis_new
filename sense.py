# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 3
a = (73168,14636,7630)
b = (73168,21225,1041)
c = (85650,2154, 7630)

ind = np.arange(N)  # the x locations for the groups
width = 0.3       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, a, width, color='r',align='center')
rects2 = ax.bar(ind + width, b, width, color='y',align='center')
rects3 = ax.bar(ind + width*2, c, width, color='b',align='center')

# add some text for labels, title and axes ticks
ax.set_ylabel('The number of words')
ax.set_xlabel('The number of senses')
#ax.set_title('Scores by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels(('1', '2', '3'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('c2=2000, c3=10000', 'c2=2000, c3=100000', 'c2=7000, c3=10000'))
#ax.legend((rects1[0], rects2[0]), ('sense count: 2000_10000', 'sense count: 2000_100000'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.savefig("sensecount.png")
plt.show()
