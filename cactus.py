import navigation

size = get_world_size()
def sort_line(start_x, start_y, direction):
	navigation.move_to(start_x, start_y)
	for i in range(size):
		navigation.move_to(start_x, start_y)
		swap_count = 0
		for j in range(size - 1 - i):
			if measure() > measure(direction):
				swap_count += 1
				swap(direction) 
			move(direction)
		if swap_count == 0:
			break
			
def sort_line_vertical():

	start_x = get_pos_x()
	start_y = get_pos_y()
	direction = North
	
	for i in range(size):
		navigation.move_to(start_x, start_y)
		swap_count = 0
		for j in range(size - 1 - i):
			if measure() > measure(direction):
				swap_count += 1
				swap(direction) 
			move(direction)
		if swap_count == 0:
			break

def sort_line_horizontal():

	start_x = get_pos_x()
	start_y = get_pos_y()
	direction = East
	
	for i in range(size):
		navigation.move_to(start_x, start_y)
		swap_count = 0
		for j in range(size - 1 - i):
			if measure() > measure(direction):
				swap_count += 1
				swap(direction) 
			move(direction)
		if swap_count == 0:
			break
	
def plant_cactus():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		move(North)
		
clear()	
while True:   
	drones = []
	while num_drones() != max_drones():
		drone = spawn_drone(plant_cactus)
		drones.append(drone)
		move(East)
	plant_cactus()
	
	while drones:
		for i in drones:
			if has_finished(i):
				drones.remove(i)
				
	drones = []
	navigation.move_to(0,0)
	while num_drones() != max_drones():
		drone = spawn_drone(sort_line_vertical)
		drones.append(drone)
		move(East)
	sort_line_vertical()
	
	while drones:
		for i in drones:
			if has_finished(i):
				drones.remove(i)
	
	drones = []
	navigation.move_to(0,0)
	while num_drones() != max_drones():
		drone = spawn_drone(sort_line_horizontal)
		drones.append(drone)
		move(North)
	sort_line_horizontal()
	
	while drones:
		for i in drones:
			if has_finished(i):
				drones.remove(i)
	navigation.move_to(0,31)
	harvest()