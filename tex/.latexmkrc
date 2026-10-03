# LuaLaTeX でビルドする（tex/ ディレクトリで `latexmk` を実行）
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error %O %S';
$max_repeat = 5;

# 生成物は tex/build/ にまとめる
$out_dir = 'build';
$aux_dir = 'build';

# 索引（日本語の読みで並べるため upmendex を使う）
# latexmk は build/ に移動してから実行するので、スタイルは ../style/ を指す。
# 索引語がまだ1つもないと upmendex がエラーを返すので、そのときは空の .ind を作る。
$makeindex = 'internal run_upmendex %S %D';
sub run_upmendex {
  my ($src, $dest) = @_;
  if (-z $src) {
    open(my $fh, '>', $dest) or return 1;
    close($fh);
    return 0;
  }
  return system('upmendex', '-s', '../style/index.ist', '-o', $dest, $src);
}

# 引数なしで実行したときに作る文書
@default_files = ('main.tex');

# \include したファイルの .aux を build/ の下に書けるように、
# tex/ のサブディレクトリと同じ構成のディレクトリを build/ に作っておく
use File::Find;
use File::Path qw(make_path);
find({ no_chdir => 1, wanted => sub {
  my $d = $File::Find::name;
  return unless -d $d;
  return if $d eq '.' || $d =~ m{(^|/)(build|figures|style)(/|$)};
  make_path("build/" . substr($d, 2));
}}, '.');
