'''
DSCI 401 -- Assignment #3, kNN Classifier
Sandra Shtabnaya, University of Mary Washington, spring 2020
'''

import numpy as np
import pandas as pd
import queue
from statistics import mode


class KNN:

    def __init__(self, k, distance_func):
        self.k = k
        self.get_distance = distance_func
        self.training_data = np.array([])
        self.training_labels = np.array([])

    def fit(self, data, labels):
        self.training_labels = labels
        self.training_data = data

        if isinstance(data, pd.DataFrame):
            self.training_data = data.values

        if isinstance(labels, pd.DataFrame):
            self.training_labels = labels.values

    def predict(self, data):
        predictions = np.array([])

        if isinstance(data, pd.DataFrame):
            data = data.values

        # for each test observation to predict
        for test_x in data:
            distances = queue.PriorityQueue()

            # compare test observation against all training observations
            for (index, train_x) in enumerate(self.training_data):
                distance = self.get_distance(test_x, train_x)
                distances.put((distance, self.training_labels[index]))  # queue pushes distances in order

            labels = []  # stores labels for k-nearest neighbors
            for neighbor in range(self.k):
                labels.append(distances.get()[1])  # queue pops off smallest distances

            # adds most common label in k-nearest to predictions
            predictions = np.append(predictions, [mode(labels)], axis=0)

        return predictions
