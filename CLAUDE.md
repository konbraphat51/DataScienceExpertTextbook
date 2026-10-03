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

### 書き方の決まり

- 句読点は「、。」
- 番号付きの囲み：`\begin{theorem}[名前][thm:xxx]`（2 つめの [] がラベル。囲みの中で `\label` を使うと節番号を拾うので使わない）
- 囲みの使い分けは `tex/style/textbook-boxes.sty` の冒頭と `tex/front/preface.tex` を参照
  - 定理には必ず `proof`、続けて `intuition`（イメージ）と `merit`（何が嬉しいか）を置く
  - 各節の最初に `\keywords{...}`（範囲表キーワード）
  - 〔数学メモ〕`mathnote`、〔補足〕`supplement`、〔参考〕`reference`
- 参照は `\cref{...}`。ラベルの接頭辞：`part: chap: sec: def: thm: prop: lem: cor: ex: prob: eq: fig: tab:`
- 用語の初出は `\term{用語}{よみ}`（太字＋索引）
- 記号は `textbook-math.sty` のマクロを使う（`\E[X]`、`\V[X]`、`\Cov(X,Y)`、`\Normal(\mu,\sigma^2)`、`\dd x` など）。新しい記号もここに足す

### 作業環境の注意

- Bash の heredoc やコマンドラインに日本語や `\b` を含む文字列を書くと化けることがある。日本語を含むファイルの編集は Edit / Write ツールで行う
- jlreq の見出し設定で長さに `zw` を使うときは `\zw` と書く
- jlreq の `label_format` にフォント命令や `\color` を直接書かない（しおりが壊れる）。色は `\texorpdfstring` で包む
