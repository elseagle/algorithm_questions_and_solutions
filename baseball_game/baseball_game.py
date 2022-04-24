def calculate_points(ops: list) -> int:
    """
    ops: List of operations
    """
    record = []
    for val in ops:
        if val.isdigit():
            record.append(int(val))
        elif val == "+":
            record.append(record[-1] + record[-2])
        elif val == "C":
            record.pop()
        elif val == "D":
            record.append(record[-1] * 2)
    return sum(record)


if __name__ == "__main__":
    print(calculate_points(["9", "D", "2", "5", "+"])) # TODO: expected_output : 
    print(calculate_points(["5", "2", "+", "7", "7", "2"])) # TODO: expected_output : 30
    print(calculate_points(["2", "9", "D", "5", "C"])) # TODO: expected_output : 30
    print(calculate_points(["5", "2", "+", "5", "8", "6", "+", "C"])) # TODO: expected_output : 30
    print(calculate_points(["8", "C", "2", "1", "+"])) # TODO: expected_output : 30
    print(calculate_points(["9", "8", "4", "5", "D"])) # TODO: expected_output : 30
    print(calculate_points(["5", "2", "C", "D", "+"])) # expected_output : 30
