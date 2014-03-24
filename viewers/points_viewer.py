#! env python2.7

import numpy as np
import matplotlib.pyplot as plt
import sys
import json

def showPoints(values):
    plt.xlabel('Generation')
    plt.ylabel('Average score')
    plt.plot(range(0, len(values)), values, 'ro', linestyle='-')
    plt.axis([0, len(values), 0, max(values)])
    plt.show()

input_str = ""
for line in sys.stdin:
    input_str += line

values = json.loads(input_str)
showPoints(values)
