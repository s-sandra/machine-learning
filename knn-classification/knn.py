'''
DSCI 401 -- Assignment #3, kNN Classifier
Sandra Shtabnaya, University of Mary Washington, spring 2020
'''

import numpy as np
import pandas as pd


class KNN:
    def __init__(self, k, distance_func):
        self.k = k
        self.get_distance = distance_func

    def fit(self, data, labels):
        pass

    def predict(self, data):
        pass

    