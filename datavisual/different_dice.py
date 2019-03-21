from die import Die
import pygal

#创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

#骰子多次，讲结果保存到列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(2,17):
    frequency = results.count(value)
    frequencies.append(frequency)

#可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling 50000 times"
hist.x_labels = list(range(2,17))
hist.x_title = "Results"
hist.y_title = "Frequencies of Result"
hist.add('D6 + D10',frequencies)
hist.render_to_file('dice_visual1.svg')