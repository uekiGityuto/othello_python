# othello_python

## 概要

ターミナルで遊ぶオセロ。

## 仕様

- 8 \* 8 の盤面が出てくる
- ゲーム開始時に白 2 黒 2 が置かれている
- 盤面で自分と違う色の石の隣に黒 or 白の石を置ける
- 違う色で挟まれたらところに石を置かれたら、挟まれた石は色が反転する
- 終了時に勝敗を判定

## 必要

python3, pip3
(Python3.10.8 で動作確認済み)

### エディタ

VS Code

### 拡張機能

- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
  ※ Code Runner は標準入力出来なくて？最終的には使わなかったが、`.vscode/setting.json`で設定だけしたので記載

## 環境準備

```
python3 -m pip install --upgrade pip
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

※
`source .venv/bin/activate`で仮想環境を有効化している。
仮想環境を無効化したい場合は以下コマンド。

```
deactivate
```

## テスト方法

```
python3 -m unittest discover
```

## デバッグ方法

VS Code のデバッグを実行する。

## 実行方法

```
python3 -m othello_python
```

## 遊び方

起動すると説明が出てきます。

## 注意

設定ファイルの内容などは基本的に他サイトからのコピペで、動作確認はしていますが、細かな精査はしていません。

また、実行方法なども軽くググって見つかった方法で実行しているだけなので、他により良い方法があるかもしれません。
