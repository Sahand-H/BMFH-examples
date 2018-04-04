from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np

figsize(12.5, 4)

a = np.arange(16)
poi = stats.poisson
lambda_ = [1.5, 4.25]
colors = ["#348ABD", "#A60628"]
plt.bar(a, poi.pmf(a, lambda_[0]), color=colors[0], label="$\lambda = %.1f$" %
        lambda_[0], alpha=0.60, edgecolor=colors[0], lw="3")
plt.show()
