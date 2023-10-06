import matplotlib.pyplot as plt
"""
这是笔者试验得到的一组统计数据.
图片个数 -- 分辨率（正方形） -- 完整一次卷积需要的显存
# 1 -- 1704 dpi -- 70.224MB
# 2 -- 1704 dpi -- 117.992MB
# 5 -- 1704 dpi -- 263.181MB
# 10 -- 1704 dpi -- 505.218MB
# 20 -- 1704 dpi -- 990.609MB
# 30 -- 1704 dpi -- 1473MB
# 40 -- 1704 dpi -- 1959.626MB
# 45 -- 1704 dpi -- 2201.543MB
# 46 -- 1704 dpi -- 4GB 显存不够，报错.
"""

X = [1,2,5,10,20,30,40,45]
Y1 = [70.24,117.99,263.18,505.21,990.60,1473,1959.626,2201.543]
Y2 = [i*70.224 for i in X]

plt.rcParams['font.sans-serif']=['Kaiti']
plt.plot(X,Y1,'--')
plt.plot(X,Y2,'-')
plt.xlabel('图片个数', fontsize=16)
plt.ylabel('显存大小', fontsize=16)
plt.show()