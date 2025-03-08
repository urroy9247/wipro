import time

#getting the current time

current_time = time.localtime()
print("Current time:", current_time)

#Let's format our time in a way that's easier to read

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S %a:%A %b:%B", time.localtime())
print("Formatted time:", formatted_time)