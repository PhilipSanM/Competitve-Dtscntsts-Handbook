# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=--=-=-=-=-=-= K-Means -=-=-=-=-===-=-=-=-=-=-=-=-=-==-=-=-=-=-=-
# =-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# ML Coding Questions
# Date: 6 - October - 2023
# AlgoExpers = https://www.algoexpert.io/machine-learning/coding-questions/k-means

# My solution

# T:O(iknf) | S:O(kn)

#     i = iterations ; k = clusters ; n = users ; f = features

import random


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    # Declare coordinates of centroids:
    centroids = [
        Centroid(user_feature_map[initial_centroid])
        for initial_centroid in inital_centroid_users
    ]

    # iterartions
    iterations = 10
    while iterations > 0:
        iterations -= 1

        # Calculate users to centroids
        for uid, features in user_feature_map.items():
            closest_centroid = None
            closest_distance = float("inf")

            for centroid in centroids:
                curr_distance = get_manhattan_distance(features, centroid.location)
                if curr_distance < closest_distance:
                    closest_centroid = centroid
                    closest_distance = curr_distance

            closest_centroid.closest_users.add(uid)

        #  Update average
        for centroid in centroids:
            centroid.location = get_average(
                centroid, user_feature_map, num_features_per_user
            )
            # clear again
            centroid.closest_users = set()

    return [centroid.location for centroid in centroids]


def get_manhattan_distance(features, other_features):
    distance = 0
    for i in range(len(features)):
        distance += abs(features[i] - other_features[i])

    return distance


def get_average(centroid, user_feature_map, size_features):
    new_features = [0] * size_features

    for user in centroid.closest_users:
        total_users = len(centroid.closest_users)
        for i in range(len(new_features)):
            new_features[i] += user_feature_map[user][i] / total_users

    return new_features
