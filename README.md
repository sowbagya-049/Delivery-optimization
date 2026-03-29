#  Delivery Optimization System

##  Overview

This project focuses on solving a **Logistics Delivery Optimization Problem** using advanced decision-making techniques. The system processes delivery data and assigns tasks to agents efficiently while balancing workload and prioritizing urgent deliveries.

---

##  Objectives

* Read delivery data from CSV files
* Prioritize deliveries based on urgency
* Optimize assignment across 3 agents
* Minimize total travel distance imbalance
* Compare multiple optimization techniques
* Select the best method dynamically

---

##  Input Format

Each input CSV file must contain:

| Column Name             | Description                    |
| ----------------------- | ------------------------------ |
| Location ID             | Unique identifier for location |
| Distance from warehouse | Distance value                 |
| Delivery Priority       | High / Medium / Low            |

---

##  Algorithms Used

### 🔹 1. Greedy + Priority Weighting

* Assigns priority values (High = 3, Medium = 2, Low = 1)
* Computes score = Priority / Distance
* Sorts deliveries based on score
* Assigns tasks to the agent with minimum total distance

✔ Fast and efficient
✔ Ensures priority handling

---

### 🔹 2. K-Means Clustering

* Groups locations into 3 clusters
* Each cluster is assigned to an agent
* Minimizes travel distance naturally

✔ Good for spatial grouping
✔ Balanced clustering approach

---

##  Decision Technique

A **Multi-Criteria Decision Making (MCDM)** approach is used to select the best method based on:

*  Variance → Load balancing
*  Maximum Distance → Workload fairness
*  Priority Score → Urgency handling

###  Decision Formula:

Score = 0.5 × Variance + 0.3 × Max Distance − 0.2 × Priority Score

 Lower score indicates a better solution

---

##  Workflow

1. Read all input CSV files
2. Apply both algorithms (Greedy & K-Means)
3. Calculate performance metrics
4. Compare results using MCDM
5. Select the best method
6. Generate outputs and visualizations

---

##  Output Files

For each input file, the system generates:

###  1. Optimized Delivery Plan (`output_*.csv`)

Includes:

* Agent assignment
* Location ID
* Distance
* Priority

Example:

```
Agent,Location ID,Distance,Priority
1,L1,10,High
1,L4,15,High
2,L2,20,Medium
```

---

###  2. Agent Distance Summary (`summary_*.csv`) ⭐

Includes total workload per agent:

```
Agent,Total Distance
1,25
2,45
3,42
```

✔ Ensures requirement: *“total distance per agent”*

---

###  3. Visualization Outputs

* Distance comparison plot
* Metrics comparison plot

---

###  4. Final Report

* `comparison_report.csv`
* Contains performance comparison across all test cases

---

##  Edge Case Testing

The system was tested on multiple edge cases:

* All high priority deliveries
* Same distance values
* Extremely large distance values
* Skewed priority distribution
* Minimum dataset
* Large dataset

✔ Ensures robustness and reliability

---

##  Project Structure

```
DeliveryOptimization/
│
├── input/                   # Input CSV files
├── output/                  # Generated outputs
├── main.py                  # Main execution file
├── utils.py                 # Core logic functions
├── README.md                # Documentation
├── comparison_report.csv    # Final comparison report
```

---

##  How to Run

### 1. Install required libraries:

```
pip install pandas numpy matplotlib scikit-learn
```

### 2. Run the program:

```
python main.py
```

---

##  Features

✔ Multi-algorithm approach
✔ Automated decision-making
✔ Visualization support
✔ Handles multiple datasets
✔ Edge case validation
✔ Scalable and efficient

---

##  Key Concepts Used

* Greedy Algorithms
* K-Means Clustering
* Load Balancing
* Multi-Criteria Decision Making (MCDM)
* Data Analysis & Visualization

---

##  Conclusion

This project demonstrates how combining multiple optimization techniques with decision-making strategies can significantly improve logistics efficiency. The system dynamically selects the best approach based on real-world conditions, making it robust, scalable, and efficient.

---

##  Submitted By

**Sowbagya V S**
**Reg No: 2303717673722049**
