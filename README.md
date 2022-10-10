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
- ** 中国の[Elecrow](https://www.elecrow.com/)などに[gerber.zip](./gerber.zip)を渡して発注する
- *** 納期と品質と郵便が届かない可能性に目をつぶればAliExpressが安い

## セットアップ手順

Raspberry Pi Picoの初期設定を行い、動作確認する。

以下の手順ではWindows 10を想定している。

CircuitPythonのバージョン`6.3.0`を使用して動作確認を行った。他のバージョンでは仕様が異なる可能性がある。

参考:[7.0.0で正常に動作しないという指摘](https://www.hobbyhappyblog.jp/raspberrypipico-keyboard)

### CircuitPythonのインストール


### HIDライブラリのインストール


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


### 課題1 定型文をオリジナルのものに変更しよう

使用するプログラム: `code1.py`

### 課題2 音の鳴るキーボードを作ろう

使用するプログラム: `code2.py`


### 課題3 テルミンもどきを作ろう

使用するプログラム: `code3.py`
