# DeadlockGuard
### Deadlock Detection and Avoidance Simulator

## 🚀 Live Demo

Try the project here: **[DeadlockGuard Live Website](https://deadlockguard-rdhd.onrender.com)**

**GitHub Repository:** [DeadlockGuard](https://github.com/ashutoshsakolkar/DeadlockGuard)

## 📖 About the Project

Deadlocks are a common problem in operating systems when multiple processes compete for resources and end up waiting for one another. Understanding how operating systems handle these situations can be difficult when learning only from theory.

**DeadlockGuard** is a web-based project that makes these concepts easier to understand through interactive simulations. It allows users to experiment with resource allocation, check whether a system is safe, detect deadlocks, and explore different ways of handling resource requests.

The project is built using Python and Flask for the backend, with HTML, CSS, and JavaScript providing the user interface.

## ✨ What Can You Do With DeadlockGuard?

### 1. Banker's Algorithm
Check whether the system is in a safe state before resources are allocated.

- Calculate the Need matrix.
- Find a safe sequence if one exists.
- Understand how the available resources affect process execution.

### 2. Resource Request Evaluation
Ever wondered what happens when a process requests additional resources? This section lets you test it.

- Enter a process ID and its resource request.
- Check whether the requested resources are available.
- Evaluate whether granting the request keeps the system in a safe state.
- View the decision and resulting allocation information.

### 3. Deadlock Detection
Sometimes, processes get stuck waiting for resources that cannot be released. This module helps identify such situations.

- Analyse available resources and current allocations.
- Enter the outstanding request matrix.
- Identify processes that cannot finish under the current conditions.

### 4. PARAH Recommendation
PARAH stands for **Priority-Aware Resource Allocation Heuristic**. It is a proposed approach in this project for ranking pending resource requests.

- Compare pending requests from different processes.
- Rank requests using a scoring function.
- View recommended requests and their associated safe sequences.

The goal is to explore whether prioritising requests using a simple heuristic can help with resource-allocation decisions.

*PARAH is a rule-based heuristic, not a trained machine-learning model.*

### 5. DeadlockGuard Flexibility Analysis
A system may be safe but still have limited options for progressing with its current resource allocation. This module explores that aspect.

- Analyse the current allocation state.
- Count unfinished processes that can proceed immediately.
- Calculate a flexibility score based on the proportion of unfinished processes that are currently eligible to proceed.

The score is intended as a simple indicator of resource-allocation flexibility, not a probability of deadlock.

### 6. 🎲 Generate Random Dataset
Testing every scenario manually can take time, so DeadlockGuard includes a random dataset generator.

- Generate new input values with a single click.
- Update the inputs across all five modules.
- Experiment with different numbers of processes and resource types.
- Clear previous analysis results before testing the new dataset.

Once the new values are generated, run the analysis in each module to see how the system responds.

## 🛠️ Technologies Used

- **Python** – Implements the backend logic and algorithms.
- **Flask** – Connects the backend with the web interface.
- **HTML** – Structures the application.
- **CSS** – Handles the layout and styling.
- **JavaScript** – Makes the interface interactive and generates random datasets.
- **Git and GitHub** – Used for version control and project hosting.
- **Render** – Hosts the live application.

## 📁 Project Structure

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

## 💻 Running the Project Locally

Want to run DeadlockGuard on your own computer? Follow these steps.

### Prerequisites
- Python 3
- pip
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/ashutoshsakolkar/DeadlockGuard.git
```

### Step 2: Open the project folder

```bash
cd DeadlockGuard
```

### Step 3: Install the required packages

```bash
pip install -r requirements.txt
```

### Step 4: Start the application

```bash
python app.py
```

If you're using Windows and the `python` command doesn't work, try:

```powershell
py app.py
```

### Step 5: Open the website

Visit the following address in your browser:

```text
http://127.0.0.1:5000/
```

That's it! You can now experiment with the different modules locally.

## 🧪 How to Test It

1. Open DeadlockGuard.
2. Enter your own resource-allocation values or click **Generate Random Dataset**.
3. Use Banker's Algorithm to check whether the system is safe.
4. Test a resource request and see whether it can be granted.
5. Run Deadlock Detection to check for deadlocked processes.
6. Explore PARAH to compare pending resource requests.
7. Use Flexibility Analysis to examine how many unfinished processes can proceed immediately.
8. Generate another dataset and repeat the process with different inputs.

## 🎯 What We Wanted to Achieve

The main idea behind DeadlockGuard was to make operating-system resource management more interactive and easier to experiment with.

Through this project, we explored:
- How operating systems allocate resources to processes.
- How safe and unsafe states are identified.
- How deadlocks can be detected.
- How resource requests can be evaluated.
- How a heuristic can be used to rank pending requests.
- How current resource availability affects a system's flexibility.

## ⚠️ A Few Things to Keep in Mind

- An unsafe state does not automatically mean that a deadlock has occurred.
- A request can be rejected because resources are unavailable or granting it would make the system unsafe.
- Random datasets are intended for experimentation, and different inputs can produce different results.
- PARAH and the flexibility score are heuristic approaches; they do not guarantee optimal resource allocation.

## 👨‍💻 Author

**Ashutosh Sakolkar**

---

*Built as an Operating Systems project to explore deadlock detection, avoidance, and resource management through interactive simulations.*
