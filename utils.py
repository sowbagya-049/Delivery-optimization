import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

priority_map = {"High": 3, "Medium": 2, "Low": 1}

def calculate_metrics(agent_distance, agents, df):
    variance = np.var(list(agent_distance.values()))
    max_dist = max(agent_distance.values())

    priority_score = 0
    for agent in agents:
        for loc in agents[agent]:
            val = df[df["Location ID"] == loc]["Priority_Value"].values[0]
            priority_score += val

    return variance, max_dist, priority_score


#greed method
def method_greedy(df):
    df["Priority_Value"] = df["Delivery Priority"].map(priority_map)
    df["Score"] = df["Priority_Value"] / df["Distance from warehouse"]

    df = df.sort_values(by="Score", ascending=False)

    agents = {1: [], 2: [], 3: []}
    agent_distance = {1: 0, 2: 0, 3: 0}

    for _, row in df.iterrows():
        agent = min(agent_distance, key=agent_distance.get)
        agents[agent].append(row["Location ID"])
        agent_distance[agent] += row["Distance from warehouse"]

    var, max_d, p_score = calculate_metrics(agent_distance, agents, df)

    return agents, agent_distance, var, max_d, p_score


#kmeans method
def method_kmeans(df):
    df["Priority_Value"] = df["Delivery Priority"].map(priority_map)

    kmeans = KMeans(n_clusters=3, random_state=0)
    df["Cluster"] = kmeans.fit_predict(df[["Distance from warehouse"]])

    agents = {0: [], 1: [], 2: []}
    agent_distance = {0: 0, 1: 0, 2: 0}

    for _, row in df.iterrows():
        c = row["Cluster"]
        agents[c].append(row["Location ID"])
        agent_distance[c] += row["Distance from warehouse"]

    var, max_d, p_score = calculate_metrics(agent_distance, agents, df)

    return agents, agent_distance, var, max_d, p_score


#comparision
def decision_function(var1, var2, max1, max2, p1, p2):
    score1 = 0.5*var1 + 0.3*max1 - 0.2*p1
    score2 = 0.5*var2 + 0.3*max2 - 0.2*p2

    if score1 < score2:
        return "Greedy"
    else:
        return "KMeans"