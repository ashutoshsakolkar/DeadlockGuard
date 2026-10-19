from algorithms import request_resources, parah_recommendation


available = [3, 3, 2]

maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]


# Test 1: Safe resource request
result = request_resources(
    1, [1, 0, 2], available, maximum, allocation
)

assert result["granted"] is True
print("TEST 1 PASSED: Safe resource request")


# Test 2: Request exceeding remaining need
result = request_resources(
    0, [8, 0, 0], available, maximum, allocation
)

assert result["granted"] is False
print("TEST 2 PASSED: Invalid resource request rejected")


# Test 3: PARAH ranks safe requests
pending_requests = [
    {"process_id": 1, "request": [1, 0, 2]},
    {"process_id": 3, "request": [0, 1, 0]}
]

result = parah_recommendation(
    available, maximum, allocation, pending_requests
)

assert len(result["ranked_safe_requests"]) == 2

scores = [
    item["score"]
    for item in result["ranked_safe_requests"]
]

assert scores == sorted(scores)

print("TEST 3 PASSED: PARAH ranks safe requests")
print("Recommended request:", result["recommended_request"])

print("\nALL NEW FUNCTION TESTS PASSED!")