# サンプルプログラム

「AITuberを作ってみたら生成AIプログラミングがよくわかった件」にて掲載したコードを改変したものです。
配信用画像に関しては同ページの日経さんのURL（nkbpで始まる方）を参照ください。

## 依存パッケージのインストール

音声を再生するために PortAudio をインストールしてください。

```shell
$ sudo apt-get install libportaudio2
```

## 利用者向け: パッケージのインストール

以下のコマンドを実行して本パッケージをインストールしてください。

```shell
$ pip install .
```

## 開発者向け: 開発用インストール

以下のコマンドを実行して開発用パッケージをインストールしてください。

```shell
$ pip install -e ".[dev,test]"
```

## voicevox エンジンのインストール

```shell
# download engine
wget https://github.com/VOICEVOX/voicevox_engine/releases/download/0.14.6/voicevox_engine-linux-cpu-0.14.6.7z.001

# install dependecy
sudo apt install p7zip

# decompression
mv voicevox_engine-linux-cpu-0.14.6.7z.001 voicevox_engine-linux-cpu-0.14.6.7z
p7zip -d voicevox_engine-linux-cpu-0.14.6.7z
```

```shell
# move into linux-cpu directory
cd linux-cpu
```

```shell
# change the access permission
chmod 755 run
```

```shell
# open the help for the engine
./run --help
```

```shell
# run the engine
./run --help
```
