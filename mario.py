def mario():
	
	# Get (valid) user input
	while True:
		try:
			height = int(raw_input("Height: "))
			# Handle negatives as input
			if height < 0:
				print "Please enter a positive integer!"
				continue
			break
		# For any other format of input
		except ValueError:
			print "Oops, that's not a valid input. Try again!"

	hash_counter = 0

	while hash_counter < height + 1:
		if hash_counter == 0:
			hash_counter += 1
			continue
		print (height - hash_counter) * " " + hash_counter * "#", hash_counter * "#"
		hash_counter += 1

mario()
