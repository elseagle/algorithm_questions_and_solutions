from functools import reduce
import itertools
from re import sub
import re

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

people_dict = {}
people_counter = 0
all_checkers = []

# logic to get what topics folks are knowledgeable about
def extract_positions(topic_):
    global people_counter, people_dict
    people_counter += 1
    knowledgeable_about = [m.start() for m in re.finditer("1", topic_)]
    people_dict[people_counter] = []
    people_dict[people_counter].extend(knowledgeable_about)


def get_intersection(combination):
    global all_checkers, people_dict
    i, j = combination

    # find the union of knowledge between a pair of participants
    intersection = set(people_dict[int(i)]).union(set(people_dict[int(j)]))
    all_checkers.append(len(intersection))


def acmTeam(topic):
    global people_dict, all_checkers

    _ = list(map(extract_positions, topic))

    all_checkers = []
    all_combinations = list(
        itertools.product(range(1, len(topic) + 1), range(1, len(topic) + 1))
    )
    # necessary conditions to filter out unneeded values
    all_combinations = list(
        filter(
            lambda x: x[0] <= len(topic[1]) and x[1] <= len(topic) and x[0] != x[1],
            all_combinations,
        )
    )

    # drop duplicate tuple - using frozen set b/c tuples are not hashable
    all_combinations = list(
        set(list(set(frozenset(set(item)) for item in all_combinations)))
    )
    _ = list(map(get_intersection, all_combinations))

    return [len(topic[1]), all_checkers.count(len(topic[1]))]


# N.B: Run one testcase at a time to get correct output

# print(acmTeam(["10101", "11110", "00010", "00101"]))
print(acmTeam(["11101", "10101", "11001", "10111", "10000", "01110"]))
