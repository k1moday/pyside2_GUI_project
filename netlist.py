import numpy as np
from PySide2.QtWidgets import QFileDialog


class NetList:
    # 网表文件格式应为每个元器件的所有信息单独一行
    def __init__(self):
        self.names = []
        self.mapMatrix = np.zeros((0, 0), dtype=int)

    def makeNetMap(self):
        path, _ = QFileDialog.getOpenFileName()
        f = open(path, 'r')
        temps = f.readlines()
        n = len(temps)
        net2node = {}
        node2net = {}
        for index in range(len(temps)):
            temp = temps[index]
            words = temp.split()
            theNames = words[0].split('.')
            theName = theNames[1]
            self.names.append(theName)
            lNet = words[1].split(':')[1]
            rNet = words[2].split(':')[1]
            neighbourNets = [lNet, rNet]
            if 'mos' in theName:
                mNet = words[3].split(':')[1]
                neighbourNets = [lNet, rNet, mNet]
                if net2node.__contains__(mNet):
                    tempV = net2node.get(mNet)
                    tempV.append(index)
                    net2node[mNet] = tempV
                else:
                    tempV = [index]
                    net2node[mNet] = tempV

            node2net[theName] = neighbourNets
            if net2node.__contains__(lNet):
                tempV = net2node.get(lNet)
                tempV.append(index)
                net2node[lNet] = tempV
            else:
                tempV = [index]
                net2node[lNet] = tempV

            if net2node.__contains__(rNet):
                tempV = net2node.get(rNet)
                tempV.append(index)
                net2node[rNet] = tempV
            else:
                tempV = [index]
                net2node[rNet] = tempV

        self.mapMatrix = np.zeros((n, n), dtype=int)
        for i in range(n):
            nodeName = self.names[i]
            nets = node2net[nodeName]
            lNet = nets[0]
            rNet = nets[1]
            lNet2Nodes = net2node[lNet]
            rNet2Nodes = net2node[rNet]
            for index in range(len(lNet2Nodes)):
                self.mapMatrix[i][lNet2Nodes[index]] = 1
            for index in range(len(rNet2Nodes)):
                self.mapMatrix[i][rNet2Nodes[index]] = 1
            if 'mos' in nodeName:
                mNet = nets[2]
                mNet2Nodes = net2node[mNet]
                for index in range(len(mNet2Nodes)):
                    self.mapMatrix[index][mNet2Nodes[index]] = 1

        # for i in range(n):
        #     for j in range(n):
        #         print(self.mapMatrix[i][j], end=" ")
        #     print()

    def getNames(self):
        return self.names

    def getNetMap(self):
        return self.mapMatrix
