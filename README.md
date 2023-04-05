# GraphVisualizationApp
Streamlit Sample App

# プロジェクトの概要（アプリの目的、使用技術など）
グラフデータを可視化するWebアプリです。

https://raw.githubusercontent.com/ragini30/Networks-Homework/main/phase1.csv

# 使用方法
1. Access to https://kyo678-graphvisualizationapp-streamlit-app-a9p7gy.streamlit.app/
2. Upload CSV file

# 使用している技術
1. Centrality Analysis
2. Graph Clustering
※詳細は工事中

## Prompt to GPT4
**Prerequisites:**
1. code must include comments
2. use Python 3.9
3. use the main function
4. avoid using global variables by passing necessary variables via function arguments
5. use Plotly for plotting
6. use Streamlit to create web apps

**Functional Requirements:**
1. read a CSV file with the following structure:
  
    1-1. this CSV file represents the adjacency matrix of a directed graph
 
    1-2. the value of each cell represents the weight of an edge
 
    1-3. the first row and the first column indicate the ID of the node
  
        - The cell in the first row and first column contains the string "player".
        
        - The ID of the node contains an integer value.
        
2. plot the data read in under Functional Condition 1 in the following format

    2-1. The first plot is a graph showing the connection between each node.
    
        2-1-1. the ID of each node is noted on the node
        
        2-1-2. assume a directed graph, so also plot the direction and weight of each edge
        
        2-1-3. shade the nodes according to the value of Centrality: dark blue for nodes with high Centrality and light blue for nodes with low Centrality
        
        2-1-4. for Centrality, the following can be selected from a pull-down menu
            - Closeness Centrality
            - Betweenness Centrality
            - Eigenvector Centrality
            - In-degree Centrality
            - Out-degree Centrality
            - Katz Centrality
            
    2-2. The second plot is a bar graph of the Centrality values selected above, with the horizontal axis representing the Node IDs and the vertical axis representing the Centrality values.
    
    2-3. The third plot is a color-coded plot of each Node according to the results of the graph clustering. In doing so, select the type of clustering in a pull-down format from the following
        - Louvain method
        - Girvan-Newman method
        - Fast Greedy method
        - Label Propagation method
        - Spectral Clustering method
        - Infomap method
        
    2-4. Arrange the above graphs vertically
