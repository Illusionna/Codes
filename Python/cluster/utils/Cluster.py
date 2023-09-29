'''
# System --> Linux & Python3.8.0
# File ----> Cluster.py
# Author --> Illusionna
# Create --> 2023/09/02 11:25:21
'''
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    from packages import *
    from Dunn import DUNN
    from Minisom import MINISOM
else:
    from utils.packages import *
    from utils.Dunn import DUNN
    from utils.Minisom import MINISOM


class CLUSTER:
    """
    聚类类：{"Kmeans", "GMM", "SOM"}.
    """
    # Constraint the MODE type of inputing.
    MODE = Literal['Kmeans', 'GMM', 'SOM']

    def __init__(self, data:list, clusterRange:tuple=(3,3), epoch:int=1) -> None:
        os.makedirs("./tempData", exist_ok=True)
        self.data = data
        self.labels = []
        self.n_clusters = clusterRange
        self.epoch = epoch
        """
        CONTROL_ACCURACY 控制精度列表：
            Epoch       Accuracy
            1~9         1
            10~49       2
            50~99       3
            100~499     4
            500~999     5
            1000~infty  6
            else        default=3
        """
        self.CONTROL_ACCURACY = [
            [s for s in range(1, 10, 1)],
            [s for s in range(10, 50, 1)],
            [s for s in range(50, 100, 1)],
            [s for s in range(100, 500, 1)],
            [s for s in range(500, 1000, 1)],
            [s for s in range(1000, (1<<20), 1)]
        ]

    def Transpose(self) -> None:
        """
        Transpose 数据转置.
        """
        self.data = pd.DataFrame(self.data).T.values.tolist()
    
    def __CumulativeOccurrence(self, tupleList:list) -> tuple:
        """
        私有函数：计算 list 列表中稳恒众数.
        """
        def Accuracy(epoch:int, accuracyList:list) -> int:
            for i in range(0, len(accuracyList), 1):
                if epoch in accuracyList[i]:
                    return i+1
            else:
                return 3
        DBI_List = []
        for i in range(0, len(tupleList), 1):
            val = f"%.{Accuracy(self.epoch, self.CONTROL_ACCURACY)}f" % tupleList[i][0]
            DBI_List.append(float(val))
        modeNumber = max(
            DBI_List,
            default = "Error! The list is empty.",
            key = lambda element: DBI_List.count(element)
        )
        remark = DBI_List.index(modeNumber)
        return tupleList[remark]

    def __SaveClusterResult(mode:MODE, pos:int, DBI:float, DI:float, register:list, modeNumber:int, labelsList:list) -> None:
        """
        私有函数：寄存聚类结果.
        """
        f = open(f"./tempData/storageClusterLabels/{mode}_DBI_DI_Index.txt", mode='a')
        f.write("DBI:")
        f.write(str(DBI))
        f.write('\n')
        f.write("DI:")
        f.write(str(DI))
        f.write('\n\n')
        f.close()
        findFileIndex = register.index(modeNumber)
        f = open(f"./tempData/storageClusterLabels/{mode}/{mode}Cluster{pos}.txt", mode='w')
        f.writelines(map(str, labelsList[findFileIndex]))
        f.close()

    def Cluster(self, mode:MODE="Kmeans") -> None:
        """
        Cluster: args = {"Kmeans", "GMM", "SOM"}.
        """
        df = pd.DataFrame(self.data).to_excel("./tempData/processingData.xlsx", index=False, header=True)
        df = pd.read_excel("./tempData/processingData.xlsx")
        df['^#&@']= [3.1415926 for i in range(0, len(self.data), 1)]
        df.to_excel("./tempData/processingData.xlsx", index=False, header=True)

        if mode == "Kmeans":
            stamp = time.time()
            stamp = time.time()
            CLUSTER._Kmeans(self)
            now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
            print("Kmeans costs time:")
            print(now)
            print('\n')
        elif mode == "GMM":
            stamp = time.time()
            CLUSTER._Gmm(self)
            now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
            print("GMM costs time:")
            print(now)
            print('\n')
        elif mode == "SOM":
            stamp = time.time()
            CLUSTER._Som(self)
            now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
            print("SOM costs time:")
            print(now)
            print('\n')
        else:
            stamp = time.time()
            CLUSTER._Kmeans(self)
            now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
            print("Kmeans costs time:")
            print(now)
            print('\n')

    def _Kmeans(self) -> None:
        """
        受保护函数：Kmeans 聚类.
        """
        os.makedirs("./tempData/storageClusterLabels/Kmeans", exist_ok=True)
        shutil.rmtree("./tempData/storageClusterLabels/Kmeans")
        os.makedirs("./tempData/storageClusterLabels/Kmeans", exist_ok=True)
        f = open("./tempData/storageClusterLabels/Kmeans_DBI_DI_Index.txt", mode='w')
        f.close()

        bar = [i for i in range(self.n_clusters[0], (self.n_clusters[1]+1), 1)]
        for pos in tqdm(bar, desc='Kmeans', ncols=60,mininterval=1e-5):
            register = []
            labelsList = []
            for n in range(0, self.epoch, 1):
                model = KMeans(
                    n_clusters = pos,
                    n_init = 'auto'
                )
                cluster = model.fit(self.data)
                predictedLabels = model.predict(self.data)
                self.labels = predictedLabels
                labelsList.append(predictedLabels)
                DBI = davies_bouldin_score(self.data, model.predict(self.data))
                tensor = CLUSTER.GenerateDunnList(self.data, predictedLabels)
                DI = DUNN(tensor).Dunn()
                register.append((DBI, DI))

            modeNumber = CLUSTER.__CumulativeOccurrence(self, register)

            CLUSTER.__SaveClusterResult(
                mode = "Kmeans",
                pos = pos,
                DBI = DBI,
                DI = DI,
                register = register,
                modeNumber = modeNumber,
                labelsList = labelsList
            )

    def _Gmm(self) -> None:
        """
        受保护函数：GMM 聚类.
        """
        os.makedirs("./tempData/storageClusterLabels/GMM", exist_ok=True)
        shutil.rmtree("./tempData/storageClusterLabels/GMM")
        os.makedirs("./tempData/storageClusterLabels/GMM", exist_ok=True)
        f = open("./tempData/storageClusterLabels/GMM_DBI_DI_Index.txt", mode='w')
        f.close()

        bar = [i for i in range(self.n_clusters[0], (self.n_clusters[1]+1), 1)]
        for pos in tqdm(bar, desc='GMM   ', ncols=60,mininterval=1e-5):
            register = []
            labelsList = []
            for n in range(0, self.epoch, 1):
                model = GMM(
                    n_components = pos,
                    covariance_type = "full"
                )
                cluster = model.fit(self.data)
                predictedLabels = model.predict(self.data)
                self.labels = predictedLabels
                labelsList.append(predictedLabels)
                DBI = davies_bouldin_score(self.data, model.predict(self.data))
                tensor = CLUSTER.GenerateDunnList(self.data, predictedLabels)
                DI = DUNN(tensor).Dunn()
                register.append((DBI, DI))

            modeNumber = CLUSTER.__CumulativeOccurrence(self, register)

            CLUSTER.__SaveClusterResult(
                mode = "GMM",
                pos = pos,
                DBI = DBI,
                DI = DI,
                register = register,
                modeNumber = modeNumber,
                labelsList = labelsList
            )

    def _Som(self) -> None:
        """
        受保护函数：SOM 聚类.
        """
        os.makedirs("./tempData/storageClusterLabels/SOM", exist_ok=True)
        shutil.rmtree("./tempData/storageClusterLabels/SOM")
        os.makedirs("./tempData/storageClusterLabels/SOM", exist_ok=True)
        f = open("./tempData/storageClusterLabels/SOM_DBI_DI_Index.txt", mode='w')
        f.close()

        bar = [i for i in range(self.n_clusters[0], (self.n_clusters[1]+1), 1)]
        for pos in tqdm(bar, desc='SOM   ', ncols=60,mininterval=1e-5):
            register = []
            labelsList = []
            for n in range(0, self.epoch, 1):
                somShape = (1, pos)
                model = MINISOM(
                    x = 1,
                    y = pos,
                    input_len = np.array(self.data).shape[1],
                    sigma = 0.5,
                    learning_rate = 0.5,
                    neighborhood_function = "gaussian",
                    random_seed = 50
                )
                model.train_batch(self.data, 1200, verbose=True)
                winner_coordinates = np.array([model.winner(x) for x in self.data]).T
                predictedLabels = np.ravel_multi_index(winner_coordinates, somShape)
                self.labels = predictedLabels
                labelsList.append(predictedLabels)
                DBI = davies_bouldin_score(self.data, predictedLabels)
                tensor = CLUSTER.GenerateDunnList(self.data, predictedLabels)
                DI = DUNN(tensor).Dunn()
                register.append((DBI, DI))

            modeNumber = CLUSTER.__CumulativeOccurrence(self, register)

            CLUSTER.__SaveClusterResult(
                mode = "SOM",
                pos = pos,
                DBI = DBI,
                DI = DI,
                register = register,
                modeNumber = modeNumber,
                labelsList = labelsList
            )

    def GenerateDunnList(data:list, predictedLabels:list) -> list:
        """
        Static method 静态公共函数：为 Dunn 指数计算，根据预测标签生成聚类三维张量.
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


if __name__ == '__main__':
    randomData = np.random.randint(1, 9, size=[70, 12])
    clusterRange = (2, 4)
    epoch = 10

    obj = CLUSTER(randomData.tolist(), clusterRange, epoch)

    obj.Cluster(mode="GMM")