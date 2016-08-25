import matplotlib.pyplot as plt

lines = open("count.txt").readlines()

a=map(lambda x:x.split()[0],lines)

b=map(lambda x:x.split()[1],lines)

c=map(lambda x:x.split()[2],lines)

plt.figure();[x,y]=[0,len(c)];plt.plot(a[x:y],c[x:y]);plt.title("Word count: "+str(a[x])+"~"+str(a[y-1]));plt.xlabel("Word Count");plt.ylabel("Accumulated Frequency");plt.savefig("allcount.png")

plt.figure();[x,y]=[0,50];plt.plot(a[x:y],c[x:y]);plt.title("Word count: "+str(a[x])+"~"+str(a[y]));plt.xlabel("Word Count");plt.ylabel("Accumulated Frequency");plt.savefig(str(a[x])+"to"+str(a[y])+".png")

plt.figure();[x,y]=[50,500];plt.plot(a[x:y],c[x:y]);plt.title("Word count: "+str(a[x])+"~"+str(a[y]));plt.xlabel("Word Count");plt.ylabel("Accumulated Frequency");plt.savefig(str(a[x])+"to"+str(a[y])+".png")

plt.figure();[x,y]=[500,900];plt.plot(a[x:y],c[x:y]);plt.title("Word count: "+str(a[x])+"~"+str(a[y]));plt.xlabel("Word Count");plt.ylabel("Accumulated Frequency");plt.savefig(str(a[x])+"to"+str(a[y])+".png")

plt.figure();[x,y]=[900,len(c)];plt.plot(a[x:y],c[x:y]);plt.title("Word count: "+str(a[x])+"~"+str(a[y-1]));plt.xlabel("Word Count");plt.ylabel("Accumulated Frequency");plt.savefig(str(a[x])+"torest.png")


