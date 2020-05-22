import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# 鸢尾花花萼长度数据做聚类并用散点图显示
iris = datasets.load_iris()
x=iris.data[:,0]#取出鸢尾花花萼的长度
y=np.zeros(len(x))#用于存放聚类中心的标签

#-----------------------------------手写K-Means聚类算法-------------------------------------------
#选最开始的3个数据作为聚类的中心
def start_center(sample,k):
    return sample[:k]
kc = start_center(x,3)

#求到聚类中心kc的欧氏距离，按距离最短分到相应的kc类
def nearest(kc,sample):
    d = abs(kc - sample)
    t = np.where(d == np.min(d))
    return t[0][0]
def xclassify(sample,y,kc):
    for i in range(len(sample)):
        y[i]=nearest(kc,sample[i])
    return y
y=xclassify(x,y,kc)

#更新聚类中心，将每个类中所有对象的均值作为该类别的聚类中心
def kcmean(sample,y,kc,k):
    l=list(kc)
    flag=False
    for j in range(k):
        m=np.where(y==j)
        means=np.mean(sample[m])
        if l[j]!=means:
            l[j]=means
            flag=True
    return(np.array(l),flag)

#迭代，知道聚类中心不再变化
flag=True
while flag:
    y=xclassify(x,y,kc)
    kc,flag=kcmean(x,y,kc,3)
print(y,kc)

#用散点图来显示聚类结果
plt.scatter(x,x,s=x,c=y,cmap='rainbow',alpha=0.5,linewidths=3)
plt.scatter(kc[0], kc[0], c='purple',s=200, marker='o',edgecolors='g',  alpha=0.7)
plt.scatter(kc[1], kc[1], c='cyan',s=200, marker='o',edgecolors='g',  alpha=0.7)
plt.scatter(kc[2], kc[2], c='r',s=200, marker='o', edgecolors='g', alpha=0.7)
plt.xlabel('sepal length')
plt.ylabel('sepal length')
plt.show()

# -----------------------------------调用sklearn中的K-Means聚类算法-------------------------------------------
from sklearn.cluster import KMeans
X = iris.data[:, :2]  #取特征空间中的前2个维度数据
predict = KMeans(n_clusters=3)  # 构造聚类器分为3类
predict.fit(X)  # 聚类
label_pred = predict.labels_  # 获取聚类标签

# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]

#最终的聚类中心
m,n=x0.shape
sum=0
for i in x0[:,0]:
    sum=sum+i
b0=sum/m
sum=0
for i in x0[:,1]:
    sum=sum+i
b1=sum/m

m,n=x1.shape
sum=0
for i in x1[:,0]:
    sum=sum+i
b2=sum/m
sum=0
for i in x1[:,1]:
    sum=sum+i
b3=sum/m

m,n=x2.shape
sum=0
for i in x2[:,0]:
    sum=sum+i
b4=sum/m
sum=0
for i in x2[:,1]:
    sum=sum+i
b5=sum/m

#聚类散点图
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o')
plt.scatter(x1[:, 0], x1[:, 1], c="purple", marker='o')
plt.scatter(x2[:, 0], x2[:, 1], c="cyan", marker='o')
#最终的聚类中心
plt.scatter(b0,b1,s=200,c="red",marker='o',edgecolors='b',alpha=0.7)
plt.scatter(b2,b3,s=200,c="purple",marker='o',edgecolors='b',alpha=0.7)
plt.scatter(b4,b5,s=200,c="cyan",marker='o',edgecolors='b',alpha=0.7)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show()