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
		<td>ピンソケット<br>（15ピン）</td>
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


