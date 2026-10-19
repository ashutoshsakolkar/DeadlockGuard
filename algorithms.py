def calculate_need(maximum, allocation):
    """
    Calculate the remaining resources required by each process.
    Need = Maximum - Allocation
    """
    need = []

    for i in range(len(maximum)):
        row = []
        for j in range(len(maximum[i])):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)

    return need


def bankers_algorithm(available, maximum, allocation):
    """
    Check whether the system is in a safe state
    using Banker's Algorithm.
    """

    process_count = len(allocation)
    resource_count = len(available)

    need = calculate_need(maximum, allocation)

    work = available.copy()
    finish = [False] * process_count
    safe_sequence = []

    while len(safe_sequence) < process_count:
        found = False

        for i in range(process_count):
            if not finish[i]:
                can_execute = True

                for j in range(resource_count):
                    if need[i][j] > work[j]:
                        can_execute = False
                        break

                if can_execute:
                    for j in range(resource_count):
                        work[j] += allocation[i][j]

                    safe_sequence.append(f"P{i}")
                    finish[i] = True
                    found = True

        if not found:
            break

    if len(safe_sequence) == process_count:
        return {
            "safe": True,
            "safe_sequence": safe_sequence,
            "need": need,
            "message": "The system is in a SAFE state."
        }

    return {
        "safe": False,
        "safe_sequence": safe_sequence,
        "need": need,
        "message": "The system is in an UNSAFE state."
    }


def detect_deadlock(available, allocation, request):
    """
    Detect deadlock using current resource allocations
    and outstanding resource requests.

    Assumes each resource type has a single instance.
    For multiple instances, the algorithm uses the
    standard reduction procedure.
    """

    process_count = len(allocation)
    resource_count = len(available)

    work = available.copy()

    finish = [
        all(allocation[i][j] == 0 for j in range(resource_count))
        for i in range(process_count)
    ]

    unfinished = [
        i for i in range(process_count) if not finish[i]
    ]

    while True:
        found = False

        for i in unfinished:
            if finish[i]:
                continue

            if all(
                request[i][j] <= work[j]
                for j in range(resource_count)
            ):
                for j in range(resource_count):
                    work[j] += allocation[i][j]

                finish[i] = True
                found = True

        if not found:
            break

    deadlocked_processes = [
        f"P{i}" for i in range(process_count) if not finish[i]
    ]

    return {
        "deadlock": len(deadlocked_processes) > 0,
        "deadlocked_processes": deadlocked_processes,
        "message": (
            "Deadlock detected."
            if deadlocked_processes
            else "No deadlock detected."
        )
    }


# RESOURCE REQUEST VALIDATION


def request_resources(
    process_id,
    request,
    available,
    maximum,
    allocation
):
    """
    Evaluate a resource request using Banker's Algorithm.
    Grant the request only if the resulting state is safe.
    """

    process_count = len(allocation)
    resource_count = len(available)

    # Validate process ID
    if not isinstance(process_id, int) or not (
        0 <= process_id < process_count
    ):
        raise ValueError("Invalid process ID.")

    # Calculate remaining need
    need = calculate_need(maximum, allocation)

    # Validate request dimensions and values
    if not isinstance(request, list) or len(request) != resource_count:
        raise ValueError("Request dimensions are incorrect.")

    if any(type(value) is not int or value < 0 for value in request):
        raise ValueError("Requests must contain non-negative integers.")

    # Check whether request exceeds declared need
    for j in range(resource_count):
        if request[j] > need[process_id][j]:
            return {
                "granted": False,
                "reason": "Request exceeds remaining process need."
            }

    # Check whether resources are available
    for j in range(resource_count):
        if request[j] > available[j]:
            return {
                "granted": False,
                "reason": "Insufficient resources. Request must wait."
            }

    # Simulate allocation without modifying original data
    new_available = [
        available[j] - request[j]
        for j in range(resource_count)
    ]

    new_allocation = [row.copy() for row in allocation]

    for j in range(resource_count):
        new_allocation[process_id][j] += request[j]

    # Check safety of the simulated state
    result = bankers_algorithm(
        new_available,
        maximum,
        new_allocation
    )

    if not result["safe"]:
        return {
            "granted": False,
            "reason": "Request would make the system unsafe."
        }

    return {
        "granted": True,
        "reason": "Request can be granted safely.",
        "safe_sequence": result["safe_sequence"],
        "available_after": new_available,
        "allocation_after": new_allocation
    }


# PARAH: PRIORITY-AWARE RESOURCE ALLOCATION
# HEURISTIC


def parah_recommendation(
    available,
    maximum,
    allocation,
    pending_requests
):
    """
    Rank safe resource requests using a simple heuristic.

    Lower scores receive higher priority.
    """

    need = calculate_need(maximum, allocation)

    ranked_requests = []
    rejected_requests = []

    for item in pending_requests:

        process_id = item["process_id"]
        requested = item["request"]

        result = request_resources(
            process_id,
            requested,
            available,
            maximum,
            allocation
        )

        if not result["granted"]:
            rejected_requests.append({
                "process_id": process_id,
                "request": requested,
                "reason": result["reason"]
            })
            continue

        # Proposed heuristic scoring function
        remaining_need = sum(need[process_id])
        allocated_resources = sum(allocation[process_id])

        score = remaining_need + 0.5 * allocated_resources

        ranked_requests.append({
            "process_id": process_id,
            "request": requested,
            "score": score,
            "safe_sequence": result["safe_sequence"]
        })

    # Lowest score receives highest priority
    ranked_requests.sort(
        key=lambda item: (item["score"], item["process_id"])
    )

    return {
        "recommended_request": (
            ranked_requests[0] if ranked_requests else None
        ),
        "ranked_safe_requests": ranked_requests,
        "rejected_requests": rejected_requests,
        "message": (
            "Safe requests ranked successfully."
            if ranked_requests
            else "No safe pending requests are available."
        )
    }