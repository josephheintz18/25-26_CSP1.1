seconds = 10000

hours = int(seconds / 3600)
secondsLeft = seconds % 3600
minutes = int(secondsLeft / 60)
extraseconds = secondsLeft % 60

print("Lab03, 80 Point Version")
print("Starting seconds: ", seconds)
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", extraseconds)