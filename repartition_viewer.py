#! env python2.7
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import sys
import json

def showRepartition(values):
    plt.hist(values, 20, stacked=1, facecolor='blue')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title(r'Score repartition')
    to_percentage = lambda y, pos: str(round( ( y / float(len(values)) ) * 100.0, 2)) + '%'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percentage))
    plt.show()

input_str = ""
for line in sys.stdin:
    input_str += line
print(input_str)
values = json.loads(input_str)
showRepartition(values)
