# DeadlockGuard
## 🚀 Live Demo

**[Open DeadlockGuard](https://deadlockguard-rdhd.onrender.com)**

### Deadlock Detection and Avoidance Simulator

DeadlockGuard is a web-based Operating Systems project that demonstrates
resource allocation, system safety, deadlock detection, and heuristic-based
resource request prioritization.

The application uses Python and Flask for its backend and HTML, CSS, and
JavaScript for its interactive web interface.

## Features

### 1. Banker's Algorithm
- Calculates the Need matrix.
- Checks whether the system is in a safe state.
- Displays a safe sequence when one exists.

### 2. Resource Request Evaluation
- Evaluates a process's resource request.
- Checks resource availability and safety before granting a request.
- Displays the decision and resulting resource allocation.

### 3. Deadlock Detection
- Analyses available resources, current allocations, and outstanding requests.
- Identifies processes involved in a detected deadlock.

### 4. PARAH Recommendation
- Implements a proposed Priority-Aware Resource Allocation Heuristic.
- Ranks safe pending resource requests using a scoring function.
- Displays recommended requests and their associated safe sequences.

## Technology Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Algorithms:** Banker's Algorithm, resource request evaluation,
  deadlock detection, and PARAH heuristic
- **Version Control:** Git and GitHub

## Project Structure

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
