def monitor():
	try:
		val1 = 1250
		val2 = 1350

		mag_levels = list(range(val1, val2, 10))

		current = get_magnesium_level()
		mesg = "MONITOR-ERROR"

		num_levels = len(mag_levels) - 1
		if (current < mag_levels[0]):
			mesg = "Magnesium level too low!"
		elif (current > mag_levels[num_levels]):
			mesg = "Magnesium level too high!"
		else:
			mesg = "Magnesium level OK"    
	except:
		print("Unexpected error")

	return mesg

# Function to simulate actual fish tank monitoring
def get_magnesium_level() -> int:
	#return 1000
	return 1300
	#return 1500

#print(monitor())