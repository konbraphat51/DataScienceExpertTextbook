"""レイアウト見本（tex/sample.tex）用の図：正規分布の密度とヒストグラム。"""

import numpy as np
from scipy import stats

from figstyle import COLORS, new_figure, save

rng = np.random.default_rng(seed=0)
x = rng.normal(size=1000)

fig, ax = new_figure()
ax.hist(x, bins=30, density=True, color=COLORS["main"], alpha=0.3, label="乱数 1000 個のヒストグラム")
grid = np.linspace(-4, 4, 200)
ax.plot(grid, stats.norm.pdf(grid), color=COLORS["theorem"], label="標準正規分布の密度 $f(x)$")
ax.set_xlabel("$x$")
ax.set_ylabel("密度")
ax.legend(frameon=False, loc="upper left")

save(fig, "sample_normal")
