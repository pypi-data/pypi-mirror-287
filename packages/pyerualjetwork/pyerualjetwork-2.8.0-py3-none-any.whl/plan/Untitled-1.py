

import plan
import time
from colorama import Fore
import numpy as np
from sklearn.datasets import load_digits

# TRAIN

data = load_digits()

X = data.data
y = data.target

X = plan.normalization(X)
    
x_train, x_test, y_train, y_test = plan.split(X, y, 0.4, 42)


y_train, y_test = plan.encode_one_hot(y_train, y_test)


x_test, y_test = plan.auto_balancer(x_test, y_test)


W = plan.fit(x_train, y_train, val=True)

# TEST

test_model = plan.evaluate(x_test, y_test,show_metrices=True, W=W)