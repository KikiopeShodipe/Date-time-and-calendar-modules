import random
from datetime import datetime, timedelta
# Ask the user for input
start_input = input("Enter the start date and time (YYYY-MM-DD HH:MM:SS): ")
end_input = input("Enter the end and time (YYYY-MM-DD HH:MM:SS): ")
# Prase the input into date time objectives
start_date = datetime.strptime(start_input, "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime(end_input, "%Y-%m-%d %H:%M:%S")
# Calculate the difference
time_difference = end_date - start_date
#Generate a random number of seconds
random_seconds = random.randint(0, int(time_difference.total_seconds()))
#Generate random datetime
random_datetime = start_date + timedelta(seconds=random_seconds)
print("Random date and time:", random_datetime)