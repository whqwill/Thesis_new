import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

x=[50,100,150,200,250,300]
t1=[342.9,494.7,502.7,632.5,764.7,947.8]
t2=[34.6,70.1,210,322,533,842]
t3=[683.29,827.30,1069.9,1389.9,1755.7,2272.9]
scws=[0.4666,0.4994,0.5087,0.5103,0.5083,0.5048]
word353=[0.5449,0.5355,0.5319,0.5371,0.5271,0.5233]

plt.figure(1)

line1, = plt.plot(x,t1, marker='o', label='count time')
line2, = plt.plot(x,t2, marker='o', label='treeAggregate time')
line3, = plt.plot(x,t3, marker='o', label='iteration time')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("Embedding Dimension")
plt.ylabel("Time (s)")

plt.savefig("vec_time.png")

plt.figure(2)

line1, = plt.plot(x,scws, marker='o')

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("Embedding Dimension")
plt.ylabel("Spearman-Rank Coefficient")

plt.savefig("vec_SCWS.png")

plt.figure(3)

line1, = plt.plot(x,word353, marker='o')

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("Embedding Dimension")
plt.ylabel("Spearman-Rank Coefficient")

plt.savefig("vec_word353.png")

