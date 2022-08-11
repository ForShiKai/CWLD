import Orange
# import orngStat
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Adam-LDL-SCL x^2
names = ['FCM ', 'KM', 'LP', 'ML', 'GLLE', 'LESC', 'CWLD']
# Intersec
# avranks = [4.46, 7.00, 4.38, 5.85, 3.00, 1.92, 1.07]

# Cosine
# avranks = [4.54, 6.92, 4.15, 5.85, 3.23, 1.92, 1.07]

# KL
# avranks = [4.69, 7.00, 4.46, 5.85, 2.92, 1.92, 1.07]

# Clark
# avranks = [4.38, 7.00, 4.62, 6.00, 3.00, 1.85, 1.07]

# Canber
# avranks = [4.23, 7.00, 4.77, 6.00, 3.00, 1.92, 1.07]

# cheb
avranks = [5.00, 7.00, 4.00, 5.85, 3.08, 1.92, 1.07]

 #tested on 13 datasets
cd = Orange.evaluation.compute_CD(avranks, 13, alpha='0.05', test='bonferroni-dunn')

print('cd=', cd)
Orange.evaluation.graph_ranks(avranks, names, cd=cd, width=8, cdmethod=6, reverse=True)
# reverse 表示按照算法平均排名从左到右依次增大的顺序绘图
# cdmethod 为控制算法的索引，如果不指定则每个算法都会标出其CD范围
plt.show()