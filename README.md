# はじめての自作キーボード

for 岐阜高専 公開講座（技術室）

Raspberry Pi Picoを使って自由にカスタマイズした定型文を入力できるキーボード

## 部品リスト

参考として購入先の例を示している。

公開講座でRaspberry Pi Picoを購入しなかった場合、[秋月電子](https://akizukidenshi.com/catalog/)で
`K-16149`を購入すると必要な部品が揃う。

<table>
	<tr>
		<td>部品</td>
		<td>数</td>
		<td>購入先</td>
	</tr>
	<tr>
		<td>基板</td>
		<td>1</td>
		<td>基板製造業者**</td>
	</tr>
	<tr>
		<td>Raspberry Pi Pico<br>（ピンヘッダ付）</td>
		<td>1</td>
		<td rowspan="2">秋月電子 K-16149</td>
	</tr>
	<tr>
		<td>microUSBケーブル</td>
		<td>1</td>
	</tr>
	<tr>
		<td>LED</td>
		<td>3</td>
		<td>秋月電子<br>赤 I-11577<br>黄 I-11639<br>緑 I-11637</td>
	</tr>
	<tr>
		<td>ピンソケット<br>（20ピン）</td>
		<td>2</td>
		<td>秋月電子 C-03077</td>
	</tr>
	<tr>
		<td>抵抗(1k)</td>
		<td>3</td>
		<td>秋月電子 R-25102</td>
	</tr>
	<tr>
		<td>キースイッチ</td>
		<td>3</td>
		<td>遊舎工房***</td>
	</tr>
	<tr>
		<td>キーキャップ</td>
		<td>3</td>
		<td>遊舎工房***</td>
	</tr>
	<tr>
		<td>CdSセル*</td>
		<td>1</td>
		<td>あ</td>
	</tr>
	<tr>
		<td>抵抗(10k)*</td>
		<td>1</td>
		<td>秋月電子 R-25103</td>
	</tr>
	<tr>
		<td>圧電スピーカー*</td>
		<td>1</td>
		<td>あ</td>
	</tr>
</table>

- \* 課題2, 3を行う場合のみ必要
- ** 中国の[Elecrow](https://www.elecrow.com/)などに[gerber.zip](./gerber.zip)を渡して発注する。2層基板
- *** 納期と品質と郵便が届かない可能性に目をつぶればAliExpressが安い

## セットアップ手順

Raspberry Pi PicoにCircuitPythonをインストールし、キーボードとして使用する。

以下の手順ではWindows 10を想定している。

CircuitPythonのバージョン`6.3.0`を使用して動作確認を行った。他のバージョンでは仕様が異なる可能性がある。

参考:[7.0.0で正常に動作しないという指摘](https://www.hobbyhappyblog.jp/raspberrypipico-keyboard)

### CircuitPythonのインストール

まずは、Raspberry Pi PicoにCircuitPythonのイメージファイルをインストールする。以下のサイトからダウンロードできる。

[Pico Download](https://circuitpython.org/board/raspberry_pi_pico/)

`adafruit-circuitpython-raspberry_pi_pico-なんたら.uf2`というファイルがダウンロードされたら成功。

次に、Raspberry Pi Picoにある白いボタン（横に`BOOSTEL`と書かれている）を押しながらUSBをパソコンに接続する。

エクスプローラを開き、`PC`の中に`RPI-RP2`（あるいはこれに似た文字列）というドライブが表示される。

このドライブ`RPI-RP2`のなかに`adafruit-circuitpython-raspberry_pi_pico-なんたら.uf2`をコピーする。（`なんたら`に入っている文字は気にしなくてよい）

コピーが終わると`RPI-RP2`が消え、代わりに`CIRCUITPY`というドライブが表示される。

これでCircuitPythonがRaspberry Pi Picoにインストールされた。

### HIDライブラリのインストール

Raspberry Pi Picoをマウスやキーボードとして使うためのHIDライブラリをインストールする。
ライブラリは以下からダウンロードできる。

[Releases · adafruit/Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases)

`Assets`から以下のような名前のファイルをダウンロードする。

`adafruit-circuitpython-hid-[バージョン番号].x-mpy-なんたら.zip`

`Assets`には`[バージョン番号]`の異なるいくつかのファイルがあるが、上でダウンロードしたMicroPythonのバージョン番号の一番左と
同じ番号にする。

例: MicroPython 7.3.2ならバージョン番号は`7`

ダウンロードしたzipファイルを展開し、`lib`フォルダの中に`adafruit_hid`フォルダがあることを確認しておく。

次に、Raspberry Pi Picoのドライブ`CIRCUITPY`の中の`lib`フォルダの中に`adafruit_hid`フォルダをコピーする。

これでRaspberry Pi Picoをマウスやキーボードとして使えるようになった。

### サンプルプログラムの実行

このリポジトリから`code1.py`をダウンロードし、Raspberry Pi Picoに書き込む。

[code1.py](./code1.py)

上のリンクを開き、右上の`Raw`を右クリックして`名前をつけてリンク先を保存`を選択するとプログラムがダウンロードできる。

ダウンロードした`code1.py`の名前を`code.py`に変更する(Raspberry Pi Picoでは`code.py`という名前のプログラムが
最初に実行されるため）。

Raspberry Pi Picoのドライブ`CIRCUITPY`の中に`code.py`をコピーすると、プログラムが実行できる。

適当な入力欄に入力できるようにしてから、基板のボタンを押してみて文字が入力されたら成功！



### プログラムを書き換える

`CIRCUITPY`上に保存した`code.py`をメモ帳で開き、プログラムを変更して上書き保存すると変更が反映される。

## 課題

基板でできることの紹介として、3つの課題を設定している。

公開講座では、課題1を必須で行い、時間が余った場合2や3に進む。

### 課題1 定型文をオリジナルのものに変更しよう

使用するプログラム: [code1.py](./code1.py)

ボタンを押すと定型文を入力できるプログラムがある。プログラムを変更し、自分の好きな言葉を入力できるようにしよう。

### 課題2 音の鳴るキーボードを作ろう

使用するプログラム: [code2.py](./code2.py)

ボタンを押すと音が鳴るプログラムがある。プログラムを変更し、ボタンによって鳴る音を変えてみよう。

### 課題3 テルミンもどきを作ろう

使用するプログラム: [code3.py](./code3.py)

ボタンを押すと音が鳴るプログラムがある。このプログラムは、センサを使って鳴る音を変えている。

センサは周囲のどのような値（温度？湿度？明るさ？加速度？傾き？）を読み取って音を変えているのか考えよう。

また、別のボタンを押すと音が1オクターブ上下するプログラムを作ろう。音の周波数を2倍にすると音は1オクターブ上がり、周波数を1/2倍にすると1オクターブ下がる。
