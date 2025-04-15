# 題目一：分群分析
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor

# 分群資料產生與 KMeans
np.random.seed(42)
df = pd.DataFrame({
    'CustomerID': range(1, 201),
    'Age': np.random.randint(18, 70, size=200),
    'Annual Income (k$)': np.random.randint(15, 150, size=200),
    'Spending Score (1–100)': np.random.randint(1, 101, size=200)
})
X = df[['Annual Income (k$)', 'Spending Score (1–100)']]
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(X)

# 視覺化
sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1–100)', hue='Cluster', palette='Set2')
plt.title('KMeans Clustering Result')
plt.show()

# 題目二：異常偵測 LOF
X_lof = np.array([
    [1.0, 1.1], [1.2, 1.0], [0.9, 0.95], [1.0, 1.0], [1.05, 1.0],
    [1.1, 1.2], [1.0, 0.9], [1.2, 1.1], [0.95, 1.05], [1.0, 0.95]
])
lof = LocalOutlierFactor(n_neighbors=3)
lof_result = lof.fit_predict(X_lof)
lof_scores = -lof.negative_outlier_factor_

df_lof = pd.DataFrame(X_lof, columns=["X1", "X2"])
df_lof["LOF"] = lof_scores
df_lof["Is_Outlier"] = lof_result == -1

# 畫圖
sns.scatterplot(x=df_lof["X1"], y=df_lof["X2"], hue=df_lof["Is_Outlier"], palette={True: "red", False: "blue"})
plt.title("Local Outlier Factor (LOF) Detection")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()

# 題目三：關聯規則探勘
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ['牛奶', '麵包', '尿布'],
    ['可樂', '尿布', '啤酒', '雞蛋'],
    ['牛奶', '尿布', '啤酒', '可樂'],
    ['麵包', '牛奶', '尿布', '啤酒'],
    ['麵包', '牛奶', '尿布', '可樂']
]
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df_trans, min_support=0.6, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.8)
print(rules)
