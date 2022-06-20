import matplotlib.pyplot as plottah
import time

def get_data():
	x = [] 
	y = []
	data_clear = []

	data_raw = open('./Ping_data/ping.data', 'r')
	data_read = data_raw.read()
	data_split = data_read.split(',')

	for ping_lab in data_split:
		print(ping_lab.replace('\n', ''))
		data_clear += [ping_lab.replace('\n', '')]
	data_clear.remove('')

	for component_t2 in data_clear:
		component_t1 = component_t2.split(':')

		y.insert(int(component_t1[0]), int(component_t1[1]))
		x.insert(int(component_t1[0]), int(component_t1[0]))
	data_raw.close()

	return x, y

figure, ax = plottah.subplots(figsize=(4,5))

# Data Coordinates

x, y = get_data()

# GUI
plottah.ion()

# Plot
plot1, = ax.plot(x, y)

# Labels
plottah.xlabel("Ping ticks (1 tick ~= 45Sec)",fontsize=13)
plottah.ylabel("Ping responce in ms",fontsize=13)

while True:
	x, y = get_data()

	plot1.set_xdata(x)
	plot1.set_ydata(y)
    
	figure.canvas.draw()
	figure.canvas.flush_events()

	# Display
	plottah.show()
