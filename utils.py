import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# ✅ CONSTANTS (fix Sonar issues)
LOCATION_COL = "Location ID"
DISTANCE_COL = "Distance from warehouse"
PRIORITY_COL = "Delivery Priority"

priority_map = {"High": 3, "Medium": 2, "Low": 1}


def calculate_metrics(agent_distance, agents, df):
    variance = np.var(list(agent_distance.values()))
    max_dist = max(agent_distance.values())

    priority_score = 0
    for agent in agents:
        for loc in agents[agent]:
            val = df[df[LOCATION_COL] == loc]["Priority_Value"].values[0]
            priority_score += val

    return variance, max_dist, priority_score


# Greedy Method
def method_greedy(df):
    df["Priority_Value"] = df[PRIORITY_COL].map(priority_map)
    df["Score"] = df["Priority_Value"] / df[DISTANCE_COL]

    df = df.sort_values(by="Score", ascending=False)

    agents = {1: [], 2: [], 3: []}
    agent_distance = {1: 0, 2: 0, 3: 0}

    for _, row in df.iterrows():
        agent = min(agent_distance, key=agent_distance.get)
        agents[agent].append(row[LOCATION_COL])
        agent_distance[agent] += row[DISTANCE_COL]

    var, max_d, p_score = calculate_metrics(agent_distance, agents, df)

    return agents, agent_distance, var, max_d, p_score


# KMeans Method
def method_kmeans(df):
    df["Priority_Value"] = df[PRIORITY_COL].map(priority_map)

    kmeans = KMeans(n_clusters=3, random_state=0)
    df["Cluster"] = kmeans.fit_predict(df[[DISTANCE_COL]])

    agents = {0: [], 1: [], 2: []}
    agent_distance = {0: 0, 1: 0, 2: 0}

    for _, row in df.iterrows():
        c = row["Cluster"]
        agents[c].append(row[LOCATION_COL])
        agent_distance[c] += row[DISTANCE_COL]

    var, max_d, p_score = calculate_metrics(agent_distance, agents, df)

    return agents, agent_distance, var, max_d, p_score


# Decision Function
def decision_function(var1, var2, max1, max2, p1, p2):
    score1 = 0.5 * var1 + 0.3 * max1 - 0.2 * p1
    score2 = 0.5 * var2 + 0.3 * max2 - 0.2 * p2

    return "Greedy" if score1 < score2 else "KMeans"
