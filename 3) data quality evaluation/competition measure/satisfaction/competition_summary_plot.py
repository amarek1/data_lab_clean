import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import scipy.stats
np.random.seed(7)

score_synthpop =
score_GAN =
score_cGAN =
score_WGAN =
score_WcGAN =
score_tGAN =


fig = plt.figure()
x = np.arange(6)
distance = [score_synthpop, score_GAN, score_cGAN, score_WGAN, score_WcGAN, score_tGAN]
plt.title('Synthetic ranking agreement results for satisfaction dataset')
plt.ylabel('Score')
plt.xlabel('data generator')
a = plt.bar(x, distance)
plt.xticks(x, ('synthpop', 'GAN', 'cGAN', 'WGAN', 'WcGAN', 'tGAN'))
plt.ylim((0,1))
plt.tight_layout()
a[0].set_color('lightseagreen')
a[1].set_color('gold')
a[2].set_color('darkorange')
a[3].set_color('grey')
a[4].set_color('dodgerblue')
a[5].set_color('mediumvioletred')
plt.savefig('3) data quality evaluation/competition measure/satisfaction/competition_measure_plot_sat.png')