# CLAUDE.md

## ユーザーによる指示

- 平易な日本語で記述
- 前提知識は高校数学・Python文法のみに
- 具体例・例題を交えて説明
- 定理の導出は必ず行う
- 定理や数式の含意（イメージ）を言葉で説明
  - 特に「何が嬉しいか」を強調
- 読者が理解しやすいように、図やグラフを用いて説明
- 細かくステップごとにgit commit
- もしPythonが必要なら、uvで管理

## Claude用メモ

=これ以降は、Claudeがチャットセッション間の一貫性を保つことを目的に、自由に編集することが許可される=

### 構成

- 章立ての元は `Docs/SectionPlan.md`（範囲表の大項目 = `\part`、中項目 = `\chapter`、小項目 = `\section`、説明内容 = `\subsection`）
- 章番号は本全体の通し番号（統計基礎の「0. 準備」が第 1 章）。部の順番はまだ決まっていない
- 1 章 = 1 ファイル（`tex/parts/<部>/NN-<slug>.tex`）。`main.tex` から `\include`
- 骨組みの `% TODO:` は SectionPlan の説明内容。書いたら消す

### ビルド・確認

- `cd tex && latexmk`（LuaLaTeX + jlreq、JIS B5、40 字 × 34 行）。出力は `tex/build/`
- スタイルを変えたら `latexmk sample.tex` を作り、`pdftoppm -png` で画像にして見た目を確かめる
- 図は `scripts/figures/<名前>.py`（`figstyle` を使う）→ `uv run scripts/figures/build_all.py` → `tex/figures/<名前>.pdf`。PDF もコミットする
- 図は `\includegraphics{名前.pdf}` と拡大縮小せずに入れる（幅は Python 側の `WIDTH` などで決める）
- 図のファイル名は章ごとの接頭辞をつける（第 1 章「準備」は `prep_`）
- 数表は `scripts/tables/<名前>.py` → `tex/tables/<名前>.tex` を作り、`\input{tables/<名前>}` で入れる（例：標準正規分布表 `normal-upper`）
- 本文の Python コードは、実際に `uv run python` で実行して、出力をそのまま `pyoutput` に貼る（乱数は `seed=0` で固定）
- スクラッチパッドで Python を実行するときは、`py/` などのサブフォルダに置く（`bisect.py` などの名前の残骸が標準ライブラリを隠して、実行が止まったことがある）

### 書き方の決まり

- 句読点は「、。」
- 番号付きの囲み：`\begin{theorem}[名前][thm:xxx]`（2 つめの [] がラベル。囲みの中で `\label` を使うと節番号を拾うので使わない）
- 囲みの使い分けは `tex/style/textbook-boxes.sty` の冒頭と `tex/front/preface.tex` を参照
  - 定理には必ず `proof`、続けて `intuition`（イメージ）と `merit`（何が嬉しいか）を置く
  - 各節の最初に `\keywords{...}`（範囲表キーワード）
  - 〔数学メモ〕`mathnote`、〔補足〕`supplement`、〔参考〕`reference`
- 参照は `\cref{...}`。ラベルの接頭辞：`part: chap: sec: def: thm: prop: lem: cor: ex: prob: eq: fig: tab:`
- 用語の初出は `\term{用語}{よみ}{英語}`（太字＋英語訳＋索引）。例：`\term{積率母関数}{せきりつぼかんすう}{moment generating function}` → **積率母関数**（moment generating function）
  - 英語訳は必ず付ける（ユーザーの指示）。英語は小文字始まり、略語があれば `moment generating function, MGF` のように続ける
  - 英語訳が本当にない場合だけ 3 つめを `{}` にする（括弧ごと省かれる）
- 索引の読みは、記号で始まる用語もかなで書く（`$z$ スコア` → `ぜっとすこあ`）。英字のままだと索引の先頭に別の見出しができる
- 第 1 章「準備」は範囲表外なので、節に `\keywords` を置かない
- 記法：余事象は $A^c$（$\bar{x}$ は平均に使う）。条件付き確率は `\Prob(A \mid B)`。データの分散は $s_x^2$（$n$ で割る）、共分散 $s_{xy}$、相関係数 $r_{xy}$。確率変数の相関係数は $\rho_{XY}$。標準正規分布の密度は $\varphi(z)$、上側確率は $Q(z)$。標本分散 $S^2$（$n$ で割る）、不偏分散 $U^2$（$n-1$ で割る）。仮説は $H_0$、$H_1$
- 第 1 章「準備」で定義済み（後の章では `\cref` で参照し、`\term` を使わない）：確率変数・期待値・分散・共分散・独立・各基本分布・母集団・標本・統計量・標本分布・推定量・不偏推定量・バイアス・自由度・仮説検定・p 値・検出力など。迷ったら `grep -n '\\term' tex/parts` で確かめる
- 幾何分布は「初めて成功するまでの試行回数」（$1, 2, \dots$）で定義した
- 記号は `textbook-math.sty` のマクロを使う（`\E[X]`、`\V[X]`、`\Cov(X,Y)`、`\Normal(\mu,\sigma^2)`、`\dd x` など）。新しい記号もここに足す

### 作業環境の注意

- Bash の heredoc やコマンドラインに日本語や `\b` を含む文字列を書くと化けることがある。日本語を含むファイルの編集は Edit / Write ツールで行う
- jlreq の見出し設定で長さに `zw` を使うときは `\zw` と書く
- jlreq の `label_format` にフォント命令や `\color` を直接書かない（しおりが壊れる）。色は `\texorpdfstring` で包む
