def move_to(x_target, y_target):
	size = get_world_size()
	current_x = get_pos_x()
	current_y = get_pos_y()
	
	# Calculate horizontal distance and direction (shortest path)
	distance_x = (x_target - current_x) % size
	
	# If distance_x <= n/2, move East distance_x  steps; otherwise move West (size - distance_x) steps
	if distance_x  <= size // 2:
		steps_x = distance_x
		direction_x = East
	else:
		steps_x = size - distance_x
		direction_x = West
	
	# Calculate vertical distance and direction (shortest path)
	distance_y = (y_target - current_y) % size
	
	# If distance_y <= size/2, move North distance_y steps; otherwise move South (size - distance_y) steps
	if distance_y <= size // 2:
		steps_y = distance_y
		direction_y = North
	else:
		steps_y = size - distance_y
		direction_y = South
	
	# Move step by step, alternating between X and Y directions
	while steps_x > 0 or steps_y > 0:
	# Prioritize the direction with more remaining steps
		if steps_x >= steps_y and steps_x > 0:
			move(direction_x)
			steps_x -= 1
		elif steps_y > 0:
			move(direction_y)
			steps_y -= 1