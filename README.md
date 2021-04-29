## elapsed-time
時間差を計算してくれる、簡単なコマンド。ドキュメントの作成やレポートに使える。

### インストール方法
関連ライブラリとして`dateutil`が必要
```
pip install dateutil
```
### 利用法
```
$ python3 elapsed-time.py <time1> <time2>
# python3 ./elapsed_time.py "20210428-11:24:48.784" "20210428-11:43:55.734"
elapsed time is 1146.9500000476837 [sec], 19.115833334128062 [min], 0.3185972222354677 [hour]
```
ミリ秒まで対応している。

### 利用上の注意
時刻表現の文字列のパースは`dateutil.parser`に依存している。

