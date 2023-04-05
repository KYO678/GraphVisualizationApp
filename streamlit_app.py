import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from community import community_louvain

def read_csv(file):
    """Reads CSV file and returns adjacency matrix as a Pandas DataFrame."""
    df = pd.read_csv(file, index_col=0, header=0)
    df.index = df.index.astype(str)
    df.columns = df.columns.astype(str)
    return df

def create_graph(adj_matrix):
    """Creates a directed graph from the adjacency matrix."""
    G = nx.from_pandas_adjacency(adj_matrix, create_using=nx.DiGraph())
    return G

def compute_centrality(G, method):
    """Computes centrality of nodes based on the selected method."""
    if method == "Closeness Centrality":
        centrality = nx.closeness_centrality(G)
    elif method == "Betweenness Centrality":
        centrality = nx.betweenness_centrality(G)
    elif method == "Eigenvector Centrality":
        centrality = nx.eigenvector_centrality(G)
    elif method == "In-degree Centrality":
        centrality = nx.in_degree_centrality(G)
    elif method == "Out-degree Centrality":
        centrality = nx.out_degree_centrality(G)
    elif method == "Katz Centrality":
        centrality = nx.katz_centrality(G)
    return centrality

def plot_graph(G, centrality, method):
    """Plots directed graph with node centrality."""
    # Plot settings
    edge_trace = go.Scatter(x=[], y=[], line=dict(width=0.5, color="#888"), hoverinfo="none", mode="lines")
    node_trace = go.Scatter(x=[], y=[], text=[], mode="markers+text", textposition="bottom center", hoverinfo="text", marker=dict(showscale=True, colorscale="Blues", reversescale=False, color=[], size=10, colorbar=dict(thickness=15, title=f"{method}", xanchor="left", titleside="right"), line=dict(width=2)))

    # Position nodes using Fruchterman-Reingold force-directed algorithm
    pos = nx.spring_layout(G)

    # Add edges to plot
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace["x"] += tuple([x0, x1, None])
        edge_trace["y"] += tuple([y0, y1, None])

    # Add nodes to plot
    for node in G.nodes():
        x, y = pos[node]
        node_trace["x"] += tuple([x])
        node_trace["y"] += tuple([y])
        node_trace["marker"]["color"] += tuple([centrality[node]])
        node_trace["text"] += tuple([f"{node}<br>{method}: {centrality[node]:.2f}"])

    # Create plot
    fig = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(showlegend=False, hovermode="closest", margin=dict(b=20, l=5, r=5, t=40), xaxis=dict(showgrid=False, zeroline=False, showticklabels=False), yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    return fig

def plot_centrality_bar(centrality, method):
    """Plots bar graph of centrality values."""
    df = pd.DataFrame(centrality.items(), columns=["Node", "Centrality"])
    fig = px.bar(df, x="Node", y="Centrality", title=f"{method}", labels={"Centrality": f"{method}"})
    return fig


def plot_clustered_graph(G, method):
    """Plots graph with nodes colored based on clustering method."""
    if method in ["Louvain method", "Label Propagation method", "Fast Greedy method"]:
        G = G.to_undirected()

    if method == "Louvain method":
        partition = community_louvain.best_partition(G)
    elif method == "Girvan-Newman method":
        communities = nx.community.girvan_newman(G)
        partition = {node: cid for cid, community in enumerate(next(communities)) for node in community}
    elif method == "Fast Greedy method":
        dendrogram = community_louvain.generate_dendrogram(G, random_state=42)
        partition = community_louvain.partition_at_level(dendrogram, len(dendrogram) - 1)
    elif method == "Label Propagation method":
        communities = list(nx.community.label_propagation_communities(G))
        partition = {node: cid for cid, community in enumerate(communities) for node in community}
    elif method == "Spectral Clustering method":
        raise NotImplementedError("Spectral Clustering method not implemented.")
    elif method == "Infomap method":
        raise NotImplementedError("Infomap method not implemented.")

    # Node colors based on community
    node_colors = [partition[node] for node in G.nodes()]

    # Create a figure and axis objects
    fig, ax = plt.subplots()

    # Plot graph with node colors
    nx.draw(G, with_labels=True, node_color=node_colors, cmap="viridis", ax=ax)

    return fig


def main():
    st.title("Graph Analysis App")

    # Read CSV file
    st.sidebar.title("Upload CSV")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        adj_matrix = read_csv(uploaded_file)
        G = create_graph(adj_matrix)

        # Select centrality method
        st.sidebar.title("Select Centrality Method")
        centrality_method = st.sidebar.selectbox("Choose a Centrality method", ("Closeness Centrality", "Betweenness Centrality", "Eigenvector Centrality", "In-degree Centrality", "Out-degree Centrality", "Katz Centrality"))

        # Compute centrality
        centrality = compute_centrality(G, centrality_method)

        # Plot graph
        st.title("Graph Visualization")
        st.plotly_chart(plot_graph(G, centrality, centrality_method))

        # Plot centrality bar chart
        st.title("Centrality Bar Chart")
        st.plotly_chart(plot_centrality_bar(centrality, centrality_method))

        # Select clustering method
        st.sidebar.title("Select Clustering Method")
        #clustering_method = st.sidebar.selectbox("Choose a Clustering method", ("Louvain method", "Girvan-Newman method", "Fast Greedy method", "Label Propagation method", "Spectral Clustering method", "Infomap method"))
        clustering_method = st.sidebar.selectbox("Choose a Clustering method", ("Louvain method", "Girvan-Newman method", "Fast Greedy method", "Label Propagation method",))

        # Plot clustered graph
        st.title("Clustered Graph Visualization")
        clustered_fig = plot_clustered_graph(G, clustering_method)
        st.pyplot(clustered_fig)


if __name__ == "__main__":
    main()