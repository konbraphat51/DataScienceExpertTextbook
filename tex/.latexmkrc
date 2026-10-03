# LuaLaTeX でビルドする（tex/ ディレクトリで `latexmk` を実行）
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error %O %S';
$max_repeat = 5;

# 生成物は tex/build/ にまとめる
$out_dir = 'build';
$aux_dir = 'build';

# 索引（日本語の読みで並べるため upmendex を使う）
# latexmk は build/ に移動してから実行するので、スタイルは ../style/ を指す
$makeindex = 'upmendex %O -s ../style/index.ist -o %D %S';

# 引数なしで実行したときに作る文書
@default_files = ('main.tex');
