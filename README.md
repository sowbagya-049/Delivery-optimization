# Delivery Optimization System

## Overview

This project focuses on solving a **Logistics Delivery Optimization Problem** using advanced decision-making techniques. The system processes delivery data and assigns tasks to agents efficiently while balancing workload and prioritizing urgent deliveries.

---

## Objectives

* Read delivery data from CSV files
* Prioritize deliveries based on urgency
* Optimize assignment across 3 agents
* Minimize total travel distance imbalance
* Compare multiple optimization techniques
* Select the best method dynamically

---

## Input Format

Each input CSV file must contain:

| Column Name             | Description                    |
| ----------------------- | ------------------------------ |
| Location ID             | Unique identifier for location |
| Distance from warehouse | Distance value                 |
| Delivery Priority       | High / Medium / Low            |

---

## Algorithms Used

### 🔹 1. Greedy + Priority Weighting

* Assigns priority values (High=3, Medium=2, Low=1)
* Computes score = Priority / Distance
* Sorts deliveries based on score
* Assigns tasks to agent with minimum distance

✔ Fast and efficient
✔ Ensures priority handling

---

### 🔹 2. K-Means Clustering

* Groups locations into 3 clusters
* Each cluster assigned to an agent
* Minimizes travel distance naturally

✔ Good for spatial grouping
✔ Balanced clustering approach

---

## Decision Technique

A **Multi-Criteria Decision Making (MCDM)** approach is used to select the best method based on:

* Variance → Load balancing
* Maximum Distance → Workload fairness
* Priority Score → Urgency handling

### Decision Formula:

Score = 0.5 × Variance + 0.3 × Max Distance − 0.2 × Priority Score

Lower score = Better method

---

## Workflow

1. Read all input CSV files
2. Apply both algorithms
3. Calculate performance metrics
4. Compare results
5. Select best method
6. Generate outputs and plots

---

## Output Files

For each input file:

* Optimized delivery plan (`output_*.csv`)
* Distance comparison plot
* Metrics comparison plot

### Final Output:

* `comparison_report.csv`

---

## Edge Case Testing

The system was tested on multiple edge cases:

* All high priority deliveries
* Same distance values
* Extremely large distance values
* Skewed priority distribution
* Minimum dataset
* Large dataset

✔ Ensures robustness and reliability

---

## Project Structure

```
DeliveryOptimization/
│
├── input/              # Input CSV files
├── output/             # Generated outputs
├── main.py             # Main execution file
├── utils.py            # Core logic functions
├── README.md           # Documentation
├── comparison_report.csv
```

---

## How to Run

1. Install required libraries:

```
pip install pandas numpy matplotlib scikit-learn
```

2. Run the program:

```
python main.py
```

---

## Features

✔ Multi-algorithm approach
✔ Automated decision-making
✔ Visualization support
✔ Handles multiple datasets
✔ Edge case validation
✔ Scalable and efficient

---

## Key Concepts Used

* Greedy Algorithms
* Clustering (K-Means)
* Load Balancing
* Multi-Criteria Decision Making
* Data Analysis & Visualization

---

## Conclusion

This project demonstrates how combining multiple optimization techniques with decision-making strategies can significantly improve logistics efficiency. The system dynamically selects the best approach based on real-world conditions, making it robust and adaptable.

---

## Submitted By

Sowbagya V S - 
2303717673722049
