# scikit-neutrosophic

A Python library for Neutrosophic Machine Learning Algorithms.

## Installation

You can install the library using pip:

```sh
pip install scikit-neutrosophic

```

## Usage

### Neutrosophic k-NN
```
from scikit_neutrosophic.neutrosophic_knn import NeutrosophicKNN

# Example usage
import numpy as np

X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([0, 1, 0, 1])

knn = NeutrosophicKNN(k=3)
knn.fit(X_train, y_train)
print(knn.predict(np.array([[2, 3]])))
```
### Neutrosophic SVM
```
from scikit_neutrosophic.neutrosophic_svm import NeutrosophicSVM

svm = NeutrosophicSVM()
svm.fit(X_train, y_train, neutrosophic_params=None)
print(svm.predict(np.array([[2, 3]])))
```

### Neutrosophic Linear Regression

```
from scikit_neutrosophic.neutrosophic_linear_regression import NeutrosophicLinearRegression

reg = NeutrosophicLinearRegression()
reg.fit(X_train[:, 0], y_train, neutrosophic_params=None)
print(reg.predict(np.array([2, 3, 4])))

```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.