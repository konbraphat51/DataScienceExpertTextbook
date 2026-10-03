"""図の共通スタイル。

使い方（各スクリプトの先頭で）::

    from figstyle import COLORS, new_figure, save

- 色は tex/style/textbook-layout.sty の定義と同じにしてある。
- 日本語フォントは TeX Live に入っている原ノ味ゴシックを使う（本文の見出しと同じ書体）。
- 図は tex/figures/ に PDF で保存する。
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

# 出力先：tex/figures/
FIG_DIR = Path(__file__).resolve().parents[2] / "tex" / "figures"

# textbook-layout.sty の色と同じ
COLORS = {
    "main": "#1F4E79",
    "theorem": "#B4532A",
    "example": "#5B6770",
    "merit": "#2E7D32",
    "image": "#6A4C93",
    "math": "#00838F",
    "supp": "#8D6E00",
    "ref": "#757575",
}
# 複数の系列を描くときの順番
CYCLE = [COLORS[k] for k in ("main", "theorem", "merit", "image", "math", "supp")]

# 図の幅（インチ）。本文は B5・1行 40 字（約 140mm = 5.5 インチ）。
# TeX 側では \includegraphics{...} と拡大縮小せずに入れる（文字の大きさがそろう）。
FULL_WIDTH = 5.5   # 本文の幅いっぱい
WIDTH = 4.4        # 標準（本文の 8 割）
HALF_WIDTH = 2.7   # 2つ並べるとき


def _find_texlive_font(name: str) -> str | None:
    """kpsewhich で TeX Live のフォントファイルを探す。"""
    if shutil.which("kpsewhich") is None:
        return None
    result = subprocess.run(["kpsewhich", name], capture_output=True, text=True)
    path = result.stdout.strip()
    return path or None


def _setup_font() -> None:
    family = "sans-serif"
    for fname in ("HaranoAjiGothic-Regular.otf", "HaranoAjiGothic-Medium.otf"):
        path = _find_texlive_font(fname)
        if path:
            font_manager.fontManager.addfont(path)
    try:
        font_manager.findfont("Harano Aji Gothic", fallback_to_default=False)
        family = "Harano Aji Gothic"
    except ValueError:
        pass
    plt.rcParams["font.family"] = family


def setup() -> None:
    """matplotlib の共通設定を行う。"""
    _setup_font()
    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.titlesize": 9,
            "axes.labelsize": 9,
            "legend.fontsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "axes.prop_cycle": matplotlib.cycler(color=CYCLE),
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.unicode_minus": False,
            "mathtext.fontset": "cm",
            "lines.linewidth": 1.5,
            "figure.dpi": 150,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,  # フォントを埋め込む
        }
    )


def new_figure(width: float = WIDTH, aspect: float = 0.55, **kwargs):
    """幅 width（インチ）、高さ width*aspect の図を作る。"""
    setup()
    return plt.subplots(figsize=(width, width * aspect), **kwargs)


def save(fig, name: str) -> Path:
    """tex/figures/<name>.pdf に保存する。"""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / f"{name}.pdf"
    # 作成日時を入れない（作り直しても中身が同じなら、git の差分が出ないように）
    fig.savefig(path, metadata={"CreationDate": None})
    plt.close(fig)
    print(f"saved: {path.relative_to(FIG_DIR.parents[1])}")
    return path
