import random
import time
from algorithms import analyze_flexibility

random.seed(42)

TOTAL_SCENARIOS = 1000

safe_count = 0
unsafe_count = 0
low_count = 0
moderate_count = 0
high_count = 0

flexibility_scores = []
execution_times = []

for _ in range(TOTAL_SCENARIOS):

    process_count = random.randint(3, 8)
    resource_count = random.randint(2, 4)

    # Generate a resource allocation state
    maximum = []
    allocation = []

    for _ in range(process_count):
        max_row = [
            random.randint(1, 8)
            for _ in range(resource_count)
        ]

        alloc_row = [
            random.randint(0, value)
            for value in max_row
        ]

        maximum.append(max_row)
        allocation.append(alloc_row)

    # Generate available resources
    available = [
        random.randint(0, 8)
        for _ in range(resource_count)
    ]

    start = time.perf_counter()

    result = analyze_flexibility(
        available,
        maximum,
        allocation
    )

    elapsed_ms = (time.perf_counter() - start) * 1000

    execution_times.append(elapsed_ms)
    flexibility_scores.append(result["flexibility_score"])

    if result["safe"]:
        safe_count += 1
    else:
        unsafe_count += 1

    if result["risk_level"] == "LOW":
        low_count += 1
    elif result["risk_level"] == "MODERATE":
        moderate_count += 1
    else:
        high_count += 1


print("\n===== DEADLOCKGUARD BENCHMARK =====")
print("Total scenarios:", TOTAL_SCENARIOS)

print(
    f"Safe states: {safe_count} "
    f"({safe_count / TOTAL_SCENARIOS * 100:.2f}%)"
)

print(
    f"Unsafe states: {unsafe_count} "
    f"({unsafe_count / TOTAL_SCENARIOS * 100:.2f}%)"
)

print(
    f"Low-risk classifications: {low_count} "
    f"({low_count / TOTAL_SCENARIOS * 100:.2f}%)"
)

print(
    f"Moderate-risk classifications: {moderate_count} "
    f"({moderate_count / TOTAL_SCENARIOS * 100:.2f}%)"
)

print(
    f"High-risk classifications: {high_count} "
    f"({high_count / TOTAL_SCENARIOS * 100:.2f}%)"
)

print(
    "Average flexibility score:",
    round(sum(flexibility_scores) / TOTAL_SCENARIOS, 4)
)

print(
    "Average analysis time (ms):",
    round(sum(execution_times) / TOTAL_SCENARIOS, 6)
)

print(
    "Maximum analysis time (ms):",
    round(max(execution_times), 6)
)