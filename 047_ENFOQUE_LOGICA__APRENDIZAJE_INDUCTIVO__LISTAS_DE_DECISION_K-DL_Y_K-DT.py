import numpy as np
from collections import Counter

class KDLClassifier:
    def __init__(self, k):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        y_pred = []
        for sample in X_test:
            distances = np.linalg.norm(self.X_train - sample, axis=1)
            indices = np.argsort(distances)[:self.k]
            k_nearest_labels = self.y_train[indices]
            most_common_label = Counter(k_nearest_labels).most_common(1)[0][0]
            y_pred.append(most_common_label)
        return np.array(y_pred)

class KDTClassifier:
    class Node:
        def __init__(self, value=None, feature=None, left=None, right=None):
            self.value = value
            self.feature = feature
            self.left = left
            self.right = right

    def __init__(self, k):
        self.k = k

    def build_kdtree(self, X_train, y_train, depth=0):
        if len(X_train) == 0:
            return None

        n_features = X_train.shape[1]
        axis = depth % n_features

        sorted_indices = X_train[:, axis].argsort()
        median_index = len(X_train) // 2

        node = self.Node()
        node.feature = axis
        node.value = X_train[sorted_indices[median_index]]

        left_X_train = X_train[sorted_indices[:median_index]]
        left_y_train = y_train[sorted_indices[:median_index]]
        right_X_train = X_train[sorted_indices[median_index + 1:]]
        right_y_train = y_train[sorted_indices[median_index + 1:]]

        node.left = self.build_kdtree(left_X_train, left_y_train, depth + 1)
        node.right = self.build_kdtree(right_X_train, right_y_train, depth + 1)

        return node

    def fit(self, X_train, y_train):
        self.root = self.build_kdtree(X_train, y_train)

    def _find_nearest_neighbor(self, node, sample):
        if node is None:
            return None

        axis = node.feature
        if sample[axis] <= node.value[axis]:
            next_node = node.left
            opposite_node = node.right
        else:
            next_node = node.right
            opposite_node = node.left

        if next_node is None:
            return node

        return self._find_nearest_neighbor(next_node, sample)

    def predict(self, X_test):
        y_pred = []
        for sample in X_test:
            nearest_neighbor = self._find_nearest_neighbor(self.root, sample)
            y_pred.append(nearest_neighbor.value)
        return np.array(y_pred)

# Ejemplo de uso
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([0, 1, 0, 1])

X_test = np.array([[1.5, 2.5], [2.5, 3.5]])

kdl_classifier = KDLClassifier(k=2)
kdl_classifier.fit(X_train, y_train)
y_pred_kdl = kdl_classifier.predict(X_test)

print("K-DL Predictions:", y_pred_kdl)

kdt_classifier = KDTClassifier(k=2)
kdt_classifier.fit(X_train, y_train)
y_pred_kdt = kdt_classifier.predict(X_test)

print("K-DT Predictions:", y_pred_kdt)
