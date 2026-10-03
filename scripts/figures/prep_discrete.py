"""第1章：離散型の分布（二項分布・ポアソン分布・幾何分布）の確率関数。"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from figstyle import COLORS, FULL_WIDTH, save, setup

setup()
fig, axes = plt.subplots(1, 3, figsize=(FULL_WIDTH, FULL_WIDTH * 0.34))
c1, c2 = COLORS["main"], COLORS["theorem"]
w = 0.4


def bars(ax, k, p1, p2, label1, label2):
    ax.bar(k - w / 2, p1, width=w, color=c1, label=label1)
    ax.bar(k + w / 2, p2, width=w, color=c2, label=label2)
    ax.set_ylim(0, max(p1.max(), p2.max()) * 1.45)  # 凡例の場所をあける
    ax.set_xlabel("$k$")
    ax.legend(frameon=False, loc="upper right", handlelength=1)


k = np.arange(0, 11)
bars(axes[0], k, stats.binom.pmf(k, 10, 0.5), stats.binom.pmf(k, 10, 0.2),
     "$n=10,\\ p=0.5$", "$n=10,\\ p=0.2$")
axes[0].set_title("二項分布 $\\mathrm{Bin}(n, p)$")
axes[0].set_ylabel("$P(X = k)$")

k = np.arange(0, 11)
bars(axes[1], k, stats.poisson.pmf(k, 1), stats.poisson.pmf(k, 4),
     "$\\lambda=1$", "$\\lambda=4$")
axes[1].set_title("ポアソン分布 $\\mathrm{Po}(\\lambda)$")

k = np.arange(1, 11)
bars(axes[2], k, stats.geom.pmf(k, 0.5), stats.geom.pmf(k, 0.2),
     "$p=0.5$", "$p=0.2$")
axes[2].set_title("幾何分布 $\\mathrm{Geo}(p)$")
for ax in axes:
    ax.set_xticks(range(0, 11, 2))

fig.tight_layout()
save(fig, "prep_discrete")
