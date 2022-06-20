import matplotlib.pyplot as plottah

def get_data(): #Getting the data from file
	x = [] 
	y = []
	data_clear = []

	data_raw = open('./Bot_logs/Ping_data/ping.data', 'r') #Get the data
	data_read = data_raw.read() #Read the data
	data_split = data_read.split(',') #Split each and every data part

	for ping_lab in data_split: #Split the data even more
		print(ping_lab.replace('\n', ''))
		data_clear += [ping_lab.replace('\n', '')]
	data_clear.remove('')#Remove the last list part cause its empty

	for component_t2 in data_clear:#Split the data and set them into lists
		component_t1 = component_t2.split(':')

		y.insert(int(component_t1[0]), int(component_t1[1]))
		x.insert(int(component_t1[0]), int(component_t1[0]))
	data_raw.close()#Close the file to update it later

	return x, y#Return the data

figure, ax = plottah.subplots(figsize=(4,5))

x, y = get_data()#Getting the data 

plottah.ion()#Creating the GUI

plot1, = ax.plot(x, y)#Creating the plot with the data.

plottah.xlabel("Ping ticks (1 tick ~= 45Sec)",fontsize=18)#Adding the labels
plottah.ylabel("Ping responce in ms",fontsize=18)

while True: #Loop of updating the data 
	x, y = get_data()#Getting the data

	plot1.set_xdata(x)#'Resetting' the data for x and y
	plot1.set_ydata(y)
    
	figure.canvas.draw()#drawing the data 
	figure.canvas.flush_events()#No idea what it does

	plottah.show()#Writing the data on board
