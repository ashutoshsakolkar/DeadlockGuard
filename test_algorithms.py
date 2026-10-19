from algorithms import (
    calculate_need,
    bankers_algorithm,
    detect_deadlock
)

def test_calculate_need():
    maximum = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2]
    ]

    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2]
    ]

    expected = [
        [7, 4, 3],
        [1, 2, 2],
        [6, 0, 0]
    ]

    result = calculate_need(maximum, allocation)

    assert result == expected, f"Expected {expected}, got {result}"

    print("TEST 1 PASSED: Need matrix calculation")



def test_banker_safe():
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

    result = bankers_algorithm(available, maximum, allocation)

    assert result["safe"] is True, "Expected a SAFE state"

    sequence = result["safe_sequence"]

    assert len(sequence) == 5, "All processes must be in the sequence"
    assert len(set(sequence)) == 5, "A process must not appear twice"

    print("TEST 2 PASSED: Banker's Algorithm detects a safe state")
    print("Safe sequence:", " -> ".join(sequence))



def test_banker_unsafe():
    available = [0]

    maximum = [
        [2],
        [2]
    ]

    allocation = [
        [1],
        [1]
    ]

    result = bankers_algorithm(available, maximum, allocation)

    assert result["safe"] is False, "Expected an UNSAFE state"

    print("TEST 3 PASSED: Banker's Algorithm detects an unsafe state")



def test_deadlock_detected():
    available = [0, 0]

    allocation = [
        [1, 0],
        [0, 1]
    ]

    request = [
        [0, 1],
        [1, 0]
    ]

    result = detect_deadlock(available, allocation, request)

    assert result["deadlock"] is True
    assert result["deadlocked_processes"] == ["P0", "P1"]

    print("TEST 4 PASSED: Deadlock correctly detected")



def test_no_deadlock():
    available = [1, 0]

    allocation = [
        [0, 1],
        [1, 0]
    ]

    request = [
        [0, 0],
        [0, 1]
    ]

    result = detect_deadlock(available, allocation, request)

    assert result["deadlock"] is False

    print("TEST 5 PASSED: No-deadlock state correctly identified")


if __name__ == "__main__":

    tests = [
        test_calculate_need,
        test_banker_safe,
        test_banker_unsafe,
        test_deadlock_detected,
        test_no_deadlock
    ]

    print("\n===== DEADLOCKGUARD TESTING =====\n")

    for test in tests:
        test()

    print("\n===== ALL TESTS PASSED SUCCESSFULLY =====")