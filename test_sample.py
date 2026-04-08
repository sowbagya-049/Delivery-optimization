from utils import method_greedy, method_kmeans, decision_function
import pandas as pd

def test_dataframe():
    df = pd.DataFrame({
        "Location ID": [1, 2],
        "Distance from warehouse": [10, 20],
        "Delivery Priority": ["High", "Low"]
    })
    assert not df.empty

def test_greedy():
    df = pd.DataFrame({
        "Location ID": [1, 2, 3],
        "Distance from warehouse": [10, 20, 30],
        "Delivery Priority": ["High", "Medium", "Low"]
    })
    result = method_greedy(df)
    assert len(result) == 5

def test_kmeans():
    df = pd.DataFrame({
        "Location ID": [1, 2, 3],
        "Distance from warehouse": [10, 20, 30],
        "Delivery Priority": ["High", "Medium", "Low"]
    })
    result = method_kmeans(df)
    assert len(result) == 5

def test_decision():
    res = decision_function(1, 2, 3, 4, 5, 6)
    assert res in ["Greedy", "KMeans"]

def test_math():
    assert 2 + 2 == 4
