# -*- coding: utf-8 -*-
#
#【elapsed_time】
#
# 概要: 2つの時間表現を入れてその時間差を計算するスクリプト
#       様々な試験やレポートで経過時間を調査する場合に便利である
#
#       ライブラリとしてdateutilが必要
#
#       ```
#       pip install dateutil
#       ```
#
# usage: elapsed_time.py <time1> <time2>
#
#
import sys
from dateutil.parser import parse


def str2time(time):
    try:
        d = parse(time)
        time = int(d.strftime('%s')) + float(d.microsecond )/1000000.0
    except:
        print("datetimeに変換できませんでした: {}".format(time))
        return None
    return time


def main():
    time1 = str2time(sys.argv[1])
    time2 = str2time(sys.argv[2])
    if time1 is None or time2 is None:
        print("time1, time2のどちらかに数値表現に変換が失敗しまた")
        exit
    time = abs(time1 - time2)
    print("elapsed time is {} [sec], {} [min], {} [hour]".format(time, time/60.0, time/(3600.0)))
    
    
if __name__ == '__main__':
    main()
