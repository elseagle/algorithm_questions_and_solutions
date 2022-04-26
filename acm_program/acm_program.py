from functools import reduce
from re import sub

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#


def acmTeam(topic):
    # Write your code here
    subject_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
    counter = 0

    for positions in topic:
        counter += 1
        [
            subject_dict[pos_counter + 1].extend([counter])
            for pos_counter, pos in enumerate(positions)
            if pos == "1"
        ]

    all_checkers = []
    pair_holder = []
    for i in range(1, len(topic) + 1):
        for j in range(1, len(topic) + 1):

            if (
                i <= len(positions)
                and j <= len(topic)
                and i != j
                and [i, j] not in pair_holder
                and [j, i] not in pair_holder
            ):
                res_checker = [
                    val for val in subject_dict.values() if i in val or j in val
                ]
                # print(f"{i}, {j} >>", res_checker)
                pair_holder.append([i, j])
                all_checkers.append(len(res_checker))

    print(all_checkers)

    return [len(positions), all_checkers.count(len(positions))]


print(acmTeam(["10101", "11110", "00010", "00101"]))
# print(acmTeam(["11101", "10101", "11001", "10111", "10000", "01110"]))
