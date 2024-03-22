def monitor():
	try:
		temps = [50, 55, 60, 65, 70, 75]
		mesg = "MONITOR-ERROR"

		# get multiple temperature readings
		temp_readings = get_temps()
		num_readings = len(temp_readings)

		# sum adds up all items in list
		ave_temp = sum(temp_readings) / num_readings

		if (ave_temp < temps[0]):
			mesg = "Average temperature too cold!"
		elif (ave_temp > temps[5]):
			mesg = "Average temperature too warm!"
		else:
			mesg = "Temperature OK"
	except:
		print("Unexpected error")

	return mesg

# Function to simulate actual fish tank monitoring
def get_temps() -> list[int, int, int]:
	#return [10, 20, 35]
	return [65, 55, 70] 
	#return [90, 95, 105]

#print(monitor())