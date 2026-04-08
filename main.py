import pandas as pd
import os
import matplotlib.pyplot as plt
from utils import method_greedy, method_kmeans, decision_function

API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("API loaded")
    
input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

report = []

def plot_distance(dist1, dist2, filename):
    agents = list(dist1.keys())
    d1 = list(dist1.values())
    d2 = list(dist2.values())
    x = list(range(len(agents)))

    plt.figure()
    plt.bar(x, d1, width=0.4, label="Greedy")
    plt.bar([i + 0.4 for i in x], d2, width=0.4, label="KMeans")
    plt.xticks([i + 0.2 for i in x], [f"A{i+1}" for i in range(len(agents))])
    plt.title("Distance Comparison")
    plt.xlabel("Agents")
    plt.ylabel("Total Distance")
    plt.legend()

    plt.savefig(f"{output_folder}/{filename}_distance.png")
    plt.close()


def plot_metrics(v1, v2, m1, m2, p1, p2, filename):
    labels = ["Variance", "Max", "Priority"]
    g = [v1, m1, p1]
    k = [v2, m2, p2]
    x = list(range(len(labels)))

    plt.figure()
    plt.bar(x, g, width=0.4, label="Greedy")
    plt.bar([i + 0.4 for i in x], k, width=0.4, label="KMeans")
    plt.xticks([i + 0.2 for i in x], labels)
    plt.title("Metrics Comparison")
    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.legend()

    plt.savefig(f"{output_folder}/{filename}_metrics.png")
    plt.close()


if __name__ == "__main__":

    print("SCRIPT STARTED")

    files = os.listdir(input_folder)
    print("Files found:", files)

    for file in files:
        if file.endswith(".csv"):

            print(f"\nProcessing: {file}")

            df = pd.read_csv(os.path.join(input_folder, file))

            a1, d1, v1, m1, p1 = method_greedy(df.copy())
            a2, d2, v2, m2, p2 = method_kmeans(df.copy())

            
            best = decision_function(v1, v2, m1, m2, p1, p2)
            final_agents = a1 if best == "Greedy" else a2

            output = []

            for agent in final_agents:
                for loc in final_agents[agent]:
                    row = df[df["Location ID"] == loc].iloc[0]

                    output.append([
                        agent,
                        loc,
                        row["Distance from warehouse"],
                        row["Delivery Priority"]
                    ])

            output_df = pd.DataFrame(output, columns=[
                "Agent", "Location ID", "Distance", "Priority"
            ])

            output_df.to_csv(
                f"{output_folder}/output_{file}", index=False
            )

            summary = []

            for agent in final_agents:
                total_distance = 0
                for loc in final_agents[agent]:
                    total_distance += df[df["Location ID"] == loc]["Distance from warehouse"].values[0]

                summary.append([agent, total_distance])

            summary_df = pd.DataFrame(summary, columns=[
                "Agent", "Total Distance"
            ])

            summary_df.to_csv(
                f"{output_folder}/summary_{file}", index=False
            )

            plot_distance(d1, d2, file)
            plot_metrics(v1, v2, m1, m2, p1, p2, file)

            report.append([file, v1, v2, m1, m2, p1, p2, best])

            print(f"{file} → Best Method: {best}")

    report_df = pd.DataFrame(report, columns=[
        "File", "Var_Greedy", "Var_KMeans",
        "Max_Greedy", "Max_KMeans",
        "Priority_Greedy", "Priority_KMeans",
        "Best_Method"
    ])

    report_df.to_csv("comparison_report.csv", index=False)

    print("\ncomparison_report.csv generated!")
    print("All processing completed!")
