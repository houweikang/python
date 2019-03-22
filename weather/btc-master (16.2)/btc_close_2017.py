import json

#将数据加载到列表中
filename = "weather/btc-master (16.2)/btc_close_2017.json"
with open(filename) as f:
    btc_data = json.load(f)

#加入列表
dates = []
months = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    months.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close.append(int(float(btc_dict["close"])))

import pygal
import math

line_chart = pygal.Line(x_label_rotation = 20,show_minor_x_labels = False)
line_chart.title = '收盘价对数变换（RMB）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('收盘价',close_log)
line_chart.render_to_file('weather/btc-master (16.2)/收盘价对数变换折线图.svg')