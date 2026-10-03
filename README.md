# 統計検定 データサイエンスエキスパート 教科書

統計検定「データサイエンスエキスパート」の出題範囲を、高校数学と Python の文法だけを前提に学ぶための教科書（LaTeX）です。

## 必要なもの

- TeX Live（LuaLaTeX・latexmk・upmendex を使う。2023 で動作確認）
- [uv](https://docs.astral.sh/uv/)（図を作る Python スクリプトの実行に使う）

## ビルド

```sh
cd tex
latexmk              # 本文 → tex/build/main.pdf
latexmk sample.tex   # レイアウト見本 → tex/build/sample.pdf
latexmk -c           # 中間ファイルの削除
```

VS Code の LaTeX Workshop を使う場合は、`.vscode/settings.json` の設定で `latexmk` が呼ばれます。

## 図の作成

```sh
uv run scripts/figures/build_all.py           # すべての図を作り直す
uv run scripts/figures/build_all.py normal    # ファイル名に normal を含むものだけ
```

`scripts/figures/<名前>.py` が `tex/figures/<名前>.pdf` を作ります。
共通の色・フォント・大きさは `scripts/figures/figstyle.py` にまとめています。

## ディレクトリ構成

```
Docs/                     範囲表（PDF）とセクション構成案
scripts/figures/          図を作る Python スクリプト
tex/
  main.tex                本文（部・章をここで \include する）
  sample.tex              レイアウト見本（すべての囲みを一度ずつ使う）
  preamble.tex            main.tex と sample.tex で共通のプリアンブル
  front/                  扉・はじめに
  parts/statistics/       第 I 部 統計基礎（1 章 = 1 ファイル）
  figures/                図（scripts/figures/ から生成した PDF）
  style/                  スタイルファイル
    textbook-layout.sty   紙面・見出し・柱・目次・色
    textbook-math.sty     数式用の記号（\E, \V, \Normal など）
    textbook-ref.sty      相互参照（\cref）と索引（\term）
    textbook-boxes.sty    定義・定理・例・〔数学メモ〕などの囲み
    textbook-code.sty     Python コードの表示
```
