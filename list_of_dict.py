# empty list for storing aliens 
aliens = []

# make 30 greenies 
for alien_number in range(30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'} 
	aliens.append(new_alien)

#show the first 5 aliens 
for aliens in aliens [:5]:
	print (aliens)

#show how many aliens have been created 
print("total number of aliens: " + str(len(aliens)))

	
