"""第1章：相関係数の値と散布図の形（6 つの例）。"""

import matplotlib.pyplot as plt
import numpy as np

from figstyle import COLORS, FULL_WIDTH, save, setup

rng = np.random.default_rng(seed=1)
n = 100


def correlated(r):
    """相関係数がほぼ r になる 2 変数のデータを作る。"""
    x = rng.normal(size=n)
    y = r * x + np.sqrt(1 - r**2) * rng.normal(size=n)
    return x, y


panels = [correlated(r) for r in (0.9, 0.5, 0.0, -0.5, -0.9)]
x = rng.uniform(-2, 2, size=n)
panels.append((x, x**2 + 0.3 * rng.normal(size=n)))  # 曲線の関係（相関は 0 に近い）

setup()
fig, axes = plt.subplots(2, 3, figsize=(FULL_WIDTH, FULL_WIDTH * 0.62))
for ax, (x, y) in zip(axes.flat, panels):
    r = np.corrcoef(x, y)[0, 1]
    ax.scatter(x, y, s=6, color=COLORS["main"], alpha=0.7)
    ax.set_title(f"$r = {r:.2f}$".replace("-", "{-}"))
    ax.set_xticks([])
    ax.set_yticks([])
axes.flat[-1].set_title(axes.flat[-1].get_title() + "（曲線の関係）")
fig.tight_layout()

save(fig, "prep_correlation")
