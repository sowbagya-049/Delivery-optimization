from utils import method_greedy, method_kmeans, decision_function
import pandas as pd
import subprocess

def sample_df():
    return pd.DataFrame({
        "Location ID": [1, 2, 3, 4],
        "Distance from warehouse": [10, 20, 30, 40],
        "Delivery Priority": ["High", "Medium", "Low", "High"]
    })

def test_greedy():
    df = sample_df()
    agents, _, _, _, _ = method_greedy(df)
    assert isinstance(agents, dict)

def test_kmeans():
    df = sample_df()
    agents, _, _, _, _ = method_kmeans(df)
    assert isinstance(agents, dict)

def test_decision():
    result = decision_function(1, 2, 3, 4, 5, 6)
    assert result in ["Greedy", "KMeans"]

def test_empty_df():
    df = pd.DataFrame(columns=["Location ID", "Distance from warehouse", "Delivery Priority"])
    assert df.empty

def test_priority_map():
    df = sample_df()
    df["Priority_Value"] = df["Delivery Priority"].map({"High":3,"Medium":2,"Low":1})
    assert df["Priority_Value"].sum() > 0

def test_distance_sum():
    df = sample_df()
    assert df["Distance from warehouse"].sum() == 100

def test_main_execution():
    result = subprocess.run(["python3", "main.py"], capture_output=True)
    assert result.returncode == 0
