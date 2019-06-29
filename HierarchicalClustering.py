'''
    凝聚层次聚类算法:
    1. 获取所有样本的距离矩阵；
    2. 将每个数据点作为一个单独的簇；
    3. 基于最不相似(距离最远)样本的距离，合并两个最接近的簇；
    4. 更新样本的距离矩阵；
    5. 重复2到4，直到所有样本都属于同一个簇为止。
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist,squareform
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# 参数
labels = ["15Age", "20Age", "35Age", "45Age", "55Age", "60Age"]     # 编号
feature = ["location"]     # 特征
data = [15, 20, 35, 45, 55, 60]     # 数据

#通过pandas将数组转换成一个DataFrame
dist_matrix = pd.DataFrame(data, columns = feature, index = labels)
print(dist_matrix)
print("===========================================")

# 只有一个特征(一维)和多个特征(高维)的求法是不一样的, 高维时需要生成对角距离矩阵, 一维则不需要
if(len(feature) != 1):
    # 高纬时运行以下程序
    # pdist: 计算两两样本间的欧式距离, 返回的是一个一维数组
    # squareform: 将数组转成一个对称矩阵
    dist_matrix = pd.DataFrame(squareform(pdist(dist_matrix, metric="euclidean")), columns = labels, index = labels)
    print(dist_matrix)
    print("===========================================")

# linkage是scipy自带的层次聚类算法, 输入: 
result_clusters = linkage(dist_matrix.values, method = "complete", metric = "euclidean")
"""
    输出由四列组成：
    第一字段与第二字段分别为聚类簇的编号，每生成一个新的聚类簇就在此基础上增加一对新的聚类簇进行标识
    第三个字段表示前两个聚类簇之间的距离
    第四个字段表示新生成聚类簇所包含的元素的个数
"""
clusters = pd.DataFrame(result_clusters, columns=["label 1","label 2","distance","sampleSize"],
                        index=["cluster %d"%(i+1) for i in range(result_clusters.shape[0])])
print(clusters)
print("===========================================")

# 画图
dendr = dendrogram(result_clusters, labels = labels)
plt.ylabel("distance between two ages")
plt.savefig("result.png")
print("图片已保存")
plt.show()
