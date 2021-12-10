import matplotlib.pyplot as plt

fi = open("l.l1.i.txt", "r")
data = fi.readlines()
xs = []
ys = []
del data[0]
flag = 1
for line in data:
    line = line.strip('\n')
    temp = line.split()
    if flag == 1:
        xs.append(float(temp[0]))
        ys.append(float(temp[1]))
    flag = (flag + 1) % 2

plt.figure(dpi=800)
plt.scatter(xs, ys, s=0.01)
plt.show()