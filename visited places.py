
visited_places = input("Enter the cities you have visited: ").split(	)

print("************* My Travel List ************")

userchoice = int(input("* (1) Add a new city to the list of visited cities.\n * (2) View your list of visited cities.\n * (3) Sort the list of visited cities.\n * (4) Shows the number of visited cities\n * (5) Remove a given city from the list of visited cities\n * (6) Remove all cities from the list of visited cities\n * (7) Save the list of visited cities to a file.\n" ))

match userchoice:
    
	case 1:
		new_city = input("Add a new city:")
		visited_places.append(new_city)
		print(visited_places)
	case 2:
		print(visited_places)
	case 3:
		print(visited_places.sort())
	case 4:
		print(len(visited_places))
	case 5:
		print(visited_places.remove[-1])
	case 6:
		print(visited_places.remove())
	case 7:
		filename = input("Enter the file name:")
		with open(filename, "w") as file:
			file.write(f"{visited_places}\n")
	case _:
		print("Invalid choice")



	


		

		
		
    
    



