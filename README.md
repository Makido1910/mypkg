# 連続する数字の表示
* このパッケージはROS2のパッケージである
* 連続する数字を順に表示するメッセージをトピック上に発行し、サブスクライブする
  * mypkgディレクトリ内にtalker.pyとlistener.pyというファイルがある
    * talker.py: 連続する数字をメッセージとしてトピック上に発行する
    * listener.py: talker.pyからトピックに送られたメッセージをサブスクライブする
  * launchディレクトリ内にはtalk_listen.launch.pyというファイルがある
    * talk_listen.launch.py: 1つの端末でtalker.pyとlistener.pyの2つのプログラムを同時に実行する

![test](https://github.com/Makido1910/mypkg/actions/workflows/test.yml/badge.svg)

# 実行方法
* 端末ごとに実行する
  * 端末1で
  ```
  $ ros2 run mypkg talker
   (なにも表示されない)
  ```
  * 端末2で
  ```
  $ ros topic echo /countup      #Ctrl+Cで終了
  data: 42
  ---
  data: 43
  ---
  data: 44
  ---
  data: 45
  ---
  data: 46
  ---
  data: 47
  ```
* 1つの端末で実行する
```
$ ros2 launch mypkg talk_listen.launch.py     #Ctrl+Cで終了
[INFO] [launch]: All log files can be found below /root/.ros/log/2023-01-04-22-12-11-400101-LAPTOP-PDI5958T-470
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [471]
[INFO] [listener-2]: process started with pid [473]
[listener-2] [INFO] [1672837932.392312700] [listener]: Listen: 0
[listener-2] [INFO] [1672837932.880007000] [listener]: Listen: 1
[listener-2] [INFO] [1672837933.378568500] [listener]: Listen: 2
[listener-2] [INFO] [1672837933.879714000] [listener]: Listen: 3
[listener-2] [INFO] [1672837934.379760000] [listener]: Listen: 4
[listener-2] [INFO] [1672837934.878952000] [listener]: Listen: 5

```
# テスト環境
* ROS2 
* Ubuntu 22.04.1 LTS
* python
  * テスト済: 3.10

# ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
* © 2022~2023 Makido1910
