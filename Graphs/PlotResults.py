import matplotlib.pyplot as plt
import numpy as np
import math
plt.style.use("seaborn-deep")


with open("RB/PerformanceAverageCase.txt", 'r') as f:
    lines = f.readlines()

averageVectorRB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        averageVectorRB[j] += float(vector[j])/10

xpointsAverageRB = np.array([x for x in range(0, len(averageVectorRB))])
ypointsAverageRB = np.array(averageVectorRB)

plt.xticks(range(0, len(xpointsAverageRB)+1, 100))
plt.plot(xpointsAverageRB, ypointsAverageRB, label="Average (Red-Black)", linewidth=0.7)
f.close()

#(3) Gráfico do pior caso da árvore Rubro-Negra:


with open("RB/PerformanceWorstCase.txt", 'r') as f:
    lines = f.readlines()

worstVectorRB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        worstVectorRB[j] = float(vector[j])

xpointsWorstRB = np.array([x for x in range(0, len(worstVectorRB))])
ypointsWorstRB = np.array(worstVectorRB)

plt.plot(xpointsWorstRB, ypointsWorstRB, label="Worst (Red-Black)", linewidth=0.7)

plt.title("Average Case vs Worst Case")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig("Graphs/RB.png")
plt.close()
f.close()

#(4) Gráfico do caso médio da árvore AVL:
with open("AVL/PerformanceAverageCase.txt", 'r') as f:
  lines = f.readlines()
averageVectorAVL = [0 for i in range(len(lines[0].split()))]
for line in lines:
   vector = line.split()
   for j in range(len(vector)):
       averageVectorAVL[j] += float(vector[j])/10
xpointsAverageAVL = np.array([x for x in range(0, len(averageVectorAVL))])
ypointsAverageAVL = np.array(averageVectorAVL)
plt.plot(xpointsAverageAVL, ypointsAverageAVL, label="Average (AVL)", linewidth=0.7)
f.close()

# (5) Gráfico do pior caso da árvore AVL:

with open("AVL/PerformanceWorstCase.txt", 'r') as f:
    lines = f.readlines()

worstVectorAVL = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        worstVectorAVL[j] = float(vector[j])

xpointsWorstAVL = np.array([x for x in range(0, len(worstVectorAVL))])
ypointsWorstAVL = np.array(worstVectorAVL)

plt.plot(xpointsWorstAVL, ypointsWorstAVL, label="Worst (AVL)", linewidth=0.7)

plt.title("Average Case vs Worst Case")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig("Graphs/AVLTree.png")
plt.close()
f.close()

# (6) Gráfico do caso médio da árvore B:

with open( "B/PerformanceAverageCase1.txt", 'r') as f:
    lines = f.readlines()

averageVectorB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        averageVectorB[j] += float(vector[j])/10

xpointsAverageB1 = np.array([x for x in range(0, len(averageVectorB))])
ypointsAverageB1 = np.array(averageVectorB)

plt.plot(xpointsAverageB1, ypointsAverageB1, label="Average (B)1", linewidth=0.7)
f.close()
with open( "B/PerformanceWorstCase1.txt", 'r') as f:
    lines = f.readlines()

worstVectorB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        worstVectorB[j] = float(vector[j])

xpointsWorstB1 = np.array([x for x in range(0, len(worstVectorB))])
ypointsWorstB1 = np.array(worstVectorB)

plt.plot(xpointsWorstB1, ypointsWorstB1, label="Worst (B)1", linewidth=0.7)

plt.title("Average Case vs Worst Case")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig( "Graphs/B1.png")
plt.close()
f.close()
with open( "B/PerformanceAverageCase5.txt", 'r') as f:
    lines = f.readlines()

averageVectorB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        averageVectorB[j] += float(vector[j])/10

xpointsAverageB5 = np.array([x for x in range(0, len(averageVectorB))])
ypointsAverageB5 = np.array(averageVectorB)

plt.plot(xpointsAverageB5, ypointsAverageB5, label="Average (B)5", linewidth=0.7)
f.close()
with open( "B/PerformanceWorstCase5.txt", 'r') as f:
    lines = f.readlines()

worstVectorB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        worstVectorB[j] = float(vector[j])

xpointsWorstB5 = np.array([x for x in range(0, len(worstVectorB))])
ypointsWorstB5 = np.array(worstVectorB)

plt.plot(xpointsWorstB5, ypointsWorstB5, label="Worst (B)5", linewidth=0.7)

plt.title("Average Case vs Worst Case")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig( "Graphs/B5.png")
plt.close()
f.close()
with open( "B/PerformanceAverageCase10.txt", 'r') as f:
    lines = f.readlines()

averageVectorB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        averageVectorB[j] += float(vector[j])/10

xpointsAverageB10 = np.array([x for x in range(0, len(averageVectorB))])
ypointsAverageB10 = np.array(averageVectorB)

plt.plot(xpointsAverageB10, ypointsAverageB10, label="Average (B)", linewidth=0.7)
f.close()
with open( "B/PerformanceWorstCase10.txt", 'r') as f:
    lines = f.readlines()

worstVectorB = [0 for i in range(len(lines[0].split()))]

for line in lines:
    vector = line.split()
    for j in range(len(vector)):
        worstVectorB[j] = float(vector[j])

xpointsWorstB10 = np.array([x for x in range(0, len(worstVectorB))])
ypointsWorstB10 = np.array(worstVectorB)

plt.plot(xpointsWorstB10, ypointsWorstB10, label="Worst (B)10", linewidth=0.7)

plt.title("Average Case vs Worst Case")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig( "Graphs/B10.png")
plt.close()
f.close()
# (7) Gráfico do pior caso da árvore B:



# (8) Plotando todos os gráficos em um só:

plt.plot(xpointsAverageRB, ypointsAverageRB,
         label="Average (RB)", linewidth=0.7)
plt.plot(xpointsAverageAVL, ypointsAverageAVL,
         label="Average (AVL)", linewidth=0.7)
plt.plot(xpointsAverageB1, ypointsAverageB1, label="Average (B)1", linewidth=0.7)
plt.plot(xpointsAverageB5, ypointsAverageB5, label="Average (B)5", linewidth=0.7)
plt.plot(xpointsAverageB10, ypointsAverageB10, label="Average (B)10", linewidth=0.7)

plt.title("Average Cases")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig( "Graphs/AllTreesAverage.png")
plt.close()

plt.plot(xpointsWorstRB, ypointsWorstRB, label="Worst (RB)", linewidth=0.7)
plt.plot(xpointsWorstAVL, ypointsWorstAVL, label="Worst (AVL)", linewidth=0.7)
plt.plot(xpointsWorstB1, ypointsWorstB1, label="Worst (B)1", linewidth=0.7)
plt.plot(xpointsWorstB5, ypointsWorstB5, label="Worst (B)5", linewidth=0.7)
plt.plot(xpointsWorstB10, ypointsWorstB10, label="Worst (B)10", linewidth=0.7)

plt.title("Worst Cases")
plt.xlabel("Elementos na árvore")
plt.ylabel("Operações")
plt.legend(loc="upper left")
plt.savefig( "Graphs/AllTreesWorst.png")
plt.close()

