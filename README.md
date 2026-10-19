# DeadlockGuard
### Deadlock Detection and Avoidance Simulator

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://deadlockguard-rdhd.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-black)](https://flask.palletsprojects.com/)

## 🚀 Live Demo

**[Open DeadlockGuard](https://deadlockguard-rdhd.onrender.com)**

**GitHub Repository:** [DeadlockGuard](https://github.com/ashutoshsakolkar/DeadlockGuard)

## 📌 Project Overview

DeadlockGuard is a web-based Operating Systems project designed to demonstrate resource allocation, system safety, deadlock detection, and resource request prioritization.

The application uses Python and Flask for backend processing and HTML, CSS, and JavaScript for its interactive web interface.

It provides an environment for exploring how operating systems manage competing resource requests, determine safe execution sequences, identify deadlocked processes, and evaluate resource allocation decisions.

## ✨ Features

### 1. Banker's Algorithm
- Calculates the Need matrix using Maximum and Allocation matrices.
- Determines whether the system is in a safe state.
- Displays a safe sequence when one exists.
- Helps demonstrate deadlock avoidance through safe-state analysis.

### 2. Resource Request Evaluation
- Evaluates resource requests made by individual processes.
- Checks whether sufficient resources are available.
- Evaluates whether granting a request would preserve system safety.
- Displays the request decision and resulting allocation information.

### 3. Deadlock Detection
- Analyses available resources, current allocations, and outstanding requests.
- Simulates the deadlock detection algorithm.
- Identifies processes involved in a detected deadlock.
- Helps distinguish between processes that can finish and those that remain blocked.

### 4. PARAH Recommendation
- Implements a proposed **Priority-Aware Resource Allocation Heuristic (PARAH)**.
- Ranks pending resource requests using a heuristic scoring function.
- Considers process resource needs and current allocations.
- Presents recommended requests and associated safe-sequence information.

**Note:** PARAH is a rule-based heuristic, not a trained machine-learning model.

### 5. DeadlockGuard Flexibility Analysis
- Analyses the system's current resource-allocation state.
- Evaluates how many unfinished processes can proceed with the currently available resources.
- Calculates a flexibility score based on the proportion of unfinished processes that are immediately eligible to proceed.
- Provides a heuristic indication of current resource-allocation flexibility.

**Note:** The flexibility score is a heuristic indicator, not a probability of deadlock.

### 6. 🎲 Random Dataset Generator
- Generates new random input values for the simulator.
- Updates the input fields across all five modules.
- Creates datasets with varying numbers of processes and resource types.
- Makes it easier to test different resource-allocation scenarios without manually entering every value.
- Clears previous analysis results so the new dataset can be evaluated independently.

After generating a dataset, run the relevant analysis in each module to view its results.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Operating Systems Algorithms | Banker's Algorithm, Resource Request Evaluation, Deadlock Detection |
| Proposed Heuristic | PARAH |
| Testing | Python test scripts |
| Version Control | Git, GitHub |
| Deployment | Render |

## 📂 Project Structure

```text
OS Deadlock Simulator/
├── app.py
├── algorithms.py
├── requirements.txt
├── Procfile
├── test_algorithms.py
├── test_new_functions.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

Additional local experiment files, such as benchmark scripts and simulation outputs, may exist outside the tracked project structure.

## ⚙️ Run Locally

### Prerequisites
- Python 3
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/ashutoshsakolkar/DeadlockGuard.git
```

### 2. Navigate to the project directory

```bash
cd DeadlockGuard
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask application

```bash
python app.py
```

If `python` is not recognized on Windows, try:

```powershell
py app.py
```

### 5. Open the application

Visit:

```text
http://127.0.0.1:5000/
```

## 🧪 How to Use

1. Open DeadlockGuard.
2. Enter or generate resource-allocation data.
3. Use **Banker's Algorithm** to check system safety.
4. Use **Resource Request Evaluation** to assess an individual request.
5. Use **Deadlock Detection** to analyse outstanding requests.
6. Use **PARAH Recommendation** to rank pending requests.
7. Use **DeadlockGuard Flexibility Analysis** to inspect current allocation flexibility.
8. Click **Generate Random Dataset** to populate all five modules with new input values and explore another scenario.

## 🎯 Project Objectives

- Demonstrate operating-system resource allocation concepts.
- Understand safe and unsafe resource-allocation states.
- Explore resource request evaluation and deadlock detection.
- Experiment with heuristic-based request prioritization.
- Analyse resource-allocation flexibility.
- Provide an interactive interface for testing different scenarios.

## ⚠️ Important Notes

- An unsafe state does not necessarily mean that a deadlock has already occurred.
- A resource request may be rejected because it exceeds the available resources or would make the system unsafe.
- Randomly generated datasets are intended for experimentation; their outcomes depend on the generated inputs.
- PARAH and the flexibility score are heuristic approaches and should not be interpreted as guaranteed optimal decisions or probabilities.

## 👨‍💻 Author

**Ashutosh Sakolkar**

## 📄 License

Add a license to this repository if you intend to distribute the project under specific reuse permissions.
