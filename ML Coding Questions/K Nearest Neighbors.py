# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-= K Nearest Neighbors =-=-=-=-=-=-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Algo Experts
# Date: 1 - October - 2023
# Leetcode link = https://www.algoexpert.io/machine-learning/coding-questions/k-nearest-neighbors

# My solution


# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    # Write your code here.

    # First step: find Euclidean distance
    distances = {}
    for pid in examples:
        distance = 0
        i = 0
        for data in examples[pid]["features"]:
            distance += (data - features[i]) ** 2
            i += 1

        distance = distance**0.5

        distances[distance] = examples[pid][label_key]

    # second step: sort values
    sort_data = sorted(distances)

    # find the K
    votes = []
    for i in range(k):
        votes.append(sort_data[i])

    # Count votes
    is_intransitive = 0
    no_intransitive = 0
    for vote in votes:
        if distances[vote] == 1:
            is_intransitive += 1
        else:
            no_intransitive += 1

    return 1 if is_intransitive > no_intransitive else 0


def find_k_nearest_neighbors(examples, features, k):
    # Write your code here.
    nearests_neighbors = {}

    for pid in examples:
        distance = 0
        i = 0

        for data in examples[pid]["features"]:
            distance += (data - features[i]) ** 2
            i += 1

        distance = distance**0.5

        if len(nearests_neighbors) < k:
            nearests_neighbors[distance] = pid
        else:
            distances = sorted(nearests_neighbors)

            if distances[-1] >= distance:
                nearests_neighbors.pop(distances[-1])
                nearests_neighbors[distance] = pid
    answ = []
    for _, ans in nearests_neighbors.items():
        answ.append(ans)

    return answ


# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-= K Nearest Neighbors =-=-=-=-=-=-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Algo Experts
# Date: 5 - October - 2023
# Leetcode link = https://www.algoexpert.io/machine-learning/coding-questions/k-nearest-neighbors

# Efficient solution
# T:O(n) | S:O(n)

import math


# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    # Write your code here.
    k_nn = find_k_nearest_neighbors(examples, features, k)
    votes = [examples[key][label_key] for key in k_nn]

    return round(sum(votes) / k)


def find_k_nearest_neighbors(examples, features, k):
    # Write your code here.

    distances = {}

    for pid, features_label_map in examples.items():
        distance = get_euclidean_distance(features, features_label_map["features"])
        distances[pid] = distance
    return sorted(distances, key=distances.get)[:k]


def get_euclidean_distance(features, other_features):
    diferences = []
    for i in range(len(features)):
        diferences.append((features[i] - other_features[i]) ** 2)

    return (sum(diferences)) ** (0.5)
