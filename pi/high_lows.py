import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f :
    reader = csv.reader(f)
    next(reader)

    dates,highs,lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))

#根据数据绘制图形
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = (0.9,0.5,0.4))
plt.plot(dates, lows, c = (.3,.3,.9))
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = .5)
#设置图形格式
plt.title('Daily high-low temperatures - 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 16)
plt.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show()