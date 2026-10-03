"""第1章：np = 3 を保って n を大きくすると、二項分布がポアソン分布 Po(3) に近づく。"""

import numpy as np
from scipy import stats

from figstyle import COLORS, WIDTH, new_figure, save

k = np.arange(0, 11)
fig, ax = new_figure(WIDTH, aspect=0.5)
ax.bar(k, stats.poisson.pmf(k, 3), width=0.7, color=COLORS["main"], alpha=0.25,
       label="ポアソン分布 $\\mathrm{Po}(3)$")
for n, color, marker in [(6, COLORS["theorem"], "s"), (30, COLORS["merit"], "o")]:
    ax.plot(k, stats.binom.pmf(k, n, 3 / n), marker=marker, markersize=4, linewidth=1,
            color=color, label=f"二項分布 $\\mathrm{{Bin}}({n},\\ 3/{n})$")
ax.set_xlabel("$k$")
ax.set_ylabel("$P(X = k)$")
ax.set_xticks(k)
ax.legend(frameon=False)

save(fig, "prep_poisson_limit")
