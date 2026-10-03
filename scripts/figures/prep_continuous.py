"""第1章：連続型の分布（一様分布・指数分布・正規分布）の確率密度関数。"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from figstyle import COLORS, FULL_WIDTH, save, setup

setup()
fig, axes = plt.subplots(1, 3, figsize=(FULL_WIDTH, FULL_WIDTH * 0.34))

# 一様分布 U(1, 3)
ax = axes[0]
ax.plot([0, 1], [0, 0], color=COLORS["main"])
ax.plot([1, 3], [0.5, 0.5], color=COLORS["main"])
ax.plot([3, 4], [0, 0], color=COLORS["main"])
ax.plot([1, 1], [0, 0.5], color=COLORS["main"], linestyle=":", linewidth=1)
ax.plot([3, 3], [0, 0.5], color=COLORS["main"], linestyle=":", linewidth=1)
ax.fill_between([1, 3], [0.5, 0.5], color=COLORS["main"], alpha=0.15)
ax.set_xticks([0, 1, 2, 3, 4], ["0", "$a=1$", "2", "$b=3$", "4"])
ax.set_yticks([0, 0.5], ["0", "$\\frac{1}{b-a}$"])
ax.set_ylim(0, 0.8)
ax.set_title("一様分布 $\\mathrm{U}(1, 3)$")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")

# 指数分布
ax = axes[1]
x = np.linspace(0, 4, 300)
for lam, color in [(0.5, COLORS["merit"]), (1, COLORS["main"]), (2, COLORS["theorem"])]:
    ax.plot(x, lam * np.exp(-lam * x), color=color, label=f"$\\lambda={lam}$")
ax.set_title("指数分布 $\\mathrm{Exp}(\\lambda)$")
ax.set_xlabel("$x$")
ax.legend(frameon=False)

# 正規分布
ax = axes[2]
x = np.linspace(-5, 6, 400)
for mu, s2, color in [(0, 1, COLORS["main"]), (0, 4, COLORS["merit"]), (2, 1, COLORS["theorem"])]:
    ax.plot(x, stats.norm.pdf(x, mu, np.sqrt(s2)), color=color,
            label=f"$\\mu={mu},\\ \\sigma^2={s2}$")
ax.set_title("正規分布 $\\mathrm{N}(\\mu, \\sigma^2)$")
ax.set_xlabel("$x$")
ax.set_ylim(0, 0.55)
ax.legend(frameon=False, loc="upper left", fontsize=7)

fig.tight_layout()
save(fig, "prep_continuous")
