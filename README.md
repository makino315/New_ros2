# 東京都の明日の天気を取得

[![test](https://github.com/makino315/New_ros2/actions/workflows/test.yml/badge.svg)](https://github.com/makino315/New_ros2/actions/workflows/test.yml)

## mypkg
- このリポジトリはROS2のパッケージで授業で作成しました。

## ノードの説明
- このノードは天気APIを使用しております。
- このパッケージは明日の東京の天気をパブリッシュする'weather_pub'というノードで構成されています。
- topicの名前は'weather'です。

## 使い方
以下のコマンドで実行します。
```bash
ros2 run mypkg weather_pub
```
このコマンドを実行しても何も表示されない為、別の端末で次のコマンドを入力して実行してください。
 ```bash
 ros2 topic echo /weather
 ```
 出力すると以下のような結果になります。
 ```bash
 data: '2025年01月11日の東京都 東京 の天気は晴時々曇です。

  最高気温は11度、最低気温は1度です。'
---
data: '2025年01月11日の東京都 東京 の天気は晴時々曇です。

  最高気温は11度、最低気温は1度です。'
---
data: '2025年01月11日の東京都 東京 の天気は晴時々曇です。

  最高気温は11度、最低気温は1度です。'
---
data: '2025年01月11日の東京都 東京 の天気は晴時々曇です。

  最高気温は11度、最低気温は1度です。'
---
data: '2025年01月11日の東京都 東京 の天気は晴時々曇です。

  最高気温は11度、最低気温は1度です。'
---
```

## テストの為のコード
- listener.py
- talk_listen.launch.py

#動作環境

## テスト環境(GitHub Actions)
- ROS2 version：humble
- OS：Ubuntu 22.04 LTS

## 開発環境
- os: ubuntu20.04 LTS
- ROS2 version: Foxy

## 著作権とライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- © 2025 Kazuki Makino
