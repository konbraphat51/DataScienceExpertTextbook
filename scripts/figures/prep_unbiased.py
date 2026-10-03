"""第1章：n で割る標本分散と n-1 で割る不偏分散の平均（シミュレーション）。

母集団は N(0, 1)（σ² = 1）。標本の大きさ n ごとに 20 万回標本をとり、2 つの分散の平均を描く。
"""

import numpy as np

from figstyle import COLORS, WIDTH, new_figure, save

rng = np.random.default_rng(seed=0)
ns = np.arange(2, 21)
reps = 200_000
s2_mean, u2_mean = [], []
for n in ns:
    x = rng.normal(size=(reps, n))
    ss = ((x - x.mean(axis=1, keepdims=True)) ** 2).sum(axis=1)
    s2_mean.append((ss / n).mean())
    u2_mean.append((ss / (n - 1)).mean())

fig, ax = new_figure(WIDTH, aspect=0.5)
ax.axhline(1, color=COLORS["ref"], linewidth=1, linestyle=":")
ax.text(20.3, 1, "$\\sigma^2 = 1$", va="center", fontsize=8, color=COLORS["ref"])
grid = np.linspace(2, 20, 200)
ax.plot(grid, (grid - 1) / grid, color=COLORS["theorem"], linewidth=1, alpha=0.5)
ax.plot(ns, s2_mean, "o", color=COLORS["theorem"], markersize=4,
        label="$S^2$（$n$ で割る）の平均。線は $(n-1)/n$")
ax.plot(ns, u2_mean, "s", color=COLORS["main"], markersize=4,
        label="$U^2$（$n-1$ で割る）の平均")
ax.set_xlabel("標本の大きさ $n$")
ax.set_ylabel("20 万回の平均")
ax.set_xticks([2, 5, 10, 15, 20])
ax.set_ylim(0.4, 1.15)
ax.legend(frameon=False, loc="lower right")

save(fig, "prep_unbiased")
