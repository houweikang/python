import csv
import matplotlib.pyplot as plt
from datetime import datetime 

filename = 'weather\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            higt = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(higt)           
            lows.append(low)
#绘制图形
fig = plt.figure(dpi=128,figsize=(10,5))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形格式
plt.title("Day high and low tempreture - 2014(DV)",fontsize = 24)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('T(F)',fontsize = 16)
plt.tick_params(axis='both',which = 'major',labelsize = 16)

plt.show()