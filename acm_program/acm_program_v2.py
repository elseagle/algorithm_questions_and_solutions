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

people_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
people_counter = 0
def extract_positions(topic_):
        global people_counter, people_dict
        people_counter +=1
        knowledgeable_about = [m.start() for m in re.finditer('1', topic_)]
        people_dict[people_counter] = []
        people_dict[people_counter].extend(knowledgeable_about)

def acmTeam(topic):
    # Write your code here
    global people_dict
    
    _ = list(map(extract_positions, topic))

    all_checkers = []
    pair_holder = []
    all_combinations = list(itertools.product(range(1, len(topic) + 1), range(1, len(topic) + 1)))
    for i,j in all_combinations:

            if (
                i <= len(topic[1])
                and j <= len(topic)
                and i != j
                and [i, j] not in pair_holder
                and [j, i] not in pair_holder
            ):
                person_i_set = set(people_dict[i])
                person_j_set = set(people_dict[j])
                intersection = person_i_set.union(person_j_set)
                pair_holder.append([i, j])
                all_checkers.append(len(intersection))

    print(all_checkers)

    return [len(topic[1]), all_checkers.count(len(topic[1]))]


print(acmTeam(["10101", "11110", "00010", "00101"]))
# print(acmTeam(["11101", "10101", "11001", "10111", "10000", "01110"]))
