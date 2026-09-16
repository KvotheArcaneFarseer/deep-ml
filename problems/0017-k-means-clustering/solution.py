import numpy as np


def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    # Work with a mutable copy of the initial centroids
    centroids = [list(centroid) for centroid in initial_centroids]

    for schlatt in range(max_iterations):

        # Create one empty cluster for each centroid
        clusters = [[] for lisst in range(k)]

        # Assign every point to its nearest centroid
        for eachpt in range(len(points)):

            clus = []

            # Calculate distance from this point to every centroid
            for centr in range(len(centroids)):

                sqrd_list = []

                for dimen in range(len(points[0])):
                    diff = points[eachpt][dimen] - centroids[centr][dimen]
                    squared_diff = diff**2
                    sqrd_list.append(squared_diff)

                distance = np.sqrt(np.sum(sqrd_list))
                clus.append(distance)

            # Find which centroid has the smallest distance
            min_index = np.argmin(clus)

            # Assign the actual point to that cluster
            clusters[min_index].append(points[eachpt])

        # Calculate new centroids
        mean_centr = []

        for dimens in range(len(clusters)):

            # If cluster is empty, keep its previous centroid
            if len(clusters[dimens]) == 0:
                eachpt_dmean = centroids[dimens].copy()

            else:
                eachpt_dmean = []

                # Calculate mean for each coordinate
                for pt_col in range(len(points[0])):

                    mean_num = []

                    for pt_row in range(len(clusters[dimens])):
                        mean_num.append(
                            clusters[dimens][pt_row][pt_col]
                        )

                    eachpt_dmean.append(np.mean(mean_num))

            mean_centr.append(eachpt_dmean)

        # Stop early if the centroids no longer move
        if np.allclose(centroids, mean_centr):
            centroids = mean_centr
            break

        # Otherwise, use the new centroids for the next iteration
        centroids = mean_centr

    # Convert each centroid to a rounded tuple
    final_centroids = []

    for centroid in centroids:
        rounded_centroid = tuple(
            round(float(value), 4) for value in centroid
        )
        final_centroids.append(rounded_centroid)

    return final_centroids