# 使用者：姜海波
# 创建时间：2023/6/1  22:04

'''
# System --> Linux & Python3.8.0
# File ----> slice3.py
# Author --> Illusionna
# Revise --> 2023/09/11 20:51:43
'''
# -*- encoding: utf-8 -*-


if __name__ == '__main__':
    from packages import *
else:
    from utils.packages import *


class GENERATOR:
    """
    生成器：生成孪生网络需要的图片集.
    """
    MODE = Literal['Kmeans', 'GMM', 'SOM', 'NonCluster']
    CATEGORY = Literal['Train', 'Test']

    def __init__(self, data:list, labels:list, rule:MODE, clusterNumber:int, category:CATEGORY, patching:[0,1]=0) -> None:
        self.data = data
        self.labels = labels
        self.rule = rule
        self.numbers = clusterNumber
        self.category = category
        self.patch = patching
        if self.rule == 'NonCluster':
            pass
        else:
            self.predictedLabels = GENERATOR.__LoadLabels(self)

    def Generator(self) -> None:
        if self.rule == 'NonCluster':
            GENERATOR.AlternativeGenerator(self)
        else:
            GENERATOR.Phalanx(self)
            os.makedirs(f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}Positive', exist_ok=True)
            os.makedirs(f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}Negative', exist_ok=True)
            shutil.rmtree(f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}Positive')
            shutil.rmtree(f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}Negative')
            os.makedirs(f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}Positive', exist_ok=True)
            os.makedirs(f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}Negative', exist_ok=True)
            DEFINITION_STATUS = {1:'Positive', 0:'Negative'}
            posP = 1
            posN = 1
            bar = [i for i in range(0, len(self.data), 1)]
            plt.figure()
            stamp = time.time()
            for i in tqdm(bar, desc=f'{self.category} Set', ncols=60,mininterval=1e-5):
                val = self.data[i]
                imageList = deepcopy(self.matrix)
                for s in range(0, len(imageList), 1):
                    for t in range(0, len(imageList[s]), 1):
                        index = imageList[s][t]
                        imageList[s][t] = val[index-1]
                if self.labels[i] == 0:
                    GENERATOR.Paint(
                        self,
                        imageMatrix = imageList,
                        status = DEFINITION_STATUS[0],
                        pos = f'N{posN}'
                    )
                    posN = -~posN
                else:
                    GENERATOR.Paint(
                        self,
                        imageMatrix = imageList,
                        status = DEFINITION_STATUS[1],
                        pos = f'P{posP}'
                    )
                    posP = -~posP
            now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
            print("Charting costs time:")
            print(now)
            print('\n')

    def AlternativeGenerator(self) -> None:
        temp = self.data
        columnNumber = len(self.data[0])
        while(not np.sqrt(columnNumber).is_integer()):
            columnNumber = -~columnNumber
        diff = columnNumber - len(self.data[0])
        for i in range(0, len(self.data), 1):
            tempList = temp[i]
            for j in range(0, diff, 1):
                tempList.append(self.patch)
            temp[i] = tempList
        self.data = temp
        os.makedirs(f'./ChartResults/{self.rule}/{self.category}Positive', exist_ok=True)
        os.makedirs(f'./ChartResults/{self.rule}/{self.category}Negative', exist_ok=True)
        shutil.rmtree(f'./ChartResults/{self.rule}/{self.category}Positive')
        shutil.rmtree(f'./ChartResults/{self.rule}/{self.category}Negative')
        os.makedirs(f'./ChartResults/{self.rule}/{self.category}Positive', exist_ok=True)
        os.makedirs(f'./ChartResults/{self.rule}/{self.category}Negative', exist_ok=True)
        DEFINITION_STATUS = {1:'Positive', 0:'Negative'}
        posP = 1
        posN = 1
        bar = [i for i in range(0, len(self.data), 1)]
        plt.figure()
        stamp = time.time()
        L = []
        for i in range(1, len(self.data[0])+1, 1):
            L.append([i])
        self.matrix = GENERATOR.Solution(L, num=int(np.sqrt(max(L))))
        for i in tqdm(bar, desc=f'{self.category} Set', ncols=60,mininterval=1e-5):
            val = self.data[i]
            imageList = deepcopy(self.matrix)
            for s in range(0, len(imageList), 1):
                for t in range(0, len(imageList[s]), 1):
                    index = imageList[s][t]
                    imageList[s][t] = val[index-1]
            if self.labels[i] == 0:
                GENERATOR.AlternativePaint(
                    self,
                    imageMatrix = imageList,
                    status = DEFINITION_STATUS[0],
                    pos = f'N{posN}'
                )
                posN = -~posN
            else:
                GENERATOR.AlternativePaint(
                    self,
                    imageMatrix = imageList,
                    status = DEFINITION_STATUS[1],
                    pos = f'P{posP}'
                )
                posP = -~posP
        now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
        print("Charting costs time:")
        print(now)
        print('\n')

    def Phalanx(self) -> None:
        temp = self.data
        columnNumber = len(self.data[0])
        remark = -~columnNumber
        sequenceList = [i for i in range(1, columnNumber+1, 1)]
        while(not np.sqrt(columnNumber).is_integer()):
            columnNumber = -~columnNumber
        diff = columnNumber - len(self.data[0])
        for i in range(0, len(self.data), 1):
            tempList = temp[i]
            for j in range(0, diff, 1):
                tempList.append(self.patch)
            temp[i] = tempList
        self.data = temp
        sequenceList = GENERATOR.GenerateDunnList(sequenceList, self.predictedLabels)
        replenishment = [i for i in range(remark, -~columnNumber, 1)]
        sequenceList.append(replenishment)
        self.matrix = GENERATOR.Solution(location=sequenceList, num=int(np.sqrt(columnNumber)))


    def __LoadLabels(self) -> list:
        """
        聚类标签 .txt 文件加载器.
        """
        io = f'./tempData/storageClusterLabels/{self.rule}/{self.rule}Cluster{self.numbers}.txt'
        f = open(io, mode='r')
        text = f.readlines()
        predictedLabels = []
        for i in range(0, len(text[0]), 1):
            predictedLabels.append(eval(text[0][i]))
        return predictedLabels

    def GenerateDunnList(data:list, predictedLabels:list) -> list:
        """
        CLUSTER 类的 Static method 静态公共函数.
        """
        clusterNumber = -~max(predictedLabels)
        tensor = []
        for i in range(0, clusterNumber, 1):
            matrix = []
            for j in range(0, len(predictedLabels), 1):
                val = predictedLabels[j]
                if val == i:
                    matrix.append(data[j])
            tensor.append(matrix)
        return tensor
    
    def Solution(location: List[List[int]],num) -> List[List[int]]:
    # 寻找初始聚类中心
        def fundcenter(j: float) -> list:
            for x in range(num):
                for y in range(num):
                    if matrix[x][y] == -1:
                        center = [x, y]
                        sublocation.append(center)
                        matrix[x][y] = j
                        return center

        # 输入聚类中心,返回最近的想要的位置
        # 欧氏距离
        def bianli(center: list, number: int) -> list:
            x = center[0]
            y = center[1]
            min_distance = num*num
            ans = [0, 0]
            for i in range(num):
                for j in range(num):
                    if matrix[i][j] == -1:
                        if ((i - x) ** 2 + (j - y) ** 2) < min_distance:
                            min_distance = ((i - x) ** 2 + (j - y) ** 2)
                            ans = [i, j]
            matrix[ans[0]][ans[1]] = number
            return ans

        # 重新计算聚类中心
        def recount(sublocation: list) -> list:
            sumx, sumy = 0, 0
            for i in sublocation:
                sumx += i[0]
                sumy += i[1]
            newcenter = [sumx / len(sublocation), sumy / len(sublocation)]
            return newcenter
        # 存放聚类中心的位置
        centerlocation = list()
        # 存放所有点的位置
        alllocation = []
        matrix = [[-1] * num for _ in range(num)]
        for i in location:
            center = [-1, -1]
            # sublocation存放的是该类下的所有的点的位置
            sublocation = list()
            for index, j in enumerate(i):
                if center == [-1, -1]:
                    center = fundcenter(j)
                    continue
                sublocation.append(bianli(center, j))
                # 更新中心
                center = recount(sublocation)
                if index == len(i) - 1:
                    centerlocation.append(center)
                    alllocation.append(list(sublocation))

        def find_more_near() -> None:
            for i in range(len(alllocation)):
                for j in range(len(alllocation[i])):
                    for k in range(len(alllocation)):
                        for l in range(len(alllocation[k])):
                            if i!=k and (alllocation[i][j][0] - centerlocation[i][0]) ** 2 + (
                                    alllocation[i][j][1] - centerlocation[i][1]) ** 2 + (
                                    alllocation[k][l][0] - centerlocation[k][0]) ** 2 + (
                                    alllocation[k][l][1] - centerlocation[k][1]) ** 2 > (
                                    alllocation[i][j][0] - centerlocation[k][0]) ** 2 + (
                                    alllocation[i][j][1] - centerlocation[k][1]) ** 2 + (
                                    alllocation[k][l][0] - centerlocation[i][0]) ** 2 + (
                                    alllocation[k][l][1] - centerlocation[i][1]) ** 2:
                                matrix[alllocation[i][j][0]][alllocation[i][j][1]], matrix[alllocation[k][l][0]][
                                    alllocation[k][l][1]] = matrix[alllocation[k][l][0]][alllocation[k][l][1]], \
                                matrix[alllocation[i][j][0]][alllocation[i][j][1]]
                                alllocation[i][j], alllocation[k][l] = alllocation[k][l], alllocation[i][j]
                                sumx = 0
                                sumy = 0
                                for x, y in alllocation[i]:
                                    sumx += x
                                    sumy += y
                                centerlocation[i] = [sumx / len(alllocation[i]), sumy / len(alllocation[i])]
                                sumx = 0
                                sumy = 0
                                for x, y in alllocation[k]:
                                    sumx += x
                                    sumy += y
                                centerlocation[k] = [sumx / len(alllocation[k]), sumy / len(alllocation[k])]
                                return
        circulation = 1000
        while circulation:
            compare = deepcopy(alllocation)
            find_more_near()
            circulation-=1
            if compare == alllocation:
                break
        return matrix

    def Paint(self, imageMatrix:list, status:str, pos:int):
        plt.matshow(imageMatrix, cmap=plt.get_cmap('binary'))
        plt.xticks([])
        plt.yticks([])
        plt.axis('off')
        plt.savefig(
            fname = f'./ChartResults/{self.rule}/ClusterNumber{self.numbers}/{self.category}{status}/{pos}.png',
            bbox_inches = 'tight',
            dpi = 30,
            pad_inches = 0.0
        )
        plt.clf()
        plt.close('all')

    def AlternativePaint(self, imageMatrix:list, status:str, pos:int) -> None:
        plt.matshow(imageMatrix, cmap=plt.get_cmap('binary'))
        plt.xticks([])
        plt.yticks([])
        plt.axis('off')
        plt.savefig(
            fname = f'./ChartResults/{self.rule}/{self.category}{status}/{pos}.png',
            bbox_inches = 'tight',
            dpi = 30,
            pad_inches = 0.0
        )
        plt.clf()
        plt.close('all')