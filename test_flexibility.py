from algorithms import analyze_flexibility

# Scenario A: More immediately eligible processes
available_a = [3, 2]

maximum = [
    [3, 2],
    [2, 2],
    [4, 3],
    [2, 1]
]

allocation = [
    [1, 1],
    [1, 0],
    [1, 1],
    [0, 1]
]

# Scenario B: Fewer immediately eligible processes
available_b = [2, 1]

for name, available in [
    ("Scenario A", available_a),
    ("Scenario B", available_b)
]:
    result = analyze_flexibility(
        available,
        maximum,
        allocation
    )

    print(f"\n===== {name} =====")
    print("Available:", available)
    print("Safe:", result["safe"])
    print("Eligible processes:", result["eligible_processes"])
    print("Flexibility score:", result["flexibility_score"])
    print("Risk level:", result["risk_level"])
    print("Warning:", result["warning"])