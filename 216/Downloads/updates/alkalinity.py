def monitor():
	try:
		max = 17
		min = 12

		current = get_alkalinity()
		mesg = "MONITOR-ERROR"

		if (current < min):
			mesg = "Alkalinity too low!"
		elif (current > max):
			mesg = "Alkalinity too high!"
		else:
			mesg = "Alkalinity OK"
	except:
		print("Unexpected Error") 
	return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
	return 9
	#return 13
	#return 21

#print(monitor())