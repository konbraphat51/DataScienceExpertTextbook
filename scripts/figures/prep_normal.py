"""第1章：標準正規分布。左は上側確率 Q(z)（正規分布表の値）、右は 68-95-99.7 の目安。"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from figstyle import COLORS, FULL_WIDTH, save, setup

setup()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(FULL_WIDTH, FULL_WIDTH * 0.34))
x = np.linspace(-3.8, 3.8, 400)
phi = stats.norm.pdf(x)

# 左：上側確率
z = 1.2
ax1.plot(x, phi, color=COLORS["main"])
m = x >= z
ax1.fill_between(x[m], phi[m], color=COLORS["theorem"], alpha=0.3)
ax1.annotate("$Q(z) = P(Z \\geq z)$", xy=(1.7, 0.04), xytext=(1.6, 0.25), fontsize=8,
             arrowprops={"arrowstyle": "->", "color": COLORS["example"]})
ax1.set_xticks([-3, -2, -1, 0, z, 2, 3], ["$-3$", "$-2$", "$-1$", "0", "$z$", "2", "3"])
ax1.set_yticks([])
ax1.spines["left"].set_visible(False)
ax1.set_title("正規分布表が与える値")

# 右：±1σ、±2σ、±3σ に入る確率
ax2.plot(x, phi, color=COLORS["main"])
for k, alpha in [(3, 0.12), (2, 0.2), (1, 0.32)]:
    m = np.abs(x) <= k
    ax2.fill_between(x[m], phi[m], color=COLORS["main"], alpha=alpha, linewidth=0)
for k, p, y in [(1, "68.3%", 0.27), (2, "95.4%", 0.15), (3, "99.7%", 0.03)]:
    ax2.annotate("", xy=(-k, y), xytext=(k, y),
                 arrowprops={"arrowstyle": "<->", "color": COLORS["example"], "linewidth": 0.8})
    ax2.text(0, y, p, ha="center", va="center", fontsize=7, color=COLORS["example"],
             bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
ax2.set_xticks(range(-3, 4), ["$\\mu-3\\sigma$", "", "$\\mu-\\sigma$", "$\\mu$",
                              "$\\mu+\\sigma$", "", "$\\mu+3\\sigma$"])
ax2.set_yticks([])
ax2.spines["left"].set_visible(False)
ax2.set_title("平均から $\\sigma$ の何倍以内に入るか")

fig.tight_layout()
save(fig, "prep_normal")
