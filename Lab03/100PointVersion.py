milliseconds = 10000123
seconds = int(milliseconds / 100)
minutes = int(milliseconds / 6000)
hours = int(milliseconds / 360000)
millisecondsLeft = seconds % 3600
extramilliseconds = millisecondsLeft % 60

print("Starting millisecond: ", milliseconds)
print("Hours: ", hours)
