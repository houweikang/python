from die import Die
import pygal

#创建die 6
die1 = Die()
die2 = Die()

#置几次骰子，将结果存于列表中
results = []
for roll_num in range(10000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
for value in range(2,13):
    frequency = results.count(value)
    frequencies.append(frequency)

#可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling 10000 times"
hist.x_labels = list(range(1,13))
hist.x_title = "Results"
hist.y_title = "Frequencies of Result"
hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')