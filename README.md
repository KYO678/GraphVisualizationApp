# GraphVisualizationApp
Streamlit Sample App

# プロジェクトの概要（アプリの目的、使用技術など）
グラフデータを可視化するWebアプリです。
下記のように有向グラフを隣接マトリックス形式で扱うことを仮定します。
https://raw.githubusercontent.com/ragini30/Networks-Homework/main/phase1.csv

# 使用方法
1. Access to https://kyo678-graphvisualizationapp-streamlit-app-a9p7gy.streamlit.app/
2. Upload CSV file
3. Select Centrality Method : 中心性分析のいずれかの手法を選択します。
4. Select Clustering Method : グラフクラスタリングのいずれかの手法を選択します。

# 使用している技術
1. Centrality Analysis
  1.1. Closeness Centrality
  1.2. Betweenness Centrality
  1.3. Eigenvector Centrality
  1.4. In-degree Centrality
  1.5. Out-degree Centrality
  1.6. Katz Centrality 
2. Graph Clustering
  2.1. Louvain method
  2.2. Girvan-Newman method
  2.3. Fast Greedy method
  2.4. Label Propagation method
