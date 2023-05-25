import matplotlib.pyplot as plt

def plot(judge:bool=False, tupleResult:tuple=(), subplotjudge:bool=False, epoch:int=3) -> None:
    if judge == False:
        pass
    elif judge == True:
        resultKmeans = tupleResult[0]
        resultGMM = tupleResult[1]
        L = [i for i in range(2, epoch+2, 1)]
        if subplotjudge == False:
            plt.figure(1, figsize=(8, 5), dpi=120)
            plt.plot(L, resultKmeans[0], linestyle='--')
            plt.plot(L, resultKmeans[1], linestyle='--')
            plt.scatter(L, resultKmeans[0], s=12)
            plt.scatter(L, resultKmeans[1], s=12)
            plt.xlabel("Cluster Numbers", font={"family":"Times New Roman","size":12})
            plt.ylabel("Internal Index", font={"family":"Times New Roman","size":12})
            plt.title("Kmeans: Expect the DBI to be smaller & Expect the DI to be larger", font={"family":"Times New Roman","size":15})
            plt.legend(["Davies-Bouldin Index", "Dunn Index"], loc='upper right')
            plt.savefig("./result/KmeansClusterIndexResult.pdf")

            plt.figure(2, figsize=(8, 5), dpi=120)
            plt.plot(L, resultGMM[0], linestyle='--')
            plt.plot(L, resultGMM[1], linestyle='--')
            plt.scatter(L, resultGMM[0], s=12)
            plt.scatter(L, resultGMM[1], s=12)
            plt.xlabel("Cluster Numbers", font={"family":"Times New Roman","size":12})
            plt.ylabel("Internal Index", font={"family":"Times New Roman","size":12})
            plt.title("GMM: Expect the DBI to be smaller & Expect the DI to be larger", font={"family":"Times New Roman","size":15})
            plt.legend(["Davies-Bouldin Index", "Dunn Index"], loc='upper right')
            plt.savefig("./result/GMMClusterIndexResult.pdf")

            plt.show()
            plt.close()
        elif subplotjudge == True:
            plt.figure(figsize=(10,6.5), dpi=120)
            plt.subplot(2, 1, 1)

            plt.figure(1, figsize=(8, 5), dpi=120)
            plt.plot(L, resultKmeans[0], linestyle='--')
            plt.plot(L, resultKmeans[1], linestyle='--')
            plt.scatter(L, resultKmeans[0], s=12)
            plt.scatter(L, resultKmeans[1], s=12)
            ## 如果需要 X 轴，取消注释.
            # plt.xlabel("Cluster Numbers", font={"family":"Times New Roman","size":10})
            plt.ylabel("Internal Index", font={"family":"Times New Roman","size":10})
            plt.title("Kmeans: Expect the DBI to be smaller & Expect the DI to be larger", font={"family":"Times New Roman","size":11})
            plt.legend(["Davies-Bouldin Index", "Dunn Index"], loc='upper right')

            plt.subplot(2, 1, 2)
            plt.plot(L, resultGMM[0], linestyle='--')
            plt.plot(L, resultGMM[1], linestyle='--')
            plt.scatter(L, resultGMM[0], s=12)
            plt.scatter(L, resultGMM[1], s=12)
            plt.xlabel("Cluster Numbers", font={"family":"Times New Roman","size":10})
            plt.ylabel("Internal Index", font={"family":"Times New Roman","size":10})
            plt.title("GMM: Expect the DBI to be smaller & Expect the DI to be larger", font={"family":"Times New Roman","size":11})
            plt.legend(["Davies-Bouldin Index", "Dunn Index"], loc='upper right')
            plt.savefig("./result/MixtureClusterIndexResult.pdf")

            plt.show()
            plt.close()