# robosys_ROS
## 概要
パブリッシャを1個もつノードで、ランダムに素数を表示させる。
## 動作環境
・ROS noetic  
・RaspberryPi 4 Model B  
・Ubuntu 20.04  
## デモンストレーション
https://youtu.be/HLM77n0FOtg
## インストール方法
~~~
$ cd ~/catkin_ws/src  
$ git clone https://github.com/Yui0909/robosys_ROS.git  
$ cd ..  
$ catkin_make
~~~
## 実行手順
端末1：  
roscoreを立ち上げる  
~~~
$ roscore
~~~
端末2：  
ディレクトリに入る  
~~~
$ cd ~/catkin_ws/src/robosys_ROS/scripts
~~~
実行できるようにパーミッション設定  
~~~
$ chmod +x num.py
~~~
num.pyを実行する  
~~~
$ rosrun mypkg num.py
~~~
端末3：  
numのデータを取り出す  
~~~
$ rostopic echo /num
~~~
## ライセンス
BSD 3-Clause License
