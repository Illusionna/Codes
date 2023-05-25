# 根目录下包含保存结果 saveFile.py 和绘图 plot.py 文件.
from plot import *
from saveFile import *

# saveFile.py 文件里修改 Excel 的路径.

# 设定迭代次数.
epoches = 3

# iteration() # 默认不迭代，无参数函数.
# iteration(False, n_clusters = 3) # 默认不迭代，无参数函数.

tupleResult = iteration(
    judge = True,
    # n_clusters = 0,
    epoch = epoches
)

plot(
    judge = True,
    tupleResult = tupleResult,
    subplotjudge = False,
    epoch = epoches
)