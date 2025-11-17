import navigation

def plant_pumpkin_drone():
	lista = []
	while True:
		contador = 0
		while contador < 2:
			for i in range(get_world_size()):
				if get_ground_type() != Grounds.Soil:
					till()
					
				if get_water()<0.5:
					use_item(Items.Water)	
					
				if get_entity_type() == Entities.Dead_Pumpkin:
					lista.append([get_pos_x(), get_pos_y()])
					plant(Entities.Pumpkin)
				
				plant(Entities.Pumpkin)
	
				move(North)
			contador += 1
		
		while lista:
			#quick_print(lista)
			for i in lista:
				x, y = i
				#move_to.move_to(x, y)
				navigation.move_to(x, y)
				if can_harvest():
					lista.remove([x, y])
				else:
					plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)
		break
			
def main():			
	clear()
	drones = []
	while True:
		while num_drones() != max_drones():
			drone = spawn_drone(plant_pumpkin_drone)
			drones.append(drone)
			move(East)
	
		plant_pumpkin_drone()
		while drones:
			for i in drones:
				if has_finished(i):
					drones.remove(i)
		harvest()
main()
