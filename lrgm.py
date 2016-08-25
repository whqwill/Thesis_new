import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

lr=[0.01,0.05,0.1,0.2]
gm=[0.8,0.85,0.9,0.95]
lossLr=[0.2632,0.2485,0.2458,0.2445]
iterLr=[25,30,35,45]
lossGm=[0.2490,0.2476,0.2458,0.2443]
iterGm=[25,30,35,55]

plt.figure(1)

line1, = plt.plot(lr,lossLr, marker='o')

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("The beginning learning rate")
plt.ylabel("The best loss of validation set")
plt.title("The changes of \"vLoss\" over \"lr\"")

plt.savefig("lrloss.png")

plt.figure(2)

line1, = plt.plot(lr,iterLr, marker='o')

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("The beginning learning rate")
plt.ylabel("The total number of training iterations")
plt.title("The changes of \"iter\" over \"lr\"")

plt.savefig("lriter.png")


plt.figure(3)

line1, = plt.plot(gm,lossGm, marker='o')

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("The reduction factor of learning rate")
plt.ylabel("The best loss of validation set")
plt.title("The changes of \"vLoss\" over \"gm\"")

plt.savefig("gmloss.png")

plt.figure(4)

line1, = plt.plot(gm,iterGm, marker='o')

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.xlabel("The reduction factor of learning rate")
plt.ylabel("The total number of training iterations")
plt.title("The changes of \"iter\" over \"gm\"")

plt.savefig("gmiter.png")




